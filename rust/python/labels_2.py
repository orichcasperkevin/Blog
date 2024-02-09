condition_met = False

for i in range(1,4):
    print(f"Outer loop: i = {i}")
    for j in range(1,4):
        print(f"inner loop: j = {j}")        
        if i == 2 and j==2:
            condition_met = True
            break
    #break when condition is met
    if condition_met:
        break