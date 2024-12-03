left_list = []
right_list = []
diff = 0

with open('input1.txt') as f:
  for line in f:
    left_item, right_item = str.split(line)
    left_list.append(int(left_item))
    right_list.append(int(right_item))
    
left_list.sort()
right_list.sort()
  
for (left, right) in zip(left_list, right_list):
  diff += abs(left - right)
  
print(diff)
  
##### GOLD STAR

similarity_score = 0

def convert_to_dict(list):
  d = {}
  for item in list:
    if item not in d:
      d[item] = 1
    else:
      d[item] += 1
  return d
      
left_dict = convert_to_dict(left_list)
right_dict = convert_to_dict(right_list)

for item, appearances in left_dict.items():
  if item not in right_dict:
    continue
  similarity_score += item * right_dict[item]
  
print(similarity_score)
    