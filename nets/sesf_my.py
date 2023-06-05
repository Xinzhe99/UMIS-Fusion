# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
import os
import torch
import torch.nn as nn
import torch.nn.functional as F


class CSELayer(nn.Module):
    def __init__(self, channel, reduction=16):
        super(CSELayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)


class SSELayer(nn.Module):
    def __init__(self, channel):
        super(SSELayer, self).__init__()
        self.fc = nn.Sequential(
            nn.Conv2d(channel, 1, kernel_size=1, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        y = self.fc(x)
        return x * y


class SCSELayer(nn.Module):
    def __init__(self, channel, reduction=16):
        super(SCSELayer, self).__init__()
        self.CSE = CSELayer(channel, reduction=reduction)
        self.SSE = SSELayer(channel)

    def forward(self, U):
        SSE = self.SSE(U)
        CSE = self.CSE(U)
        return SSE + CSE
class SESFuseNet(nn.Module):
    """
    The Class of SESFuseNet
    """

    def __init__(self, attention='cse',train_mode=True):
        super(SESFuseNet, self).__init__()
        # Encode
        self.train_mode=train_mode
        self.features = self.conv_block(in_channels=1, out_channels=16)
        self.conv_encode_1 = self.conv_block(16, 16)
        self.conv_encode_2 = self.conv_block(32, 16)
        self.conv_encode_3 = self.conv_block(48, 16)
        if (attention == 'cse'):
            self.se_f = CSELayer(16, 8)
            self.se_1 = CSELayer(16, 8)
            self.se_2 = CSELayer(16, 8)
            self.se_3 = CSELayer(16, 8)
        # Decode
        self.conv_decode_1 = self.conv_block(64, 64)
        self.conv_decode_2 = self.conv_block(64, 32)
        self.conv_decode_3 = self.conv_block(32, 16)
        self.conv_decode_4 = self.conv_block(16, 1)

    @staticmethod
    def conv_block(in_channels, out_channels, kernel_size=3):
        """
        The conv block of common setting: conv -> relu -> bn
        In conv operation, the padding = 1
        :param in_channels: int, the input channels of feature
        :param out_channels: int, the output channels of feature
        :param kernel_size: int, the kernel size of feature
        :return:
        """
        block = torch.nn.Sequential(
            torch.nn.Conv2d(kernel_size=kernel_size, in_channels=in_channels, out_channels=out_channels, padding=1),
            torch.nn.ReLU(),
            torch.nn.BatchNorm2d(out_channels),
        )
        return block

    @staticmethod
    def concat(f1, f2):
        """
        Concat two feature in channel direction
        """
        return torch.cat((f1, f2), 1)

    def forward(self,img1, kernel_radius=5):
        """
        Train or Forward for two images
        :param phase: str, 'train' or 'fuse'
        :param img1: torch.Tensor
        :param img2: torch.Tensor, only be used in 'fuse' mode
        :param kernel_radius: The kernel radius of spatial frequency
        :return: output, torch.Tensor
        """
        if self.train_mode:
            # Encode
            features = self.features(img1)
            se_features = self.se_f(features)
            encode_block1 = self.conv_encode_1(se_features)
            se_encode_block1 = self.se_1(encode_block1)
            se_cat1 = self.concat(se_features, se_encode_block1)
            encode_block2 = self.conv_encode_2(se_cat1)
            se_encode_block2 = self.se_2(encode_block2)
            se_cat2 = self.concat(se_cat1, se_encode_block2)
            encode_block3 = self.conv_encode_3(se_cat2)
            se_encode_block3 = self.se_3(encode_block3)
            se_cat3 = self.concat(se_cat2, se_encode_block3)
            # Decode
            decode_block1 = self.conv_decode_1(se_cat3)
            decode_block2 = self.conv_decode_2(decode_block1)
            decode_block3 = self.conv_decode_3(decode_block2)
            output = self.conv_decode_4(decode_block3)
        else:
            with torch.no_grad():
                # Encode
                features_1 = self.features(img1)

                se_features_1 = self.se_f(features_1)

                encode_block1_1 = self.conv_encode_1(se_features_1)

                se_encode_block1_1 = self.se_1(encode_block1_1)

                se_cat1_1 = self.concat(se_features_1, se_encode_block1_1)

                encode_block2_1 = self.conv_encode_2(se_cat1_1)

                se_encode_block2_1 = self.se_2(encode_block2_1)

                se_cat2_1 = self.concat(se_cat1_1, se_encode_block2_1)

                encode_block3_1 = self.conv_encode_3(se_cat2_1)

                se_encode_block3_1 = self.se_3(encode_block3_1)

                se_cat3_1 = self.concat(se_cat2_1, se_encode_block3_1)

            # SESF-Fuse calculate activity level
            output = self.fusion_channel_sf(se_cat3_1, kernel_radius=kernel_radius)
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
