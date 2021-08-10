list = ["1","4","6","8","5","9"]
x = input("Guess the number")
exist = list.count(x)
while True: 
    if exist == 1:
        x = input("Success! Enter again")
        exist = list.count(x)

  
    elif x == "q":
        break

    try:
        x = int(x)
    except ValueError:
        print("Type number only")
        
        continue
    
    else:
        x = input("Failed! This number is not in this list")
        exist = list.count(x)





