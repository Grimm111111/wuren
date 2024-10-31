import pickle
import numpy as np

# 读取 .pkl 文件
with open('D:/AI Competition/TE-GCN-main/work_dir/3003/epoch1_test_score.pkl', 'rb') as f:
    data = pickle.load(f)

# 打印字典中的所有键名
print("Dictionary keys:", data.keys())

# 提取所有样本并合并为一个数组
samples = []
for key in data:
    sample_data = data[key]
    if isinstance(sample_data, np.ndarray) and sample_data.shape == (155,):
        samples.append(sample_data)
    else:
        print(f"Skipping key '{key}' due to shape {sample_data.shape}.")

# 检查样本数量是否足够
if len(samples) >= 4599:
    # 将样本合并成一个二维数组
    combined_data = np.array(samples[:4599])  # 取前 2000 个样本
    print(f"Combined data shape: {combined_data.shape}")

    # 保存为 .npy 文件
    np.save('D:/AI Competition/TE-GCN-main/eval/pred.npy', combined_data)
    print("Combined data has been saved as .npy")
else:
    print(f"Not enough samples to create a (4599, 155) array. Found: {len(samples)} samples.")
