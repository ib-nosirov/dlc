import deeplabcut as dlc

config_path = '/work2/08229/inosirov/maverick2/60fps_preop-ib-2021-07-13/config.yaml'
#dlc.extract_frames(config_path, mode='automatic', algo='kmeans')

#config_path = '/Users/ib-nosirov/REU_2021/dlc_projects/60fps_preop-ib-2021-07-13/config.yaml'
#dlc.create_training_dataset(config_path)
#dlc.train_network(config_path, shuffle=1, trainingsetindex=0,
#max_snapshots_to_keep=5, displayiters=100, saveiters=5000, maxiters=500000)
#dlc.evaluate_network(config_path)
dlc.create_labeled_video(config_path, ['/work2/08229/inosirov/maverick2/60fps_preop-ib-2021-07-13/videos/IMG_4284.MOV'])
