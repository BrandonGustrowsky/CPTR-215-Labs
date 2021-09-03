from typing import Union

coin_types = ["Dollar", "Quarter", "Dime", "Nickel", "Penny"]
coin_amounts = [100, 25, 10, 5, 1]

def breakdown_change(change_amt: int, coin: str, coin_val):
    amount = int(change_amt / coin_val)
    if amount:
    # output = 'No change' if (change_amt == 0) else f'{amount} {coin if amount == 1 else coin.replace("y", "ie") + "s"}'
        output = f"{amount} {coin if amount == 1 else coin.replace('y', 'ie') + 's'}"
        print(output)

    return (change_amt - (amount * coin_val))

amount_change = int(input())

if not (amount_change == 0):
    for i in range(len(coin_types)):
        amount_change = breakdown_change(amount_change, coin_types[i], coin_amounts[i])
else:
    print("No change")




