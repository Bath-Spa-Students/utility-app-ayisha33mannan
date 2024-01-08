#printing a welcome sign as a visual
print ("""
 ▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ 
 ▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ 　 ░▒█░░ ▒█░░▒█ 
 ▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ 　 ░▒█░░ ▒█▄▄▄█ 
       

   ██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░    
   ██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░    
   ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░    
   ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗    
   ░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝    
   ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░    

   ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
   ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
   ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
   ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
   ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
   ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝ """)
print(" ")
print("\n NOTE:   BEFORE WE BEGIN, PLEASE ACTIVATE THE CAPS LOCK KEY TO ENHANCE YOUR SHOPPING EXPERIENCE")
print ("\t \t \t \t HAPPY SHOPPING :) \n")

#beginning of codes
#creating a class called 'CREATIVE'
class CREATIVE:

#initializing with 'balance' and 'menu'
    def __init__(show): 
        #items with codes, names, prices, and available stock
        show.menu = [
            {'Item #': 'A1', 'Item': 'lays', 'Price': 6.0, 'Stock': 5},
            {'Item #': 'A2', 'Item': 'doritos', 'Price': 5.0, 'Stock': 7},
            {'Item #': 'A3', 'Item': 'cheetos flamin hot', 'Price': 4.0, 'Stock': 2},
            {'Item #': 'A4', 'Item': 'oman chips', 'Price': 3.0, 'Stock': 5},
            {'Item #': 'B1', 'Item': 'coca cola', 'Price': 5.0, 'Stock': 7},
            {'Item #': 'B2', 'Item': 'pepsi', 'Price': 5.0, 'Stock': 3},
            {'Item #': 'B3', 'Item': 'fanta', 'Price': 5.0, 'Stock': 1},
            {'Item #': 'C1', 'Item': 'water', 'Price': 3.0, 'Stock': 9},
            {'Item #': 'C2', 'Item': 'mango juice', 'Price': 5.0, 'Stock': 5},
            {'Item #': 'C3', 'Item': 'apple juice', 'Price': 5.0, 'Stock': 4},
            {'Item #': 'C4', 'Item': 'banana milkshake', 'Price': 9.0, 'Stock': 0},
            {'Item #': 'D1', 'Item': "hershey's kisses", 'Price': 3.0, 'Stock': 6},
            {'Item #': 'D2', 'Item': "hershey's chocolate", 'Price': 5.0, 'Stock': 5},
            {'Item #': 'D3', 'Item': 'dairy milk chocolate', 'Price': 7.0, 'Stock': 3},
        ]
        show.balance = 0       #the initial balance is ZERO

    #displaying the menu (items, prices and stocks of the item)
    def displaying_menu(show):    
        print("_" * 82)
        print("Item #    |               Item                 |        Price       |    Stock   |")
        print("-" * 82)

    #dividing items in categories (their code numbers)
        divisions = {
            'snacks': ['A1', 'A2', 'A3', 'A4'],
            'Drinks': ['B1', 'B2', 'B3'],
            'Juices': ['C1', 'C2', 'C3', 'C4'],
            'Chocolates': ['D1', 'D2', 'D3']
        } 

    #printing things ordered by division
        for division, items in divisions.items():
            print(f"{' ' * 30} -{division}-")
            print("-" * 82)
            for item in show.menu:
                if item['Item #'] in items:
                    print(f"{item['Item #']:<8} | {item['Item']:<34} | ${item['Price']:<17.2f} |     ({item['Stock']})     |")
            print("-" * 82)
        print("_" * 82)

    #allowing the user to choose an item by their specific code number
    def choose_item(show): 
        while True:
            try:
                #asking user to choose
                choose = input("Please enter the code number of the item you want: ")
                #checking if the item code given by the user exists in the menu
                item = next((item for item in show.menu if item['Item #'] == choose), None)
                if item is None:  #if the item code is invalid
                    print("Invalid input. Please enter a valid Item code number...")
                    continue
                 #if the item is out of stock
                if item['Stock'] == 0: 
                    print("Sorry, this item is out of stock :(")  
                    continue
                return item
            except (ValueError, IndexError): 
                print("Invalid input. Please enter a valid Item #.")

    #payment process after selecting items
    def insert_payment(show, total_price): 
        while True:
            try:
                #asking user to give the amount of the item 
                money = float(input(f"Please enter the amount of money (${total_price}): $"))
                if money >= total_price:
                    #calculations (for change)
                    show.balance += total_price
                    change = money - total_price
                    if change > 0:
                        print(f"Here is your change: ${change:.2f}")
                    return True
                #if the user did not give the specific amount
                else:
                    remaining_money = total_price - money
                    print(f"Remaining amount to be paid: ${remaining_money :.2f}")
                    response = input(f"Do you want to continue by giving the rest of ${remaining_money} or cancel  and end the purchase and get a refund? (continue/cancel): ")
                    #if user does not want to continue 
                    if response.lower() == 'cancel':
                        print(f"Refunding ${money:.2f}...")
                        return False
                     #if user wants to continue
                    elif response.lower() == 'continue':
                        while True:
                            try:
                                #asking for the remaining money
                                additional_payment = float(input(f"Enter the remaining amount of ${remaining_money}: $"))
                                if additional_payment == remaining_money:
                                    show.balance += total_price
                                    print("Payment completed. Thank you!")
                                    return True
                                #calculations (for change)
                                elif additional_payment > remaining_money: 
                                    show.balance += total_price
                                    change = additional_payment - remaining_money
                                    print(f"Here is your change: ${change:.2f}")
                                    return True
                                else:
                                    print("Incorrect amount. Please enter the correct remaining amount.") 
                            except ValueError:
                                print("Invalid input. Please enter a valid amount of money.")
            except ValueError:
                print("Invalid input. Please enter a valid amount of money.")

    #gives the user their selected item
    def dispense_item(show, item):  
        print(f"Here is your {item['Item']}. Enjoy!")

    #calculating discounts based on the user's age
    def calculate_discount(show, age): 
        if age > 50:
            return 0.6, "60% has been applied"  #if age is more than 50, discount is 60%
        elif 36 <= age <= 50:
            return 0.2, "20% has been applied"  #if age is between 36 and 50, discount is 20% 
        elif 18 <= age <= 35:
            return 0.1, "10% has been applied"  #if age is between 18 and 35, discount is 10% 
        elif age < 18:
            return 0.15, "15% has been applied" #if age is under 18, discount is 15%
        else:
            return 0, "No discount applied"     #if non of the obove, no discount

    #executing the operations of vending machine
    def run(show):  
        while True:
            show.displaying_menu() 

            item = show.choose_item()

            print("\nDiscounts:")
            print("-" * 20)
            print("Age > 50: 60%")
            print("Age 36-50: 20%")
            print("Age 18-35: 10%")
            print("Age < 18: 15%")
            print("-" * 20)

            while True:
                try:
                    #asking user for their age
                    user_age = int(input("Enter your age to apply discount: "))
                    break
                except ValueError:
                    print("Please enter a valid age.")
            #calculations (for discount)
            discount, discount_info = show.calculate_discount(user_age)
            if discount != 0:
                print(discount_info)

            discounted_price = item['Price'] * (1 - discount)
            #after vending an item, updating the stock
            if show.insert_payment(discounted_price):
                item['Stock'] -= 1
                show.dispense_item(item)
            #asking whether to continue vending or end it.
            choose = input("Do you want anything else? (yes/no): ")
            if choose.lower() == 'no':
                break
        #providing the total bill for their purchases
        print(f"Thank you for using the Vending Machine. Your total balance: ${show.balance:.2f}")


# Creating an instance of the class and running it
CREATIVEmachine = CREATIVE()
CREATIVEmachine.run()
