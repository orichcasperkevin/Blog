class ChangeResetContext:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print(f"Changing value to {self.value}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Resetting value to original")

# Usage
original_value = 10
with ChangeResetContext(original_value) as context:
    # Code inside this block can use the changed value
    context.value = 20
    print(f"Current value: {context.value}")

