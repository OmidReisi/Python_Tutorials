import zipfile


# just like files you can use context managers with zip files as well so you don't have to close them
# by default our zip files doesn't compress anything
# in order to apply compression we have to set compression = zipfile.ZIP_DEFLATED
with zipfile.ZipFile(
    file=r"./zipfiles/files_2.zip", mode="w", compression=zipfile.ZIP_DEFLATED
) as my_zip:
    my_zip.write(r"./Original_Images/image_1.jpg")
    my_zip.write(r"./Original_Images/image_2.jpg")


