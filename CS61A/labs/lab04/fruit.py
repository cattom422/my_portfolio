def buy(fruits_to_buy, prices, total_amount):
    """Print ways to buy some of each fruit so that the sum of prices is amount.

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)  # We can only buy apple, orange, and banana, but not kiwi
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """
    def add(fruits, amount, cart):
        if fruits == [] and amount == 0:
            print(cart)
        elif fruits and amount > 0:#the idea is blocking all inavailable conditions
            fruit = fruits[0]
            price = prices[fruit]
            ith=len(fruits)
            for k in [0,1]:
                # Hint: The display function will help you add fruit to the cart.
                add(fruits[k::],amount-price ,cart[:-ith:]+[cart[-ith]+1]+cart[len(fruits_to_buy)-ith+1::])
    add(fruits_to_buy, total_amount, [0 for i in range(len(fruits_to_buy))])
prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
buy(['apples', 'oranges', 'bananas'], prices, 12)
print()
buy(['apples', 'oranges', 'bananas'], prices, 16)
print()
buy(['apples', 'kiwis'], prices, 36)