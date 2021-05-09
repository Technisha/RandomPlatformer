from sys import argv

from raylib.static import *

from utils.helper import Screen, Fps, Sprite, Vector2
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

player = Entity(Sprite('assets/player/walk.png', Vector2(64, 234), 4, 4, 12, 0.35), Vector2(Screen.width / 25, Screen.height - (Screen.height / 6)))

while not WindowShouldClose():
    BeginDrawing()
    if Fps.enabled:
        DrawFPS(Screen.width - 75, 0)
    if IsKeyDown(KEY_LEFT) and IsKeyDown(KEY_RIGHT):
        player.draw_idle()
    elif IsKeyDown(KEY_LEFT):
        player.pos.x -= 1
        player.draw()
        player.sprite.flipped = True
    elif IsKeyDown(KEY_RIGHT):
        player.pos.x += 1
        player.draw()
        player.sprite.flipped = False
    else:
        player.draw_idle()
    ClearBackground(RAYWHITE)
    EndDrawing()

CloseWindow()
