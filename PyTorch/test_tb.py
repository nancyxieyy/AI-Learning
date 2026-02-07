from tensorboard.summary.v1 import image
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import  Image

writer = SummaryWriter("logs")
image_path = "data/train/ants_image/0013035.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("test", img_array, 1, dataformats="HWC")
# y = 2x
for i in range(100):
    # 标题， y， x
    writer.add_scalar("y=2x", 2*i, i)

writer.close()