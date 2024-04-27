import numpy as np
import os
from glob import glob
import imageio.v2 as imageio

def load_timestamps(data_path):
    ts_path = os.path.join(data_path, 'timestamps.txt')
    timestamps = np.loadtxt(ts_path, delimiter=' ', usecols=1)
    return timestamps

def load_images(data_path):
    images = []
    for img_file in sorted(glob(os.path.join(data_path, '*.png'))):
        img_data = imageio.imread(img_file)
        images.append(img_data)
    return np.array(images)

def load_depth(data_path):
    depth_data = []
    for depth_file in sorted(glob(os.path.join(data_path, '*.npy'))):
        depth_img = np.load(depth_file)
        depth_data.append(depth_img)
    return np.array(depth_data)

def load_events(data_path):
    events_with_ts = []
    for npz_file in sorted(glob(os.path.join(data_path, '*.npz'))):
        with np.load(npz_file, allow_pickle=True) as data:
            # 构造结构化事件数据
            events = np.array(list(zip(data['x'], data['y'], data['t'], data['p'])),
                              dtype=[('x', 'u2'), ('y', 'u2'), ('t', 'i8'), ('pol', 'bool')])
            events_with_ts.append(events)
    return events_with_ts

def load_data(base_path, data_types):
    data_dict = {}
    timestamps = load_timestamps(os.path.join(base_path, 'events', 'data'))
    for data_type in data_types:
        print(f'Loading {data_type} data...')
        data_path = os.path.join(base_path, data_type, 'data')

        if data_type in ['semantic', 'rgb']:
            data = load_images(data_path)
            data_with_ts = [(d, t) for d, t in zip(data, timestamps)]
        elif data_type == 'depth':
            data = load_depth(data_path)
            data_with_ts = [(d, t) for d, t in zip(data, timestamps)]
        elif data_type == 'events':
            events = load_events(data_path)
            data_with_ts = [(e, t) for e, t in zip(events, timestamps)]
        else:
            raise ValueError(f"Unrecognized data type: {data_type}")

        data_dict[data_type] = np.array(data_with_ts, dtype=object)

    return data_dict

def save_to_npz(data_dict, output_file):
    print(f'Saving data to {output_file}...')
    np.savez_compressed(output_file, **data_dict)
    print('Data has been saved successfully.')


def process_sequence_folder(sequence_folder):
    base_path = os.path.join("E:/My_Project/DLProject/dataset/eventscape/", sequence_folder)
    data_types = ['semantic', 'rgb', 'depth', 'events']

    # 准备输出文件路径
    output_file = os.path.join(base_path, f"{sequence_folder}.npz")

    # 调用函数处理和保存数据
    data_dict = load_data(base_path, data_types)
    save_to_npz(data_dict, output_file)
    print(f"Data for {sequence_folder} processed and saved to {output_file}")


# 获取所有sequence文件夹
base_folder = "E:/My_Project/DLProject/dataset/eventscape/"
all_sequence_folders = [folder for folder in os.listdir(base_folder) if folder.startswith('sequence')]

# 遍历并处理每一个sequence文件夹
for sequence_folder in all_sequence_folders:
    full_path = os.path.join(base_folder, sequence_folder)
    if os.path.isdir(full_path):  # 确保它是一个目录
        process_sequence_folder(sequence_folder)
