__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
import zipfile


def main():
    clean_cache()
    zip_path = os.path.join(current_directory, "files", "data.zip")
    directory_path = os.path.join(current_directory, "files", "cache")
    cache_zip(zip_path, directory_path)
    print(cached_files())
    print(find_password(cached_files()))


# Global variables
current_directory = os.getcwd()
cache_directory = (
    os.path.join(current_directory, "cache")
    if current_directory.endswith("files")
    else os.path.join(current_directory, "files", "cache")
)


# 1. Create an empty cache directory
def clean_cache():
    # Create a cache directory if it doesn't exist
    if not os.path.exists(cache_directory):
        try:
            os.mkdir(cache_directory)
            print(f"Directory {cache_directory} has been created.")

        except OSError as e:
            print(f"Creation of the directory {cache_directory} failed. {e}")

    # Delete everything in cache directory if it already exists
    else:
        print(
            f"There is already a directory called cache. Deleting everything in {cache_directory}."
        )

        # If cache directory is not empty, delete everything in this directory
        for item in os.listdir(cache_directory):
            # Get path of the item in the cache directory
            item_path = os.path.join(cache_directory, item)

            try:
                # If item is a file or symbolic link, delete it
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    print(f"{item_path} has been deleted.")

                # if item is a directory, delete it
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"{item_path} has been deleted.")

            except OSError as e:
                print(f"{item_path} couldn't be deleted. {e}")

        print(f"{cache_directory} is empty")


# 2. Unpack an indicated zip file into a clean cache folder
def cache_zip(zip_file_path, cache_dir_path):
    # Create a clean cache folder
    clean_cache()

    try:
        # Unpack zip file in desired folder
        with zipfile.ZipFile(zip_file_path, "r") as zip:
            zip.extractall(os.path.join(cache_dir_path))

    except zipfile.error as e:
        print(f"Unable to unpack {zip_file_path}. {e}")


# 3. Get a list of all the files in the cache folder
def cached_files():
    files = []
    if os.path.exists(cache_directory):
        for item in os.listdir(cache_directory):
            # Get path of the item in the cache directory
            item_path = os.path.join(cache_directory, item)
            # If item is not a directory, add it to the list
            if not os.path.isdir(item_path):
                files.append(item_path)
    return files


# 4. Find the password
def find_password(cached_files):
    for file_path in cached_files:
        try:
            # Read every file in the list
            with open(file_path, "r") as file:
                # Check every line for password. Stop searching when it's found
                for line in file:
                    if "password" in line:
                        print(f"Password found in {file_path}")
                        password = line.strip("password: \n")
                        return password
            # Close file after reading
            file.close()

        except OSError as e:
            print(f"Unable to open/read file {file_path}. {e}")


if __name__ == "__main__":
    main()
