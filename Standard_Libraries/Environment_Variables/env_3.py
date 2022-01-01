# this scripts counts the number of times it's ran based on a local .env file


import os
import dotenv

# returns the path to the filename (searches from CWD working upwards(searchs parents not childrens))
dot_env_file = dotenv.find_dotenv(r"script.env", raise_error_if_not_found=True)

dotenv.load_dotenv(dot_env_file)


number_of_times_this_script_is_run = int(os.environ.get("SCRIPT_COUNT"))

print(number_of_times_this_script_is_run)

number_of_times_this_script_is_run += 1


# changes value of a key for given .env file
# bothe key and value should be strings
dotenv.set_key(
    dot_env_file,
    key_to_set="SCRIPT_COUNT",
    value_to_set=str(number_of_times_this_script_is_run),
)
