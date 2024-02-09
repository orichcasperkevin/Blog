def two_loops():
    for i in range(1,4):
        print(f"Outer loop: i = {i}")
        for j in range(1,4):
            print(f"inner loop: j = {j}")
            if i == 2 and j==2:
                return

if __name__ == "__main__":
    two_loops()