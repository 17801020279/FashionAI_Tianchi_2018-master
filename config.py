import os
# 2 gpus
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

# path to train and test labels
TRAIN_LABEL_DIR = 'F:/BaiduNetdiskDownload/Fashion_AI_Clothing attribute label/fashionAI_attributes_train1/Annotations/label_1.csv'
TEST_LABEL_DIR = 'datasets/final-rank/Tests/question.csv'

TRAIN_LENGTH_LABEL_DIR = 'F:/BaiduNetdiskDownload/Fashion_AI_Clothing attribute label/train_length_2.csv'
TRAIN_DESIGN_LABEL_DIR = 'F:/BaiduNetdiskDownload/Fashion_AI_Clothing attribute label/train_design_2.csv'
# 原始
# TEST_DESIGN_LABEL_DIR = 'labels/test_design.csv'
# TEST_LENGTH_LABEL_DIR = 'labels/test_length.csv'

# path to train and test images
TRAIN_IMG_DIR = 'F:/BaiduNetdiskDownload/Fashion_AI_Clothing attribute label/fashionAI_attributes_train1/'
TEST_IMG_DIR =  'datasets/final-rank/'

# path to trianed models
MODEL_LENGTH_INCEPTIONV4 =  'models/length_inceptionv4_480_12.h5'
MODEL_LENGTH_INCEPTIONRESNETV2 = 'models/length_inceptionresnet_480_12.h5'
MODEL_DESIGN_INCEPTIONV4 = 'models/design_inceptionv4_480_13.h5'
MODEL_DESIGN_INCEPTIONRESNETV2 = 'models/design_inceptionresnet_480_8.h5'


task_list_length = {
    'pant_length': 6,
    'skirt_length': 6,
    'sleeve_length': 9,
    'coat_length': 8
}

task_list_design = {
    'collar_design': 5,
    'lapel_design': 5,
    'neckline_design': 10,
    'neck_design': 5,
}

# input size
width = 480
model_name = 'inceptionv4'
