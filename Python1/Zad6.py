import os
from PIL import Image

dir_path = ".\\Images"  # directory path
files = os.listdir(dir_path)
number_files = len(files)
for i in range(0, number_files):
    im = Image.open(dir_path + "\\"+files[i])
    print(dir_path + "\\"+files[i])
    path = dir_path + "\\"+files[i].rsplit('.', 1)[0] + ".png"
    im.save(path, "PNG")


