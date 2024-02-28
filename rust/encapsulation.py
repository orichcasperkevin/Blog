class Counter:
    def __init__(self):
        self.__count = 0

    # Public method to increment the counter
    def increment(self):
        self.__count += 1

    # Public method to get the current value of the counter
    def get_count(self):
        return self.__count

    # Private method to reset the counter to zero
    def __reset(self):
        self.__count = 0

    # Public method to reset the counter to zero from within the class
    def reset_counter(self):
        self.__reset()

def main():
    # Create a new counter
    counter = Counter()

    # Increment the counter
    counter.increment()
    counter.increment()

    # Access the current count
    print("Current count:", counter.get_count())

    # Reset the counter using the public method
    counter.__reset()  # Note: This will not work due to name mangling

    # Reset the counter using the public method
    counter.reset_counter()

    # Access the count after resetting
    print("Count after reset:", counter.get_count())

if __name__ == "__main__":
    main()
