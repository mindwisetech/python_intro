def main():
    filename = "user_text.txt"

    try:
        # Write user input to file
        user_input = input("Enter a sentence to save to file: ")
        with open(filename, "w") as f:
            f.write(user_input + "\n")

        # Read and print file content
        print("\nReading from file...")
        with open(filename, "r") as f:
            content = f.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("The file could not be found.")
    except IOError:
        print("An I/O error occurred while working with the file.")

if __name__ == "__main__":
    main()
