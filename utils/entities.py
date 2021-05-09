from copy import copy

from raylib.colors import WHITE
from raylib.static import LoadTexture, DrawTextureRec

from .helper import Vector2, Rectangle

ENTITIES = []


class Entity:
    def __init__(self, spritesheet, w_frame, h_frame, count, pos=Vector2(), hitbox=Rectangle()):
        self.spritesheet = LoadTexture(spritesheet.encode())
        self.single_frame = Rectangle(width=w_frame, height=h_frame)
        self.frames_num = count
        self.current_frame = copy(self.single_frame)
        self.current_frame_num = 1
        self.pos = pos
        self.hitbox = hitbox
        self._frame_pos = pos

    def drawIdle(self):
        DrawTextureRec(self.spritesheet, self.single_frame(), self.pos(), WHITE)

    def draw(self):
        if self.current_frame_num >= self.frames_num:
            self.current_frame_num = 1
            self.current_frame = copy(self.single_frame)
            self._frame_pos.x = self.pos.x
        else:
            self.current_frame_num += 1
            self.current_frame += self.single_frame
            self._frame_pos.x -= self.pos.x
        print(self._frame_pos)
        DrawTextureRec(self.spritesheet, self.current_frame(), self._frame_pos(),
                       WHITE)
