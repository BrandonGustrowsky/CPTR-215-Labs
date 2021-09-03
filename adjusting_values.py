def main():
    list_numbers = []

    first_number = int(input())

    greatest = None

    for i in range(first_number):
        number = float(input())
        list_numbers.append(number)

        if greatest == None or number > greatest:
            greatest = number

        i += 1

    for num in list_numbers:
        print(f"{(num/greatest):.2f}")

if __name__ == "__main__":
    main()





