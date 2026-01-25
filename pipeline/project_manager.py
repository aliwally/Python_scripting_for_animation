""" Creates the structure of the project """

import os

def create_project_structure (root_path : str, project_name : str):
    """ 1 - Create the path
        2 - Create all necessary folders"""
    project_path = os.path.join(root_path, project_name)

    folders_to_create = [ "assets/characters", "assets/props", "assets/sets", "shots", "publish"]

    for f in folders_to_create:
        path = os.path.join(project_path, f)
        os.makedirs(path,exist_ok=True)
    
    return project_path