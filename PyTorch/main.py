import torch

# 打印版本号
print(f"PyTorch version: {torch.__version__}")

# 检查显卡加速是否可用 (Mac M1/M2/M3 芯片通常是 MPS)
if torch.backends.mps.is_available():
    print("恭喜！你的 Mac GPU 加速 (MPS) 已开启！")
elif torch.cuda.is_available():
    print("CUDA (NVIDIA) 可用！")
else:
    print("目前在使用 CPU 模式。")