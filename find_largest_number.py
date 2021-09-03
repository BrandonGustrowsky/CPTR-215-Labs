entered_nums = []

number = int(input())

while number >= 0:
    entered_nums.append(number)
    number = int(input())

greatest_val = entered_nums[0]
i = 0
for i in range(len(entered_nums)):
    try:
        if entered_nums[i+1] > entered_nums[i]:
            greatest_val = entered_nums[i+1]
    except IndexError:
        print(greatest_val)
    i += 1