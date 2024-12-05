left_rules = {} # left to right
right_rules = {} # right to left
pages_list = []
with open('day5/input5.txt') as f:
  line_number = None
  data = f.readlines()
  for i in range(0, len(data)):
    if data[i] == "\n":
      line_number  = i
      break
    left, right = [int(x) for x in data[i].split('|')]
    if left not in left_rules.keys():
      left_rules[left] = [right]
    else:
      left_rules[left] = [*left_rules[left], right]
    if right not in right_rules.keys():
      right_rules[right] = [left]
    else:
      right_rules[right] = [*right_rules[right], left]
      
  for i in range(line_number + 1, len(data)):
    pages_list.append([int(x) for x in data[i].strip().split(',')])
    
def check_left_right(current, previous, next):
  if current in right_rules.keys() and len(previous) != 0:
    for rule in previous:
      if rule not in right_rules[current]:
        return False
  if current in left_rules.keys() and len(next) != 0:
    for rule in next:
      if rule not in left_rules[current]:
        return False

  return True

##### GOLD STAR
def fix_order(current, pages):
  fixed = [None] * len(pages)
  for i in range(0, len(pages)):
    current = pages[i]
    count = 0
    if current in left_rules.keys():
      for rule in left_rules[current]:
        if rule in pages:
          count += 1
      fixed[len(pages) - 1 - count] =  current
      continue
    if current in right_rules.keys():
      for rule in right_rules[current]:
        if rule in pages:
          count += 1
      fixed[count] = current
    
  return fixed
    
sum = 0
corrected_sum = 0
for pages in pages_list:
  correct = True
  for i in range(0, len(pages)):
    previous = pages[:i]
    next = pages[i + 1:]
    current = pages[i]
    correct = check_left_right(current, previous, next)
    if not correct:
      fixed = fix_order(current, pages)
      corrected_sum += fixed[len(fixed) // 2]
      break
    elif len(next) != 0:
      continue
    sum += pages[len(pages) // 2]
      
print(sum)
print(corrected_sum)
    
    
