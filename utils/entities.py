from raylib.colors import RAYWHITE
from raylib.static import LoadTexture, DrawTextureRec

from .helper import Vector2, Rectangle

ENTITIES = []


class Entity:
    def __init__(self, spritesheet, w_h, count, pos=Vector2(), hitbox=Rectangle()):
        self.spritesheet = LoadTexture(spritesheet)
        self.width = w_h[0]
        self.length = w_h[1]
        self.frames = count
        self.current_frame = 1
        self.pos = pos
        self.hitbox = hitbox
        ENTITIES.append(self)

    def __del__(self):
        ENTITIES.remove(self)
        super().__del__()

    def draw(self):
        DrawTextureRec(self.spritesheet, self.hitbox, self.pos(), RAYWHITE)
        if self.current_frame >= self.frames:
            self.current_frame = 1
        else:
            self.current_frame += 1
