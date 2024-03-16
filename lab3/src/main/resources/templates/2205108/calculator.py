class Calculator:
    def __init__(self):
        self.current_value = 0
        self.memory_value = 0

    def add(self, x):
        self.current_value += x

    def subtract(self, x):
        self.current_value -= x

    def multiply(self, x):
        self.current_value *= x

    def divide(self, x):
        if x != 0:
            self.current_value /= x
        else:
            print("Error: Cannot divide by zero")

    def clear(self):
        self.current_value = 0

    def memory_store(self):
        self.memory_value = self.current_value

    def memory_recall(self):
        self.current_value = self.memory_value

    def memory_clear(self):
        self.memory_value = 0


def main():
    calc = Calculator()

    while True:
        print("\nCurrent value:", calc.current_value)
        print("Memory value:", calc.memory_value)
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Memory Store (M+)")
        print("6. Memory Recall (MR)")
        print("7. Memory Clear (MC)")
        print("8. Clear")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '0':
            break
        elif choice == '1':
            num = float(input("Enter number to add: "))
            calc.add(num)
        elif choice == '2':
            num = float(input("Enter number to subtract: "))
            calc.subtract(num)
        elif choice == '3':
            num = float(input("Enter number to multiply: "))
            calc.multiply(num)
        elif choice == '4':
            num = float(input("Enter number to divide: "))
            calc.divide(num)
        elif choice == '5':
            calc.memory_store()
        elif choice == '6':
            calc.memory_recall()
        elif choice == '7':
            calc.memory_clear()
        elif choice == '8':
            calc.clear()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
