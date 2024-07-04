from pathlib import Path
from typing import Set


SOURCE_PARENT = Path.home().joinpath("Downloads")
DESTINATION_PARENT = Path.home().joinpath("Pictures")


def get_file_count_from(folder: Path) -> int:
    """
    Get the number of files in a folder.
    """
    file_count : int = 0
    for item in folder.iterdir():
        if item.is_file():
            file_count += 1
    return file_count


def main():

    try:
        
        valid_extenstions : Set = {".avif", ".bmp", ".jpg", ".JPG", ".jpeg", ".png", ".webp"}
 
        for folder in (item for item in SOURCE_PARENT.iterdir() if item.is_dir()):
            destination_child = DESTINATION_PARENT.joinpath(folder.name)
            destination_child.mkdir(exist_ok = True)
            current_file_count = get_file_count_from(folder = destination_child) + 1
            
            print(f"Source: {folder} Destination: {destination_child}")

            images = (item for item in folder.iterdir() if item.is_file() and 
                      item.suffix in valid_extenstions)

            for index, source in enumerate(iterable = images, start = current_file_count):
                destination = Path(str(index)).with_suffix(source.suffix)
                print(f"{source.name} -> {destination.name}")
                source.rename(destination_child.joinpath(destination))

            print(f"Remove: {folder}")
            folder.rmdir()
            print("\n")
            
    except(FileExistsError, OSError) as e:
        print(e)
    
if __name__ == '__main__':
    main()
