import os

# os.chdir(r"./Original_Files")

# print(os.getcwd())


for file in os.listdir(r"./Original_Files"):

    # print(file)

    file_name, file_ext = os.path.splitext(file)

    # print(file_name)

    file_title, file_course, file_num = file_name.split(" - ")

    # print((file_title, file_course, file_num))

    # zfill method is same as zero padding in formatting but it works on strings (numeric strings) instead of numbers
    # print(f"{file_num[1:].zfill(2)}-{file_course}-{file_title}{file_ext}")

    new_file_name = f"{file_num[1:].zfill(2)}-{file_course}-{file_title}{file_ext}"

    with open(f"./Renamed_Files/{new_file_name}", "w") as file:
        file.write(f"This file was renamed to: {new_file_name}")
