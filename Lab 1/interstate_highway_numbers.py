def determine_direction(number: int) -> str:
    if number % 2 == 0:
        return "east/west."
    else:
        return "north/south."

def main():
    highway_number = int(input())

    str_highway_number = str(highway_number)

    if highway_number <= 0 or highway_number > 999:
        print(f"{highway_number} is not a valid interstate highway number.")

    else:
        if len(str_highway_number) > 2:
            if int(str_highway_number[1:]) == 0:
                print(f"{highway_number} is not a valid interstate highway number.")
            else:
                print(f"I-{highway_number} is auxiliary, serving I-{str_highway_number[2] if str_highway_number[1] == '0' else str_highway_number[1:]}, going {determine_direction(highway_number)}")

        else:
            print(f"I-{highway_number} is primary, going {determine_direction(highway_number)}")

if __name__ == "__main__":
    main()

