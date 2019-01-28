#code to fetch windows 10 spotlight wallpapers
import os
import sys
import shutil
import datetime
from PIL import Image
src_path = "C:/Users/chinm/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
tar_path = "D:/Python Practice/Windows Spotlight/Raw_Files/"
formatted_files_path="D:/Python Practice/Windows Spotlight/Formatted_Files/"
desktop_wall_path="D:/Python Practice/Windows Spotlight/Desktop_Wallpapers/"
mobile_wall_path="C:/Users/chinm/Documents/Win_Spotlight_Mobile_Wallpapers/"
curr_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
formatted_files_path_str = os.listdir(formatted_files_path)
src_files = os.listdir(src_path)
tar_files = os.listdir(tar_path)
tar_files_list = []
i = 0
for tar_file in tar_files:
    tar_files_list.append(str(tar_file))


for src_file in src_files:
    if(tar_files_list.count(str(src_file)) == 0):
        print("found missing src file :: "+src_file)
        shutil.copy(src_path+src_file,tar_path)
        shutil.copy(src_path+src_file,formatted_files_path)
        file_name='Picture_'+str(curr_time)+'_'+str(i)+'.jpg'
        os.rename(os.path.join(formatted_files_path, src_file), os.path.join(formatted_files_path,file_name))
        image = Image.open(formatted_files_path+file_name)
        image_size = str(image.size)
        print("file :: "+file_name+" :: "+image_size)
        if(image_size.find("1080, 1920") != -1):
            print("inside if "+str(image.size))
            shutil.copy(formatted_files_path+file_name,mobile_wall_path)
        elif(image_size.find("1920, 1080") != -1):
            print("inside else "+str(image.size))
            shutil.copy(formatted_files_path+file_name,desktop_wall_path)
        else:
            print("Size is not supported for file :: "+file_name)
            
        i = i+1
