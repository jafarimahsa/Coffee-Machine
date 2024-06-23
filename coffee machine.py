MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50 ,
            "coffee" : 18 ,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200 ,
            "milk" : 150 ,
            "coffee" : 24 ,
        },
        "cost" : 2.5,
    },
    "cuppuccino" : {
        "ingredients" : {
            "water" : 250 ,
            "milk" : 100 ,
            "coffee" : 24 ,
        },
        "cost" : 3.0,
    }
}

RESOURCES = {
    "water" : 300 ,
    "milk" : 200 ,
    "coffee" : 100 ,
}

def coin():
        print("please insert coins.")
        total = float(input("How many quarters?: "))*0.25
        total += float(input("How many dimes?: "))*0.10
        total += float(input("How many nickles?: "))*0.05
        total += float(input("How many pennies?: "))*0.01
        total = round(total , 2)
        print(f"here is ${total} in change.")
        return total
def espresso():
     if RESOURCES["water"] < MENU["espresso"]["ingredients"]["water"] :
          print("sorry , there is not enough water.")
     elif RESOURCES["coffee"] < MENU["espresso"]["ingredients"]["coffee"] :
          print("sorry , there is not enough coffee.")
     else :
          print("here is your espresso , enjoy!")
          RESOURCES["water"] -= MENU["espresso"]["ingredients"]["water"] 
          RESOURCES["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

def latte() :
     if RESOURCES["water"] < MENU["latte"]["ingredients"]["water"] :
          print("sorry , there is not enough water.")
     elif RESOURCES["coffee"] < MENU["latte"]["ingredients"]["coffee"] :
          print("sorry , there is not enough coffee.")
     elif RESOURCES["milk"] < MENU["latte"]["ingredients"]["milk"] : 
          print("sorry , there is not enough milk.")
     else : 
          print("here is your latte , enjoy!")
          RESOURCES["water"] -= MENU["latte"]["ingredients"]["water"] 
          RESOURCES["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
          RESOURCES["milk"] -= MENU["latte"]["ingredients"]["milk"]

def cuppuccino() :
     if RESOURCES["water"] < MENU["cuppuccino"]["ingredients"]["water"] :
          print("sorry , there is not enough water.")
     elif RESOURCES["coffee"] < MENU["cuppuccino"]["ingredients"]["coffee"] :
          print("sorry , there is not enough coffee.")
     elif RESOURCES["milk"] < MENU["cuppuccino"]["ingredients"]["milk"] : 
          print("sorry , there is not enough milk.")
     else : 
          print("here is your cuppuccino , enjoy!")
          RESOURCES["water"] -= MENU["cuppuccino"]["ingredients"]["water"] 
          RESOURCES["coffee"] -= MENU["cuppuccino"]["ingredients"]["coffee"]
          RESOURCES["milk"] -= MENU["cuppuccino"]["ingredients"]["milk"]
money = 0
ON_OFF = True
while ON_OFF :
    #money = 0
    flavor = input("what would you like ? (espresso,latte,cuppuccino) : ").lower()
    if flavor == "report" :
        print(f'water : {RESOURCES["water"]}ml')
        print(f'milk : {RESOURCES["milk"]}ml')
        print(f'coffee : {RESOURCES["coffee"]}g')
        print(f'money : ${money}')
    elif flavor == "espresso" :
         final_coin = coin()
         if final_coin < MENU["espresso"]["cost"] :
              print("sorry , there is not enough money . money refunded.")
         else :
            espresso()
            money+=MENU["espresso"]["cost"]
    elif flavor == "latte" :
         final_coin = coin()
         if final_coin < MENU["latte"]["cost"] :
              print("sorry , there is not enough money . money refunded.")
         else :
            latte()
            money+=MENU["latte"]["cost"]
    elif flavor == "cuppuccino" :
         final_coin = coin()
         if final_coin < MENU["cuppuccino"]["cost"] :
              print("sorry , there is not enough money . money refunded.")
         else :
            cuppuccino()
            money+=MENU["cuppuccino"]["cost"]
    elif flavor == "off":
         ON_OFF = False     

    

    