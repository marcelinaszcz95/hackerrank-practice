# Problem: https://www.hackerrank.com/challenges/py-set-mutations/submissions/code/381658796
# Score: 10

A_number_of_elements = int(input())
A = set(map(int, input().split())) 

N_of_operations = int(input())

commands = []
sets = []
for _ in range(N_of_operations):
    command, length_of_set = input().split()  # Adjusted for correct extraction
    set_ = set(map(int, input().split()))    # Use A instead of creating a new set
    commands.append(command)
    sets.append(set_)

for n in range(N_of_operations):
    if commands[n] == "intersection_update":
        A.intersection_update(sets[n])
    elif commands[n] == "update":
        A.update(sets[n])
    elif commands[n] == "symmetric_difference_update":
        A.symmetric_difference_update(sets[n])
    elif commands[n] == "difference_update":
        A.difference_update(sets[n])

print(sum(A))
    