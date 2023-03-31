from data_converter.nuscenes_converter_seg import  create_nuscenes_infos



if __name__ == '__main__':
    # Training settings
    # 使用nuscenes-mini数据集
    create_nuscenes_infos( './data/nuscenes','HDmaps-final',version='v1.0-mini')

