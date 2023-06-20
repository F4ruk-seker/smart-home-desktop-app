import os
import subprocess
from pathlib import Path
import nicegui
from config import BASE_DIR

# cmd = ['cd ', f'{BASE_DIR}/venv/Scripts']
# subprocess.call(cmd)
# cmd = ['activate']
# subprocess.call(cmd)

print('--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui')
#
# cmd = [
#     'python',
#     '-m', 'PyInstaller',
#     'main.py', # your main file with ui.run()
#     '--name', 'SmartHome', # name of your app
#     '--onefile',
#     '--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
#     '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
# ]
# subprocess.call(cmd)

