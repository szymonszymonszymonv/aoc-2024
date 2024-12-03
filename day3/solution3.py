import re

corrupted_memory = ''
with open('day3/input3.txt') as f:
  corrupted_memory = f.read()

regex_instructions = r'mul\(\d+\,\d+\)'
regex_extract_numbers = r'[mul\(\)]'
instructions = [re.sub(regex_extract_numbers, '', instruction) for instruction in re.findall(regex_instructions, corrupted_memory)] 
sum = 0

for instruction in instructions:
  a, b = str.split(instruction, ',')
  sum += int(a) * int(b)
  
print(sum)

##### GOLD STAR

dos_and_donts = r"(don't\(\))([\s\S]*?)(do\(\))"
corrupted_memory = re.sub(dos_and_donts, '', corrupted_memory)
instructions = [re.sub(regex_extract_numbers, '', instruction) for instruction in re.findall(regex_instructions, corrupted_memory)] 
sum = 0

for instruction in instructions:
  a, b = str.split(instruction, ',')
  sum += int(a) * int(b)

print(sum)