""" Used to link the project to Maya """
import maya.cmds as cmd

def save_scene (path : str):
    """"""
    cmd.file(rename = path)
    cmd.file(save = True, type = "mayaAscii")

def open_scene (path : str):
    """"""
    cmd.file(path, open = True, force = True)