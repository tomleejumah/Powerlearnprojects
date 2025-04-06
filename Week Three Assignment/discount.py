def calculate_discount(price, discount_percent):
    if discount_percent <= 19:
        return price
    else:
        return price - (price * discount_percent / 100)


price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")
