# shutil is another library for archiving directories with different archiving modes(zip, gzip, ...)
# note that shutil can only archive directories and can't archive files seperatly
import shutil

# basename represent the name and location of your archive file without it's format
# format represent the formt of your archive file
# base_dir represents the directory you want to archive
# root_dir is used when you want to remove the in between directories so you set the root_dir to the partent of the directory you want to archive
# this method returns the name of the archived file (if you've set root_dir it returns the absolute path otherwise it returns a relative path
print(
    shutil.make_archive(
        base_name=r"./archived_files/archived_file_1",
        format="zip",
        root_dir=r"./Images",
        base_dir=r"./Original_Images",
    )
)
