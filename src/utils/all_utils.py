import yaml
import os

def read_yaml(path_of_yaml_file:str) -> dict:
    with open(path_of_yaml_file) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content
