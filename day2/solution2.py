safe_count = 0
reports = []
with open('day2/input2.txt') as f:
  for line in f:
    reports.append([int(level) for level in str.split(line)])
    
def bruteforce(report):
  ##### GOLD STAR
  for i in range(0, len(report)):
    smaller_report = []
    if i == len(report) - 1:
      smaller_report = report[:i]
    else:
      smaller_report = report[:i] + report[i + 1:]
      
    safe = test_report(smaller_report)
      
    if safe:
      return True
    
  return False
    
def test_report(report):
  decreasing = False
  increasing = False
  for i in range(0, len(report) - 1):
    diff = abs(report[i + 1] - report[i])
    if diff > 3 or diff == 0:
      return False
    if report[i + 1] < report[i]:
      decreasing = True
    else:
      increasing = True
    if decreasing and increasing:
      return False
  return True

for report in reports:
  safe = test_report(report)

  if safe:
    safe_count += 1
  else:
    safe = bruteforce(report)
    safe_count = safe_count + 1 if safe else safe_count
    

print(safe_count)



