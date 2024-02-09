# Python does not support the use of labels and the goto statement, as it is designed to be a highly structured programming language that encourages clear and readable code through structured control flow constructs like loops, conditional statements, and functions. Instead of using labels and goto, Python emphasizes the use of functions, loops, and conditional statements to achieve program logic in a more structured and readable manner.

# Labels and goto statements can introduce spaghetti code and make it harder to understand and maintain the codebase. Python's design philosophy prioritizes simplicity, readability, and maintainability, which is why such features are intentionally not included in the languag


for i in range(1,4):
    print(f"Outer loop: i = {i}")
    for j in range(1,4):
        print(f"inner loop: j = {j}")
        if i == 2 and j==2:
            break