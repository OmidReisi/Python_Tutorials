import zipfile

# creates a new zipfile with the given path and name in the given mode
# modes are just like file modes (r,w,a,...)
my_zip = zipfile.ZipFile(file=r"./zipfiles/files_1.zip", mode="w")

# adds the given file to your zip file
# if the path to file contains directories as well it adds the directories to the zip file as well
# if you want to remove the in between directories you have to set the arcname argument
my_zip.write(r"./Original_Images/image_1.jpg")
my_zip.write(r"./Original_Images/image_2.jpg", arcname=r"image_2.jpg")

# closes the zip file
my_zip.close()
