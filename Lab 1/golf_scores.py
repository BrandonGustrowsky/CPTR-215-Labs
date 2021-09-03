def main():
    scores = ["Eagle", "Birdie", "Par", "Bogey"]

    par = int(input())
    num_swings = int(input())

    if par < 3 or par > 5:
        print("Error")
    else:
        answer = num_swings - par
        print(scores[answer + 2])

if __name__ == "__main__":
    main()