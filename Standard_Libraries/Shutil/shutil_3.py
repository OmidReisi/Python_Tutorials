import shutil

shutil.make_archive(
    base_name=r"./archived_files/archived_file_2",
    format="gztar",
    base_dir=r"./Images",
)
