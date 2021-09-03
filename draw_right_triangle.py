character = input("Enter a character:\n")
height = int(input("Enter triangle height:\n"))

for i in range(height+1):
    j = 0
    for j in range(i):
        print(f"{character} ", end="")
    
        j += 1
    print()
    i += 1