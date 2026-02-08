""" User Interface """

import maya.cmds as cmds
from pipeline.project_manager import create_project_structure

def launch_ui():
    if cmds.window("pipelineUI", exists=True):
        cmds.deleteUI("pipelineUI")

    window = cmds.window("pipelineUI", title="Asset Pipeline Manager")

    main_layout = cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Create Project")
    cmds.button(
        label="Create Project Structure",
        command=lambda x: create_project_structure("C:/temp", "MyProject")
    )

    cmds.showWindow(window)