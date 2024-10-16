priceData = {
    'biscuit': 3,
    'chicken': 5,
    'egg': 1,
    'fish': 3,
    'coke': 2,
    'bread': 2,
    'apple': 3,
    'onion': 3
}

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = str.lower(input("Press A to add product and Q to quit: "))
        if details == "a":
            product = str.lower(input("Enter product: "))
            if product in priceData.keys():
                quantity = int(input("Enter quantity: "))
                buyingData.update({product: quantity})
            else:
                print("Sorry, that product is not available.")
        elif details == "q":
            enterDetails = False
        else:
            print("Please select a correct option")
    return buyingData


def getPrice(product, quantity):
    subtotal = priceData[product] * quantity
    print(product + ':$' +
          str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal


def getDiscount(billAmount, membership):
    discount = 0
    if membership == 'Gold':
       discount = 20
       print(str(discount) + "% off for " + membership + " " + "membership on  total amount: $" + str(billAmount))
       billAmount = billAmount * 0.80
       print("The discounted amount is $" + str(billAmount))
    elif membership == 'Silver':
       discount = 10
       print(str(discount) + "% off for " + membership + " " + "membership on  total amount: $" + str(billAmount))
       billAmount = billAmount*0.90
       print("The discounted amount is $" + str(billAmount))
    elif membership == 'Bronze':
       discount = 5
       print(str(discount) + "% off for " + membership + " " + "membership on  total amount: $" + str(billAmount))
       billAmount = billAmount*0.95
       print("The discounted amount is $" + str(billAmount))
    else:
        print("The amount is $" + str(billAmount))
    return billAmount


def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    if billAmount >= 25:
        billAmount = getDiscount(billAmount, membership)
    else:
        print("No discount on amount less than $25")
        print("The amount is $" + str(billAmount))

buyingData = enterProducts()
membership = input("Enter customer membership: ")
makeBill(buyingData, membership)