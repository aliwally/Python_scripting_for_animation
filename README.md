# Python_scripting_for_animation

This repository presents some small projects I did in order to familiarise myself with what python scripting for animation looks like.

So far, when executed in Maya, the script `script_to_use_in_maya.py` prompts the user to create a project and creates a structured set of folders for characters, props, and sets, following a typical animation pipeline.

## Features

- Maya UI to create a new project structure
- Automatically generates folders for assets (characters, props, sets), shots, and publish
- Modular code: project management, asset management, versioning, Maya integration, and UI

## Project Structure

```
Python_scripting_for_animation/
│
├── pipeline/
│   ├── __init__.py
│   ├── project_manager.py
│   ├── asset_manager.py
│   ├── versioning.py
│   ├── maya_utils.py
│   └── ui.py
│
├── main.py
├── script_to_use_in_maya.py
└── README.md
```

## How to Use

1. Open Maya.
2. In the Script Editor, run:
	```python
	import sys
	sys.path.append("C:/Users/alice/Python_scripting_for_animation")
	import main
	main.launch_ui()
	```
3. Use the UI to create a new project structure at the specified location.
