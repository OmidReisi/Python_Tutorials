import zipfile

with zipfile.ZipFile(file=r"./zipfiles/files_2.zip", mode="r") as my_zip:

    # if you want to extract only one file use this method
    my_zip.extract(member=r"Original_Images/image_1.jpg", path=r"./extractedfiles")
