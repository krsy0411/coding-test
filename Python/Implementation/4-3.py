# 입력 - str
input_data = input()
# finding the location from input_data
row = int(input_data[1])
# converting to int from string using uni-code
column = int(ord(input_data[0])) - int(ord('a')) + 1

step_types = [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
count = 0

for step in step_types:
  next_row = row + step[0]
  next_column = column + step[1]
  # plus count if knight can move
  if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
    count += 1

print(count)