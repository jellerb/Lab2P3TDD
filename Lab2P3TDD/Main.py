from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")

    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break
#ask user how many times this order shall be placed
order = Invoice().inputNumber("How many times would you like to order this? : ")

total_amount = Invoice().totalPurePrice(products)

#calculate final price after calculating total orders
total_amount_order = Invoice().orderNumberPrice(products, order)


print("Your total pure price is for one order: ", total_amount)
print("After ", order, "orders, your final price is : ", total_amount_order)