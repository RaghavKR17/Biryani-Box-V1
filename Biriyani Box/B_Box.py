import datetime
stock = {1:0,
2:0,
3:0,
4:0,
5:0,
6:0}
rtrvlist = []
q = open("records.txt")
for line in q:
        pass
        last_line = line
liner = last_line.split("/")
liner2 = liner[2]
final_line = liner2.split(",")
for i in range(6):
  stock[i+1] = int(final_line[i])
q.close()  
name=input('''What is your name?
''''\n')
print('Hi, %s, Welcome to my South Indian Cuisine.'%(name),'\n')
if name == "admin123":
  print("Entered Admin Mode.")
  def restock_program():
    restock = input("Do you want to restock any items? (y/n)? ")
    if restock == "y":
        itemrest = int(input("Which item do you want to restock? (1-6)? "))
        stock[itemrest] = 100
    if restock == "n":
      print("Ok... Exiting Program...")    
      exit()  
    else:
      print("Please print either y or n?") 
      restock() 
  for i in range(5):
    restock1 = input("Do you want to restock any more items? (y/n)? ")
    if restock1 == "y":
      itemrest1 = int(input("Which item do you want to restock? (1-6)? "))
      stock[itemrest1] = 100
    else:
      exit()  
  exit()
def neworder():      
  totalprice1 = 0
  prices={'1':10,
  '2':2,
  '3':6,
  '4':3,
  '5':2,
  '6':3}
  quantity = 0
  totalprice = 0
  print("     MENU     ")
  print("______________")
  print("1 Biriyani Box - $10")
  print("2 Vada Box - $2")
  print("3 Idli Box - $6")
  print("4 Samosa Box - $3")
  print("5 Masala Tea - $2")
  print("6 Chicken 65 Box - $3"'\n')
  while True:
      user_input =input("Please Choose Menu Item Number : ")
      try:
        item = int(user_input)
        if(item == 1):
          print('You have selected, %s,:'%(item), 'Biriyani Box''\n')
          itemname = "Biriyani Boxes"
        elif(item == 2):
          print('You have selected, %s,:'%(item), "Vada Box"'\n')
          itemname = "Vada Boxes"
        elif(item == 3):
          print('You have selected, %s,:'%(item), "Idli Box"'\n')
          itemname = "Idli Boxes"
        elif(item == 4):
          print('You have selected, %s,:'%(item), "Samosa Box"'\n')
          itemname = "Samosa Boxes"
        elif(item == 5):
          print('You have selected, %s,:'%(item), "Masala Tea"'\n')
          itemname = "Masala Tea"
        elif(item == 6):
          print('You have selected, %s,:'%(item), "Chicken 65 Box"'\n')
          itemname = "Chicken 65 Box"
        elif(item > 6):
          print("Please enter number within 1 to 6"'\n')
          continue
        elif(item < 1):
          print("Please enter number wihin 1 to 6"'\n')
          continue
      except ValueError:
        try:
          item = float(user_input)
          print("You have entered the wrong number."'\n')
          continue
        except ValueError:
            print(" Please enter correct number."'\n')
            continue        
      quantity =input("How many would you like? : ")
      if(not(quantity.isdigit())):
        print("You have entered the wrong type. Please select menu item again.")
        continue
      elif(int(quantity) > stock.get(item)):
          print("Please enter a lesser quantity!"'\n')
          continue
      rtrvlist.append(str(str(quantity) + " " + str(itemname)))  
      totalprice1 = int(totalprice1) + int(((prices[user_input])*(quantity)))
      totalprice = totalprice + (int(prices[user_input])*int(quantity))
      print("Total price of all items is ... $", totalprice,'\n')
      user_input1 =input(" Do you want to finish your order? Yes or No: ")
      try:
        qty = stock.get(item) - int(quantity)
        if(user_input1 == 'Yes' or user_input1 == 'yes' or user_input1 == 'y' or user_input1 == 'Y'):
          print( "The total cost of all items in this order is, $", totalprice,'\n')
          stock[item] = qty
          j = open("records.txt","a")
          now = datetime.datetime.now()
          j.write(name.strip() + "/" + str(now) + "/" + str(stock[1]) + "," + str(stock[2]) + "," + str(stock[3]) + "," + str(stock[4]) + "," + str(stock[5]) + "," + str(stock[6]) + "\n")
          j.close()
          continuation = input("Do you want to create a new order? (y/n): ")
          if continuation == "y":
            neworder()  
        elif(user_input1 == 'No' or user_input1 == 'no' or user_input1 == 'n' or user_input1 == 'N'):
          stock[item] = qty
          continue
        break
      except ValueError:
        print("Please type Yes or No.")
        continue
neworder()
print(rtrvlist)
#retr = input("Do you want to retrieve your order details? (y/n): ")
#if retr == "y":
 # print("Name : " + name + )