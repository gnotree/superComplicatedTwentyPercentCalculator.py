# Assignment 13: twentyPcentDiscounter.py
# This program calculates the sale price of an item after applying a 20% discount.
def calculate_discounted_price(original_price: float) -> float:
    discount_rate = 0.20
    discount_amount = original_price * discount_rate
    sale_price = original_price - discount_amount
    return sale_price

# Main function to handle user interaction
def main():
    while True:
        user_input = input("Enter the cost of the item (or 'n' to stop): ")
        if user_input.lower() == 'n':
            print("Exiting the program.")
            break
        try:
            original_price = float(user_input)
            sale_price = calculate_discounted_price(original_price)
            print(f"The sale price after a 20% discount is: ${sale_price:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Run the main function
if __name__ == "__main__":
    main()
