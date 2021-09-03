def main():
    number = int(input())

    binary = ""
    while number > 0:
        if number % 2 == 0:
            binary += "0"
        else:
            binary += "1"

        number = int(number/2)

    print(binary)

if __name__ == "__main__":
    main()