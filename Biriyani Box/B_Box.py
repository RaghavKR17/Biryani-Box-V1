import datetime 
import time
import os 
stock = {1:0,
2:0,
3:0,
4:0,
5:0,
6:0}
def admin():    
    def restock_program():
      restock = input("Do you want to restock any items? (y/n)? ")
      if restock == "y":
          itemrest = int(input("Which item do you want to restock? (1-6)? "))
          stock[itemrest] = 100
          print("COMPLETED")
          restock_program()
      if restock == "n":
        print("Ok... Exiting Program...")    
        exit()  
      else:
        print("Please print either y or n?") 
        restock() 
    for i in range(5):
      restock1 = input("Do you want to restock any more items? (y/n)? ")
      happy = happy + i
      if restock1 == "y":
        itemrest1 = int(input("Which item do you want to restock? (1-6)? "))
        stock[itemrest1] = 100
      else:
        exit()  
    exit()
    restock_program()
q = open("inventory.txt")
for line in q:
        pass
        last_line = line
final_line = last_line.split(",")
for i in range(6):
    stock[i+1] = int(final_line[i+1])
q.close()  
name=input('''What is your name?
''''\n')
if name == "admin123":
    print("Entered Admin Mode.")
    admin()
else:
  print('Hi, %s, Welcome to my South Indian Cuisine.'%(name),'\n')
def main_menu():
  print("             Main Menu")
  print("___________________________________")
  print("1. New Order")
  print("2. Retrieve Order")
  print("3. Cancel Order")
  print("4. Update Order")
  print("5. Exit")
  menu_choice = int(input("Which option do you want? (number) : "))
  if menu_choice == 1:
    neworder()
  if menu_choice == 2:
    retrival()
  if menu_choice == 3:
    cancel_order()  
  if menu_choice == 4:
    update_order()  
  if menu_choice == 5:
    exit()
def neworder():   
  rtrvlist = []   
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
      elif(item == 2):
        print('You have selected, %s,:'%(item), "Vada Box"'\n')
      elif(item == 3):
        print('You have selected, %s,:'%(item), "Idli Box"'\n')
      elif(item == 4):
        print('You have selected, %s,:'%(item), "Samosa Box"'\n')
      elif(item == 5):
        print('You have selected, %s,:'%(item), "Masala Tea"'\n')
      elif(item == 6):
        print('You have selected, %s,:'%(item), "Chicken 65 Box"'\n')
      elif(item > 6):
        print("Please enter number within 1 to 6"'\n')
      elif(item < 1):
        print("Please enter number wihin 1 to 6"'\n')
    except ValueError:
      try:
        item = float(user_input)
        print("You have entered the wrong number."'\n')
      except ValueError:
          print(" Please enter correct number."'\n')       
    quantity =input("How many would you like? : ")
    if(not(quantity.isdigit())):
      print("You have entered the wrong type. Please select menu item again.")
    elif(int(quantity) > stock.get(item)):
        print("Please enter a lesser quantity!"'\n')
    rtrvlist.append(str(str(quantity) + ":" + str(item)))
    totalprice1 = int(totalprice1) + int(((prices[user_input])*(quantity)))
    totalprice = totalprice + (int(prices[user_input])*int(quantity))  
    print("Total price of all items is ... $", totalprice,'\n')
    user_input1 = str(input(" Do you want to finish your order? Yes or No: "))
    try:
      qty = stock.get(item) - int(quantity)
      if(user_input1 == 'Yes' or user_input1 == 'yes' or user_input1 == 'y' or user_input1 == 'Y'):
        print( "The total cost of all items in this order is, $", totalprice,'\n')
        stock[item] = qty
        j = open("inventory.txt","a")
        now = str(datetime.datetime.now()).replace("-" , "").replace(" " , "").replace(":" , "").replace("." , "")
        now = now[:-4]
        j.write("\n" + str(now) + "," + str(stock[1]) + "," + str(stock[2]) + "," + str(stock[3]) + "," + str(stock[4]) + "," + str(stock[5]) + "," + str(stock[6]))
        j.close()
        t = open("records.txt","a")
        t.write("\n" + name.strip() + "," + str(now) + "," + str(rtrvlist).strip("[]"))
        t.close()
        print("Your barcode is... : " + str(now))
        print("Make sure to copy it and store it!")
        break
      elif(user_input1 == "No" or user_input1 == "no" or user_input1 == "n" or user_input1 == "N"):
        stock[item] = qty
        continue
    except ValueError:
      print("Please type Yes or No.")
  main_menu()    
