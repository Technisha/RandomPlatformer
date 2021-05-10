from copy import copy

from raylib.colors import WHITE
from raylib.static import *

from .helper import Vector2, Rectangle

ENTITIES = []


class Entity:
    def __init__(self, sprite, pos=Vector2()):
        self.sprite = sprite
        self.pos = pos
        self.frame_pos = pos
        ENTITIES.append(self)

    def unsubscribe(self):
        ENTITIES.remove(self)

    def draw_idle(self, angle=0):
        ox = (0 % self.sprite.frames_wide) * self.sprite.frame_size.x
        oy = int(0 / self.sprite.frames_wide) * self.sprite.frame_size.y
        if self.sprite.flipped:
            frame_size_x = -self.sprite.frame_size.x
        else:
            frame_size_x = self.sprite.frame_size.x
        self.hitbox = Rectangle(self.pos.x,
                                self.pos.y,
                                self.sprite.frame_size.x * self.sprite.scale,
                                self.sprite.frame_size.y * self.sprite.scale
                                )()
        DrawTexturePro(self.sprite.texture,
                       Rectangle(ox,
                                 oy,
                                 frame_size_x,
                                 self.sprite.frame_size.y
                                 )(),
                       self.hitbox,
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
            frame_size_x = -self.sprite.frame_size.x
        else:
            frame_size_x = self.sprite.frame_size.x
        self.hitbox = Rectangle(self.frame_pos.x,
                                self.frame_pos.y,
                                self.sprite.frame_size.x * self.sprite.scale,
                                self.sprite.frame_size.y * self.sprite.scale
                                )()
        DrawTexturePro(self.sprite.texture,
                       Rectangle(ox,
                                 oy,
                                 frame_size_x,
                                 self.sprite.frame_size.y
                                 )(),
                       self.hitbox,
                       Vector2(self.sprite.origin.x * self.sprite.scale,
                               self.sprite.origin.y * self.sprite.scale
                               )(),
                       angle,
                       WHITE
                       )
        self.sprite.next_frame()

    def update(self):
        pass


class Player(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        if IsKeyDown(KEY_LEFT) and IsKeyDown(KEY_RIGHT):
            self.draw_idle()
        elif IsKeyDown(KEY_LEFT):
            self.pos.x -= 1
            self.draw()
            self.sprite.flipped = True
        elif IsKeyDown(KEY_RIGHT):
            self.pos.x += 1
            self.draw()
            self.sprite.flipped = False
        else:
            self.draw_idle()
