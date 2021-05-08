from copy import copy

from raylib.colors import WHITE
from raylib.static import LoadTexture, DrawTextureTiled

from .helper import Vector2, Rectangle

ENTITIES = []


class Entity:
    def __init__(self, spritesheet, width, height, x_frames, y_frames, pos=Vector2(), hitbox=Rectangle()):
        self.spritesheet = LoadTexture(spritesheet.encode())
        self.width = width
        self.height = height
        self.single_frame = Rectangle(x=self.width / x_frames, y=self.height / y_frames, width=self.width / x_frames,
                                      height=self.height / y_frames)
        self.frames_num = x_frames * y_frames
        self.current_frame = copy(self.single_frame)
        self.current_frame_num = 1
        self.pos = Rectangle(width=pos.x, height=pos.y)
        self.hitbox = hitbox

    def drawIdle(self):
        DrawTextureTiled(self.spritesheet, self.single_frame(), self.hitbox(), self.pos(), 0, 1, WHITE)

    def draw(self):
        DrawTextureTiled(self.spritesheet, self.current_frame(), self.pos(), Vector2(self.pos.x, self.pos.y)(), 0, 1, WHITE)
        if self.current_frame_num >= self.frames_num:
            self.current_frame_num = 1
        else:
            self.current_frame_num += 1
