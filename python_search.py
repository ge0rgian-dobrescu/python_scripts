"""
The purpose of this script is to search all the ".py" files in a location.
"""
import os
import subprocess
import sys

FILE_DIR_PATTERN = "python"

def find_python_files(source):
    py_files = []

    for root, dirs, files in os.walk(source):
        if FILE_DIR_PATTERN in os.path.basename(root).lower():
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root,file))
    return py_files


def main(source, target):
    cwd = os.getcwd() # gets the location of where we run the script from.
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    py_files = find_python_files(source_path)
    
    if not py_files:
        print ("No python files found in matching directories.")
        return
    print ("Found Python files:")
    for idx, path in enumerate(py_files, start = 1):
        print(f"{idx},{path}")


if __name__ == "__main__":
    args = sys.argv
    if(len(args)) != 3:
        raise Exception("You must pass a source and terget a directory - only.")

    source, target = args[1:3]
    main(source, target)
