import numpy as np
import deeplabcut as dlc

dlc.create_new_project('example', 'ib',
                       ['/Users/ib-nosirov/Example/IMG_4284.MOV'],
                       working_directory='/Users/ib-nosirov/Example')

config_path = '/Users/ib-nosirov/Example/example-ib-2021-09-06/config.yaml'

dlc.extract_frames(config_path, mode='automatic', algo='kmeans', crop=True)

dlc.label_frames(config_path)

dlc.create_training_dataset(config_path, augmenter_type='imgaug')
