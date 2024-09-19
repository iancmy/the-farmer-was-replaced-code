from __builtins__ import *
from moves import *

def main():
  while True:
    buy_pumpkin_seed()
    buy_carrot_seed()
    buy_water_tank()
    buy_fertilizer()

    # repeat(25, plant_grass)
    # plant_bush()
    repeat(10, plant_tree)
    # repeat(10, plant_carrot)
    # repeat(30, plant_pumpkin)

    # rmove()
    # harvest()
    # debug()
##
def debug():
  # print(get_world_size())
  print("X:", get_pos_x())
  print("Y:", get_pos_y())
  # print(get_ground_type())
  print("ENTITY:", get_entity_type())
  # print(get_water())
  print(move(West))

##
def repeat(n, func):
    while n > 0:
        func()
        n -= 1

##
def hmove(pos_x, pos_y):
  path = []
  stack = []
  stack.append(source)
    
  while stack:
      s = stack.pop()
      if s not in path:
          path.append(s)

      elif s in path:
          #leaf node
          continue
      for neighbour in graph[s]:
          stack.append(neighbour)
  
  return " ".join(path)

def rmove(paths=[], direction_index=0):
  directions=[North, East, South, West]

  if len(paths) > 3:
    paths.pop(0)

  for direction in directions:
    check_treasure = measure(direction)

    if check_treasure:
      move(direction)
      return paths, direction_index

  # check previous paths first
  for path in paths: 
    if path == directions[direction_index]:
      directions.pop(direction_index)
      if direction_index == 0:
        direction_index = len(directions) - 1
      else:
        direction_index -= 1

  can_move = move(directions[direction_index])
  
  if not can_move:
    if direction_index == len(directions) - 1:
      direction_index = 0
    else:
      direction_index += 1
  else:
    paths.append(directions[direction_index])
  
  return paths, direction_index

##
def plant_grass():
  x_direction = None
  y_direction = None
  for _ in range(get_world_size()):
    for _ in range(get_world_size()):
      if get_ground_type() == Grounds.Soil:
        till()
      if can_harvest():
        harvest()

      x_direction, y_direction = ymove(get_pos_y(), x_direction, y_direction)
        
def plant_bush():
  x_direction = None
  y_direction = None
  paths = []
  direction_index = 0

  for _ in range(get_world_size()):
    for _ in range(get_world_size()):
      water_soil()
      fertilize()

      if get_entity_type() == Entities.Hedge:
        paths, direction_index = rmove(paths, direction_index)
      elif can_harvest() and get_entity_type() == Entities.Treasure:
        harvest()
      else:
        plant(Entities.Bush)
        
      x_direction, y_direction = ymove(get_pos_y(), x_direction, y_direction)

def plant_tree():
  x_direction = None
  y_direction = None

  for _ in range(get_world_size()):
    for _ in range(get_world_size()):
      water_soil()

      if can_harvest():
        harvest()

      if get_pos_x() % 2 == 0:
        if get_pos_y() % 2 == 0:
          plant(Entities.Tree)
        else:
          plant(Entities.Bush)
      else:
        if get_pos_y() % 2 == 0:
          plant(Entities.Bush)
        else:
          plant(Entities.Tree)
        
      x_direction, y_direction = ymove(get_pos_y(), x_direction, y_direction)

def plant_carrot():
  x_direction = None
  y_direction = None

  for _ in range(get_world_size()):
    for _ in range(get_world_size()):
      water_soil()

      if can_harvest():
        harvest()
        plant(Entities.Carrots)
      else:
        plant(Entities.Carrots)

      x_direction, y_direction = ymove(get_pos_y(), x_direction, y_direction)

def plant_pumpkin():
  megapumpkin_index = (get_world_size() * get_world_size() - 1) * -1
  x_direction = None
  y_direction = None

  for _ in range(get_world_size()):
    for _ in range(get_world_size()):
      water_soil()

      if megapumpkin_index == 0:
        harvest()

      if can_harvest() and get_entity_type() != Entities.Pumpkin:
        harvest()
      elif can_harvest() and get_entity_type() == Entities.Pumpkin:
        megapumpkin_index += 1
      else:
        plant(Entities.Pumpkin)

      x_direction, y_direction = ymove(get_pos_y(), x_direction, y_direction)

##
def water_soil():
  water_threshold = 0.5
  if get_ground_type() == Grounds.Soil:
    if get_water() < water_threshold:
      use_item(Items.Water_Tank)
  else: 
    till()
    if get_water() < water_threshold:
      use_item(Items.Water_Tank)

def fertilize():
  if not can_harvest():
    use_item(Items.Fertilizer)
    water_soil()
  elif get_entity_type() == Entities.Bush and can_harvest():
    use_item(Items.Fertilizer)

## 
def buy_rand(max_buy):
  return max_buy * max(random(), 0.5)

def buy_carrot_seed():
  cost = 9 #wood and hay
  total_wood = num_items(Items.Wood)
  total_hay = num_items(Items.Hay)

  max_buy = (total_wood / (cost * cost * cost)) - (total_hay / (cost * cost * cost))
  buy_threshold = max_buy * 0.4

  if num_items(Items.Carrot_Seed) < buy_threshold:
    trade(Items.Carrot_Seed, buy_rand(max_buy))

def buy_pumpkin_seed():
  cost = 6 #carrots
  total_carrot = num_items(Items.Carrot)
  max_buy = total_carrot / (cost * cost * cost)
  buy_threshold = max_buy * 0.4

  if num_items(Items.Pumpkin_Seed) < buy_threshold:
    trade(Items.Pumpkin_Seed, buy_rand(max_buy))

def buy_water_tank():
  cost = 5 #wood
  total_wood = num_items(Items.Wood)
  max_buy = get_world_size() * get_world_size() * 3
  buy_threshold = max_buy * .4

  if num_items(Items.Water_Tank) * cost * 0.25 < buy_threshold:
    trade(Items.Empty_Tank, buy_rand(max_buy))

def buy_fertilizer():
  cost = 10 #pumpkins
  total_pumpkins = num_items(Items.Pumpkin)
  max_buy = total_pumpkins / (cost * 4)
  buy_threshold = max_buy * 0.4

  if num_items(Items.Fertilizer) < buy_threshold:
    trade(Items.Fertilizer, buy_rand(max_buy))


main()