def main():
    user_input = input("Enter numbers separated by commas: ")
    try:
        numbers = [float(num.strip()) for num in user_input.split(',')]
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"Sum: {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
    except ValueError:
        print("Invalid input. Please enter only numbers separated by commas.")
    except ZeroDivisionError:
        print("No numbers entered.")

if __name__ == "__main__":
    main()
