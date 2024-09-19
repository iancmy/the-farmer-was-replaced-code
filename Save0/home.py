from __builtins__ import *

while get_pos_x() > 0:
  move(West)

while get_pos_y() < get_world_size() - 1:
  move(North)

