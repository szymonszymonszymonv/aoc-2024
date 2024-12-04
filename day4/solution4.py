mess = [list(line.strip()) for line in open('day4/input4.txt').readlines()]
adjacents = [[(i, j) for j in range(-1, 2)] for i in range(-1, 2)]
phrase = "XMAS"

def ceres_search(x, y, direction=None, sum=0):
  current = mess[x][y]
  if current == "S": 
    return 1
  seeking = phrase[str.index(phrase, current) + 1]
  if direction != None:
    next_x = x + direction[0]
    next_y = y + direction[1]
    if next_x < 0 or next_y < 0:
      return 0
    try:
      if seeking == mess[next_x][next_y]:
        return ceres_search(next_x, next_y, direction, sum)
    except:
      pass
    return 0
  
  for row in adjacents:
    for col in row:
      next_x = x + col[0]
      next_y = y + col[1]
      if next_x < 0 or next_y < 0:
        continue
      try:
        if seeking == mess[next_x][next_y]:
          sum += ceres_search(next_x, next_y, col, sum)
      except:
        continue
  return sum
  
xmas_count = 0
for i in range(0, len(mess)):
  for j in range(0, len(mess[i])):
    char = mess[i][j]
    if char == 'X':
      xmas_count += ceres_search(i, j)
      
print(xmas_count)

##### GOLD STAR
diagonals = [[-1, -1,], [-1, 1],]

def x_ceres_search(x, y):
  for diagonal in diagonals:
    opposite = [diagonal[0] * -1, diagonal[1] * -1]
    try:
      chars = mess[x + diagonal[0]][y + diagonal[1]] + mess[x + opposite[0]][y + opposite[1]]
      print(chars)
    except:
      return 0
    if "M" in chars and "S" in chars:
      continue
    else:
      return 0
  return 1

mas_count = 0
for i in range(0, len(mess)):
  for j in range(0, len(mess[i])):
    char = mess[i][j]
    if char == 'A':
      mas_count += x_ceres_search(i, j)
print(mas_count)