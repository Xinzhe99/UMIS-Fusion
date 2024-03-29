# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
# ref Unet++: Redesigning skip connections to exploit multiscale features in image segmentation
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.fft


# ref SESF-Fuse: an unsupervised deep model for multi-focus image fusion
class CSELayer(nn.Module):
    def __init__(self, channel, reduction=2):
        super(CSELayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.GELU(),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)

class VGGBlock(nn.Module):
    def __init__(self, in_channels, middle_channels, out_channels):
        super().__init__()
        self.relu6 = nn.ReLU6()
        self.conv1 = nn.Conv2d(in_channels, middle_channels, 7, padding=3)
        self.bn1 = nn.BatchNorm2d(middle_channels)
        self.conv2 = nn.Conv2d(middle_channels, out_channels, 7, padding=3)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.att=CSELayer(out_channels)
    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu6(out)

        out = self.conv2(out)

        out = self.bn2(out)
        out = self.att(out)
        out = self.relu6(out)

        return out
class Up(nn.Module):
    def __init__(self):
        super().__init__()
        self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # input is CHW
        diffY = torch.tensor([x2.size()[2] - x1.size()[2]])
        diffX = torch.tensor([x2.size()[3] - x1.size()[3]])

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        return x

class NestedUNet(nn.Module):
    def __init__(self, train_mode=True, input_channels=1, **kwargs):
        super().__init__()

        nb_filter = [16, 16, 32, 32, 64]
        recon_filter=[16,8,4,1]
        self.train_mode=train_mode

        self.pool = nn.MaxPool2d(2, 2)
        self.up = Up()

        self.conv0_0 = VGGBlock(input_channels, nb_filter[0], nb_filter[0])
        self.conv1_0 = VGGBlock(nb_filter[0], nb_filter[1], nb_filter[1])
        self.conv2_0 = VGGBlock(nb_filter[1], nb_filter[2], nb_filter[2])
        self.conv3_0 = VGGBlock(nb_filter[2], nb_filter[3], nb_filter[3])
        self.conv4_0 = VGGBlock(nb_filter[3], nb_filter[4], nb_filter[4])

        self.conv0_1 = VGGBlock(nb_filter[0] + nb_filter[1], nb_filter[0], nb_filter[0])
        self.conv1_1 = VGGBlock(nb_filter[1] + nb_filter[2], nb_filter[1], nb_filter[1])
        self.conv2_1 = VGGBlock(nb_filter[2] + nb_filter[3], nb_filter[2], nb_filter[2])
        self.conv3_1 = VGGBlock(nb_filter[3] + nb_filter[4], nb_filter[3], nb_filter[3])

        self.conv0_2 = VGGBlock(nb_filter[0] * 2 + nb_filter[1], nb_filter[0], nb_filter[0])
        self.conv1_2 = VGGBlock(nb_filter[1] * 2 + nb_filter[2], nb_filter[1], nb_filter[1])
        self.conv2_2 = VGGBlock(nb_filter[2] * 2 + nb_filter[3], nb_filter[2], nb_filter[2])

        self.conv0_3 = VGGBlock(nb_filter[0] * 3 + nb_filter[1], nb_filter[0], nb_filter[0])
        self.conv1_3 = VGGBlock(nb_filter[1] * 3 + nb_filter[2], nb_filter[1], nb_filter[1])

        self.conv0_4 = VGGBlock(nb_filter[0] * 4 + nb_filter[1], nb_filter[0], nb_filter[0])


        self.recon1 = nn.Conv2d(nb_filter[0], recon_filter[0], kernel_size=7, padding=3)
        self.recon2 = nn.Conv2d(recon_filter[0],recon_filter[1] , kernel_size=7, padding=3)
        self.recon3 = nn.Conv2d(recon_filter[1], recon_filter[2], kernel_size=7, padding=3)
        self.recon4 = nn.Conv2d(recon_filter[2], recon_filter[3], kernel_size=7, padding=3)

    def forward(self, input):
        x0_0 = self.conv0_0(input)
        x1_0 = self.conv1_0(self.pool(x0_0))
        x0_1 = self.conv0_1(self.up(x1_0, x0_0))

        x2_0 = self.conv2_0(self.pool(x1_0))
        x1_1 = self.conv1_1(self.up(x2_0, x1_0))
        x0_2 = self.conv0_2(self.up(x1_1, torch.cat([x0_0, x0_1], 1)))

        x3_0 = self.conv3_0(self.pool(x2_0))
        x2_1 = self.conv2_1(self.up(x3_0, x2_0))
        x1_2 = self.conv1_2(self.up(x2_1, torch.cat([x1_0, x1_1], 1)))
        x0_3 = self.conv0_3(self.up(x1_2, torch.cat([x0_0, x0_1, x0_2], 1)))

        x4_0 = self.conv4_0(self.pool(x3_0))
        x3_1 = self.conv3_1(self.up(x4_0, x3_0))
        x2_2 = self.conv2_2(self.up(x3_1, torch.cat([x2_0, x2_1], 1)))
        x1_3 = self.conv1_3(self.up(x2_2, torch.cat([x1_0, x1_1, x1_2], 1)))
        x0_4 = self.conv0_4(self.up(x1_3, torch.cat([x0_0, x0_1, x0_2, x0_3], 1)))

        if self.train_mode:
            recon1 = self.recon1(x0_4)
            recon2 = self.recon2(recon1)
            recon3 = self.recon3(recon2)
            output = self.recon4(recon3)
        else:
            with torch.no_grad():
                # recon1 = self.recon1(x0_4)
                output=self.fusion_channel_sf(x0_4, kernel_radius=15)#todo 参数用多大要自己改 默认15
        return output

    @staticmethod
    # ref SESF-Fuse: an unsupervised deep model for multi-focus image fusion
    def fusion_channel_sf(f1, kernel_radius=5):  # default=5
        """
        Perform channel sf fusion two features
        """
        device = f1.device
        b, c, h, w = f1.shape  # 假设[1,80,5,5]
        r_shift_kernel = torch.FloatTensor([[0, 0, 0], [1, 0, 0], [0, 0, 0]]) \
            .reshape((1, 1, 3, 3)).repeat(c, 1, 1, 1).to(
            device)  # 卷积核weight.shape=[out_channels,in_channels,h,w]  这里c==out_channels
        b_shift_kernel = torch.FloatTensor([[0, 1, 0], [0, 0, 0], [0, 0, 0]]) \
            .reshape((1, 1, 3, 3)).repeat(c, 1, 1, 1).to(device)  # 需要输出维度个卷积核 所以要repeat成c个
        f1_r_shift = F.conv2d(f1, r_shift_kernel, padding=1, groups=c).to(
            device)  # 每组计算被in_channels/groups个channels的卷积核计算
        f1_b_shift = F.conv2d(f1, b_shift_kernel, padding=1, groups=c).to(
            device)  # 对输入tensor f1 进行卷积操作，卷积核为x_shift_kernel 且都用同一个卷积核计算
        f1_grad = torch.sqrt(torch.pow((f1_r_shift - f1), 2) + torch.pow((f1_b_shift - f1), 2)).to(
            device)  # RF^2+CF^2  RF与SF 两幅特征图相加的图
        kernel_size = kernel_radius * 2 + 1  # 2R+1
        add_kernel = torch.ones((c, 1, kernel_size, kernel_size)).float().to(device)  # [80,1,11,11]
        kernel_padding = kernel_size // 2  # padding==5
        f1_sf = torch.sum(F.conv2d(f1_grad, add_kernel, padding=kernel_padding, groups=c), dim=1).to(device)
        f1_sf_np = f1_sf.squeeze()
        return f1_sf_np



# device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# inputs = torch.randn((1, 1, 156, 156)).to(device)
# model = NestedUNet(num_classes=1,training=True).to(device)
# outputs = model(inputs)
# print(outputs.shape)