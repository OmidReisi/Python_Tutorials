import requests
import zipfile

r = requests.get(
    r"https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip"
)

# the following piece of code opens a normal file with .zip extention and stores the content of our downloaded zip file in it
# then we open the newly created file as a zip file and copy the contents of it in a new zip file in order to achive compresion
file_name = r"./stackoverflow_survey/data_2021.zip"
with open(file=file_name, mode="wb") as f:
    f.write(r.content)

with zipfile.ZipFile(file=r"./stackoverflow_survey/data_2021.zip", mode="r") as my_zip:
    with zipfile.ZipFile(
        # zipfile.ZIP_BZIP2 is another compression method (also zipfile.ZIP_LZMA)
        file=r"./data.zip",
        mode="w",
        compression=zipfile.ZIP_BZIP2,
    ) as data_file:
        for file_name in my_zip.namelist():
            # in order to write bytes to a zip file we use writestr method
            data_file.writestr(
                zinfo_or_arcname=file_name, data=my_zip.read(name=file_name)
            )
