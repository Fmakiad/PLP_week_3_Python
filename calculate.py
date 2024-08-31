def cal_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

#Get user input
original_price = float(input("Enter the original price of the item zmk: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = cal_discount(original_price, discount_percentage)

if final_price == original_price:
    print(f"No discount applied. The final price is: zmk{final_price:.2f}")
else:
    print(f"The final price after applying the discount is: zmk{final_price:.2f}")