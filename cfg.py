# -*- coding:utf-8 -*-
# @time :2019.09.07
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju


##数据集的类别
NUM_CLASSES = 40

#训练时batch的大小
BATCH_SIZE = 64

#网络默认输入图像的大小
INPUT_SIZE = 224

##预训练模型的存放位置
#下载地址：https://download.pytorch.org/models/densenet169-b2777c0a.pth
PRETRAINED_MODEL = './dense169.pth'

#数据集的存放位置
TRAIN_DATASET_DIR = './datasets/train_data_v2'
VAL_DATASET_DIR = './datasets/val_data_v2'
