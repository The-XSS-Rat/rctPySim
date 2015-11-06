import sys
from cx_Freeze import setup, Executable

includefiles = ['data/dolphin-show.png','data/down.png','data/grasstile.png','data/haunted-mansion.png','data/maze.png','data/merry-go-round.PNG','data/observatory.png','data/random.png',
'data/space-sim.png','data/up.png','data/down.png','data/water_slide.png','data/btnDecoration.png','data/btnAttractions.png','data/tree1.png','data/tree2.png','data/tree3.png',]

setup(
    name = "rctPySim",
    version = "0.1.1",
    description = "Theme Park Py Sim",
    options = {'build_exe': {'include_files':includefiles}}, 
    executables = [Executable("C:\\Users\\mxtwt\\Desktop\\Python scripts\\rctPySim\\MainGame.py"),])

