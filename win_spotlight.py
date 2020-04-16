#code to fetch windows 10 spotlight wallpapers

__author__= 'Chinmay Khare'
__version__='2'

import os
import sys
import shutil
import datetime
import traceback
from PIL import Image


tar_path = os.path.join(os.curdir,'Raw_Files')
formatted_files_path=os.path.join(os.curdir,'Formatted_Files')
desktop_wall_path=os.path.join(os.curdir,'Desktop_Wallpapers')
mobile_wall_path=os.path.join(os.curdir,'Win_Spotlight_Mobile_Wallpapers')

def createDir():
    ''' 
    Create required directories
    '''
    dir_list=['Raw_Files','Formatted_Files','Desktop_Wallpapers','Win_Spotlight_Mobile_Wallpapers']
    for dir in dir_list:
        dir_path=os.path.join(os.curdir,dir)
        if(os.path.isdir(dir_path) == False):
            os.mkdir(dir_path)


def fetchWallpapers():
    curr_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # formatted_files_path_str = os.listdir(formatted_files_path)
    src_files = os.listdir(src_path)
    tar_files = os.listdir(tar_path)
    tar_files_list = []
    i = 0
    for tar_file in tar_files:
        tar_files_list.append(str(tar_file))


    for src_file in src_files:
        if(tar_files_list.count(str(src_file)) == 0):
            print("found missing src file :: "+src_file)
            shutil.copy(os.path.join(src_path,src_file),tar_path)
            shutil.copy(os.path.join(src_path,src_file),formatted_files_path)
            file_name='Picture_'+str(curr_time)+'_'+str(i)+'.jpg'
            os.rename(os.path.join(formatted_files_path, src_file), os.path.join(formatted_files_path,file_name))
            image = Image.open(os.path.join(formatted_files_path,file_name))
            image_size = str(image.size)
            print("file :: "+file_name+" :: "+image_size)
            if(image_size.find("1080, 1920") != -1):
                print("inside if "+str(image.size))
                shutil.copy(os.path.join(formatted_files_path,file_name),mobile_wall_path)
            elif(image_size.find("1920, 1080") != -1):
                print("inside else "+str(image.size))
                shutil.copy(os.path.join(formatted_files_path,file_name),desktop_wall_path)
            else:
                print("Size is not supported for file :: "+file_name)
                
            i = i+1

if __name__ == "__main__":
    src_path=os.path.join(os.environ['USERPROFILE'],'AppData','Local','Packages','Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy','LocalState','Assets')
    if(os.path.isdir(src_path)):
        createDir()
        fetchWallpapers()
    else:
        print('Please correct the Micosoft Spotlight directory')