def retrival():
  w = open("records.txt","r")
  allrecords = w.readlines()
  barcode = input("Barcode: ")
  for i in range(len(allrecords)):
    if barcode in allrecords[i]:
      retrivation = allrecords[i].split(",")
      print("\n\n\n")
      print("Customer Name: " + retrivation[0])
      year = str(retrivation[1])[0] + str(retrivation[1])[1] + str(retrivation[1])[2] + str(retrivation[1])[3]
      month = str(retrivation[1])[4] + str(retrivation[1])[5] 
      day = str(retrivation[1])[6] + str(retrivation[1])[7]
      print("Date and Time: " + month + "-" + day + "-" + year)
      print("Barcode: " + retrivation[1])
      retrivation.remove(retrivation[0])
      retrivation.remove(retrivation[0])
      print("Items:")
      for i in range(len(retrivation)):
        values = str(retrivation[i]).strip("'").strip("\n").split(":")
        quant = values[0]
        itim = int(values[1])
        if(itim == 1):
          itimname = str(" Biriyani Boxes")
        elif(itim == 2):
          itimname = str(" Vada Boxes")
        elif(itim == 3):
          itimname = str(" Idli Boxes")
        elif(itim == 4):
          itimname = str(" Samosa Boxes") 
        elif(itim == 5):
          itimname = str(" Masala Tea")
        elif(itim == 6):
          itimname = str(" Chicken 65 Boxes")
        print(quant + itimname)
        input("Please enter to continue...")  
  w.close()
  main_menu()    
def cancel_order():
  w = open("records.txt","r")
  allrecords = w.readlines()
  w.close()
  barcode = input("Barcode: ")
  can = open("records.txt","w")
  for line in allrecords:
      if barcode not in line:
        can.write(line)
  can.close()
  t = open("inventory.txt","r")
  allrecords = t.readlines()
  t.close()
  can = open("inventory.txt","w")
  for line in allrecords:
      if barcode not in line:
        can.write(line)
  can.close()            
  main_menu()
def update_order():
  barcode = input("Barcode: ")
  print("Starting Update Simulation")
  rtrvlist = []   
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
      elif(item == 2):
        print('You have selected, %s,:'%(item), "Vada Box"'\n')
      elif(item == 3):
        print('You have selected, %s,:'%(item), "Idli Box"'\n')
      elif(item == 4):
        print('You have selected, %s,:'%(item), "Samosa Box"'\n')
      elif(item == 5):
        print('You have selected, %s,:'%(item), "Masala Tea"'\n')
      elif(item == 6):
        print('You have selected, %s,:'%(item), "Chicken 65 Box"'\n')
      elif(item > 6):
        print("Please enter number within 1 to 6"'\n')
      elif(item < 1):
        print("Please enter number wihin 1 to 6"'\n')
    except ValueError:
      try:
        item = float(user_input)
        print("You have entered the wrong number."'\n')
      except ValueError:
          print(" Please enter correct number."'\n')       
    quantity =input("How many would you like? : ")
    if(not(quantity.isdigit())):
      print("You have entered the wrong type. Please select menu item again.")
    elif(int(quantity) > stock.get(item)):
        print("Please enter a lesser quantity!"'\n')
    rtrvlist.append(str(str(quantity) + ":" + str(item)))
    totalprice1 = int(totalprice1) + int(((prices[user_input])*(quantity)))
    totalprice = totalprice + (int(prices[user_input])*int(quantity))  
    print("Total price of all items is ... $", totalprice,'\n')
    user_input1 = str(input(" Do you want to finish your order? Yes or No: "))
    try:
      qty = stock.get(item) - int(quantity)
      if(user_input1 == 'Yes' or user_input1 == 'yes' or user_input1 == 'y' or user_input1 == 'Y'):
        print( "The total cost of all items in this order is, $", totalprice,'\n')
        stock[item] = qty
        y = open("inventory.txt", "r")
        allrecordser = y.readlines()
        y.close()
        recopen = open("records.txt","w")
        for line in allrecordser:
            if barcode not in line:
              recopen.write(line)
        recopen.close()      
      if barcode not in line:
        can.write(line)
        j = open("inventory.txt","a")
        now = str(datetime.datetime.now()).replace("-" , "").replace(" " , "").replace(":" , "").replace("." , "")
        now = now[:-4]
        j.write("\n" + str(now) + str(stock[1]) + "," + str(stock[2]) + "," + str(stock[3]) + "," + str(stock[4]) + "," + str(stock[5]) + "," + str(stock[6]))
        j.close() 
        w = open("records.txt","r")
        allrecords = w.readlines()
        w.close()
        can = open("records.txt","w")
        for line in allrecords:
            if barcode in line:
              line = line.split(",")
              mum = line[0]
              mam = line[1]
              line.clear()
              line.append(mum)
              line.append(mam)
              hapa = str(rtrvlist).strip("[]").split(",")
              for i in range(len(hapa)):
                line.append(hapa[i])
              namer =  line[0].strip("'")
              numer = line[1].strip("'")  
              line.remove(line[0])
              line.remove(line[0])
              can.write(namer + "," + numer + "," + str(line).strip("[]").strip('"').strip('"') + "\n")
            elif barcode not in line:
              can.write(str(line))  
        can.close()      
        break
      elif(user_input1 == "No" or user_input1 == "no" or user_input1 == "n" or user_input1 == "N"):
        stock[item] = qty
        continue
    except ValueError:
      print("Please type Yes or No.")
  main_menu()    
main_menu()      
