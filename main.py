from sys import argv

from raylib.static import *

from utils.helper import Screen, Fps

for arg in argv:
    argv[argv.index(arg)] = arg.lower()

try:
    if "fps" in argv:
        if argv[argv.index("fps") + 1] == "on":
            Fps.enabled = True
        else:
            Fps.enabled = False
except IndexError:
    Fps.enabled = False

SetTargetFPS(Fps.cap)
InitWindow(Screen.width, Screen.height, b"Test Platformer")

while not WindowShouldClose():
    BeginDrawing()
    ClearBackground(RAYWHITE)
    if fps:
        DrawFPS(Screen.width - 75, 0)
    EndDrawing()

CloseWindow()
