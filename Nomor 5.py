def main():
    try:
        with open("input.txt", "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            total_sum = sum(numbers)
            formatted_sum = "{:,.3f}".format(total_sum)
            print("Sum of the numbers:", formatted_sum)
    except FileNotFoundError:
        print("File 'input.txt' not found.")
    except ValueError:
        print("Could not convert data to an integer.")

if __name__ == "__main__":
    main()