""" Creates and manages assets """
import os
def create_asset(project_path : str, asset_type : str, asset_name : str):
    asset_path = os.path.join(project_path, "assets", asset_type, asset_name)
    os.makedirs(os.path.join(asset_path, "work"))
    os.makedirs(os.path.join(asset_path, "publish"))

    return asset_path
