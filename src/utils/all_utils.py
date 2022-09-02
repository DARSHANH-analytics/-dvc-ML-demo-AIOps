from genericpath import exists
import yaml
import os

def read_yaml(path_of_yaml_file:str) -> dict:
    with open(path_of_yaml_file) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dirs):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"directory is created at {dir_path}")