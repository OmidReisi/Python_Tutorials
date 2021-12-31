import shutil

# extracts the archive of filename in the extract_dir
# extract_dir creates the directories if they don't exist
shutil.unpack_archive(
    filename=r"./archived_files/archived_file_1.zip",
    extract_dir=r"./extracted_archives",
)