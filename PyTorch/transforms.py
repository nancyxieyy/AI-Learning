from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image

from test_tb import writer

# python的用法 -> tensor数据类型
# 通过 transforms.ToTensor 去解决两个问题
# 1. transforms 该如何使用
# 2. 为什么我们需要 Tensor 数据类型


img_path = "data/train/ants_image/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

# 1. transforms 该如何使用
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

print(tensor_img)

writer.add_image("Tensor_img", tensor_img)