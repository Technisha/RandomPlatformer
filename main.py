from sys import argv

from raylib.static import *

from utils.helper import Screen, Fps, Vector2
from utils.entities import Entity

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

player = Entity('assets/player/walk.png', 64, 234, 4, Vector2(424, 230))

while not WindowShouldClose():
    BeginDrawing()
    if Fps.enabled:
        DrawFPS(Screen.width - 75, 0)
    if IsMouseButtonPressed(MOUSE_LEFT_BUTTON):
        print(f"X: {GetMouseX()}\nY: {GetMouseY()}")
        player.pos.x = GetMouseX()
        player.pos.y = GetMouseY()
    player.draw()
    ClearBackground(RAYWHITE)
    EndDrawing()

CloseWindow()
