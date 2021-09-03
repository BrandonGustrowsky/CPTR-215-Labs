def main():
    special_chars = [".", ",", "!"]

    text = input()

    length = 0

    for character in text:
        if character == " ":
            continue
        elif character in special_chars:
            continue
        else:
            length += 1

    print(length)

if __name__ == "__main__":
    main()
