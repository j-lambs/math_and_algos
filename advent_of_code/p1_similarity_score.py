
frequency_list = dict()
left_list = []

with open("advent_of_code/p1_input.txt") as f:
  for line in f:
    first_int = int(line[:5])
    second_int = int(line[8:])

    left_list.append(first_int)

    if second_int in frequency_list:
      frequency_list.update({second_int: (frequency_list.get(second_int) + 1)}) # type: ignore
    else:
      frequency_list.update({second_int: 1})

# print(frequency_list)

# get and sum similarity score
similarity_score = 0
for i in left_list:
  # check that i'th elt is in right
  # otherwise, i is not in right list and we can ignore
  if i in frequency_list:
    # then calculate and add to similarity score
    similarity_score += frequency_list.get(i) * i

print(similarity_score)
