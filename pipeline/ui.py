""" User Interface """

import maya.cmds as cmd
from pipeline.project_manager import create_project_structure

def launch_ui():
    """"""
    if cmd.window ("pipelineUI", exists = True):
        cmd.delete("pipelineUI")
    window = cmd.window("pipelineUI", title = "Asset Pipeline Manager")
    cmd.columnLayout(adjustableColumn = True)
    
    cmd.text(label="Create Project")
    cmd.button(label="Create Project Structure",
                command=lambda x: create_project_structure("C:/temp", "MyProject"))

    cmd.showWindow(window)