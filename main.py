#Simple photo copy/rename tool
#Designed with uploading photos from a memory card in mind

#imports
import shutil
import os

#Gather user input
src_dir = input("Enter the path to photos: ")
album_name = input("Enter the title for the album: ")

#Make the desenation dir and change to it
dest_dir = "C:/Users/Tim/Pictures/{}/".format(album_name)
os.mkdir(dest_dir)
os.chdir(src_dir)

#For file name number
n = 0

#Go through files in that dir, copy them to dest dir, and rename them
for file in os.listdir():
    n+=1
    #Get the extension of file and set the dest file name
    ext = file.split(".")[-1]
    dest_file = "{}{}_{}.{}".format(dest_dir,album_name,n,ext)
    #Copy the file
    shutil.copy(file, dest_file)

print("Copied {} files to {}".format((n), dest_dir))