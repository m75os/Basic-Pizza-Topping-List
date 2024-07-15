prompt = "\nEnter desired pizza topping : "
topping_ques = "Would you like to add toppings to your pizza? (Y/N) : "
cont_prompt = "\nWould you like to add more toppings? (Y/N) : "
clear_ques = "Would you like to clear all toppings from your pizza? (Y/N) : "

cont_crit = ['Yes', 'Y', 'y', 'yes', 'ye', 'yeh', 'Ye', "Yeh", 'Yeah', 'yeah']
avail_toppings = [
     "Anchovies", "Cheese", 'Extra Cheese', 'Bacon', 
     "Tomatoes", "Pepperoni", "Onion", "Mushroom", 
     "Garlic", "Sausage", ]
pizza = []

want_toppings = input(topping_ques) #Asks if user wants toppings

if want_toppings in cont_crit: #User wants toppings
    active = True
else: #User does not want toppings
    print("Your pizza is plain")
    active = False


while active: #Topping questions, continuing
       
    top = input(prompt) #Entering toppings

    if top.title() in avail_toppings: #Available topping
        pizza.append(top.title()) #Adding topping
        print("\nThe toppings on your pizza are :")

        for topping in set(pizza): #Printing the current toppings
            print(f"\t{topping}")            
            
        cont = input(cont_prompt) #Deciding whether to continue
        
        if cont in cont_crit: #Continue
            continue #Start from beginning, more toppings
        else: 
            clear_cont = input(clear_ques) # Clear topppings?

            if clear_cont in cont_crit: #Yes, clear toppings
                pizza = []
                print("\nYour pizza is now plain")
                break
            else: #No, don't clear toppings
                print("Selected toppings :")

                for topping in set(pizza): #Printing the current toppings
                    print(f"\t{topping}")
                    
                break
                
    else: #Topping not available
        print(
            "\nThat topping is not available,\n"
            "available toppings are : \n"
            )
        for avail_topping in sorted(avail_toppings):
            print(f"\t{avail_topping}")
        
        cont = input(cont_prompt)
        if cont in cont_crit:
            continue
        else: 
            clear_cont = input(clear_ques) # Clear topppings?

            if clear_cont in cont_crit: #Yes, clear toppings
                pizza = []
                print("\nYour pizza is now plain")
                break
            else: #No, don't clear toppings
                print("Selected toppings :")

                for topping in set(pizza): #Printing the current toppings
                    print(f"\t{topping}")
                    
                break
        

    
                
