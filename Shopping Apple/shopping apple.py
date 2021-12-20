money = 20
items = {'apple':2, 'banana':3, 'lemon':4}

for item_name in items:
    print('======================')    
    print('You have ' + str(money) + ' in your wallet')
    print('Each ' + item_name + ' cost ' + str(items[item_name]))

    input_count = input('How many ' + item_name + ' do you want: ')

    count = int(input_count)
    total_price = count * items[item_name]

    if money >= total_price:
        money -= total_price
        print('Thank you for Purchasing')
    else:
        print("You don't have enough money")
