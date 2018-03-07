# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0]

# Pie List 
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", 
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

  # Show pie selection prompt 
  print("---------------------------------------------------------------------")
  print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
        " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
        " (9) Tamale, (10) Steak ")

  pie_choice = input("Which would you like? ")

  # Add pie to the pie list by finding the matching index and adding one to its value
  pie_purchases[int(pie_choice)-1] = pie_purchases[int(pie_choice)-1] + 1

  print("------------------------------------------------------------------------")

  # Inform the customer of the pie purchase
  print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

  # Provide exit option
  shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete 
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_list)):

  # Gather the count of each pie in the pie list and print them alongside the pies
  print(str(pie_purchases[pie_index]) + " " + str(pie_list[pie_index]))

