from copy import copy

from raylib.colors import WHITE
from raylib.static import DrawTexturePro

from .helper import Vector2, Rectangle

ENTITIES = []


class Entity:
    def __init__(self, sprite, pos=Vector2()):
        self.sprite = sprite
        self.pos = pos
        self.frame_pos = pos

    def draw_idle(self, angle=0):
        ox = (0 % self.sprite.frames_wide) * self.sprite.frame_size.x
        oy = int(0 / self.sprite.frames_wide) * self.sprite.frame_size.y
        DrawTexturePro(self.sprite.texture,
                       Rectangle(ox,
                                 oy,
                                 self.sprite.frame_size.x,
                                 self.sprite.frame_size.y
                                 )(),
                       Rectangle(self.pos.x,
                                 self.pos.y,
                                 self.sprite.frame_size.x * self.sprite.scale,
                                 self.sprite.frame_size.y * self.sprite.scale
                                 )(),
                       Vector2(self.sprite.origin.x * self.sprite.scale,
                               self.sprite.origin.y * self.sprite.scale
                               )(),
                       angle,
                       WHITE
                       )
        if self.sprite.frame != 1:
            self.sprite.frame = 1

    def draw(self, angle=0):
        ox = (self.sprite.frame % self.sprite.frames_wide) * self.sprite.frame_size.x
        oy = int(self.sprite.frame / self.sprite.frames_wide) * self.sprite.frame_size.y
        if self.sprite.flipped:
            pass
        else:
            pass
        DrawTexturePro(self.sprite.texture,
                       Rectangle(ox,
                                 oy,
                                 self.sprite.frame_size.x,
                                 self.sprite.frame_size.y
                                 )(),
                       Rectangle(self.frame_pos.x,
                                 self.frame_pos.y,
                                 self.sprite.frame_size.x * self.sprite.scale,
                                 self.sprite.frame_size.y * self.sprite.scale
                                 )(),
                       Vector2(self.sprite.origin.x * self.sprite.scale,
                               self.sprite.origin.y * self.sprite.scale
                               )(),
                       angle,
                       WHITE
                       )
        self.sprite.next_frame()
