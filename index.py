def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
    
    Returns:
        float: The final price after applying the discount if applicable.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Main program
try:
    # Prompt user for inputs
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display the result
    if final_price < original_price:
        print(f"The final price after a {discount_percentage}% discount is: ksh {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ksh {original_price:.2f}")
except ValueError:
    print("Please enter valid numerical inputs for price and discount percentage.")
