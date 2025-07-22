price1=float(input("Enter the price of item 1: "))
quantity1=int(input("Enter the quantity of item 1: "))
price2=float(input("Enter the price of item 2: "))
quantity2=int(input("Enter the quantity of item 2: "))
price3=float(input("Enter the price of item 3: "))
quantity3=int(input("Enter the quantity of item 3: "))

total_price1=price1*quantity1
total_price2=price2*quantity2
total_price3=price3*quantity3

print(f'Item 1: {price1} * {quantity1} = {total_price1}')
print(f'Item 2: {price2} * {quantity2} = {total_price2}')
print(f'Item 3: {price3} * {quantity3} = {total_price3}')

subtotal=total_price1+total_price2+total_price3
print(f'Subtotal: {subtotal}')
tax=round(subtotal*0.085, 2)
print(f'Tax (8.5%): {tax}')
total=subtotal+tax
print(f'Total: {total}')

