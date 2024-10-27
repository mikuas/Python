# import torch
#
# print("PyTorch 版本:", torch.__version__)
# print("CUDA 可用:", torch.cuda.is_available())
# print("CUDA 版本:", torch.version.cuda)
# print("当前设备:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "无 GPU 可用")
#
#
#
#

import random

result = 0

while result != 10:
    result = random.randint(0, 10)
    print(result)