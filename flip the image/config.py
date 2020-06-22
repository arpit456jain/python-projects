import os
image_size = 128
screen_size = 512
num_tiles_side = 4
num_tiles_total = 16
margin = 4

asset_dir = 'assets'
asset_files = [x for x in os.listdir(asset_dir) if x[-3:].lower() == 'png']

assert len(asset_files) == 8
