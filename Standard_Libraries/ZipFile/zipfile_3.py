from os import name, path
import zipfile
from PIL import Image

with zipfile.ZipFile(file=r"./zipfiles/files_2.zip", mode="r") as my_zip:

    # shows the name of files in the zip file
    print(my_zip.namelist())

    # open a file in the zip file
    # mode should be same as the mode of the zip file
    # just like members explaind down blow don't use ./ for name of file in zip file
    img = my_zip.open(name=r"Original_Images/image_1.jpg", mode="r")
    img = Image.open(img)
    img.show()

    # returns the content of the file in the zip file in bytes
    # you can't actually open image from the return of my_zip.read()
    # this is bytes object and not actually an image object
    img_content = my_zip.read(name=r"Original_Images/image_2.jpg")

    # extracts the zip file to the given path
    # you can specify the memebers argument to specify which files should be extracted
    # when passing members it should be a subset of namelist() method so don't use ./ as in path to file. you have to use the filename(including it's directories but don't use ./)
    my_zip.extractall(members=[r"Original_Images/image_1.jpg"], path="./extractedfiles")
