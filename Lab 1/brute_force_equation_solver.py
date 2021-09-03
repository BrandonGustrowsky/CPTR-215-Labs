def main():
    a = int(input())
    b = int(input())
    c = int(input())

    d = int(input())
    e = int(input())
    f = int(input())

    equals = False

    for i in range(-10, 11):
        for j in range(-10, 11):
            first_equation = a*i + b*j
            if first_equation == c:
                second_equation = d*i + e*j
                if second_equation == f:
                    equals = True
                    print(f"x = {i} , y = {j}")
            
    if equals == False:
        print("There is no solution")

if __name__ == "__main__":
    main()
        
        