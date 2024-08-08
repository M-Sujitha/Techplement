import os
import csv
import datetime

def title():
  line_1 = "-------------------------------"
  title = "Contacts Management System"
  line_2 = "-------------------------------"
  
  print(line_1.center(130))
  print(title.center(130))
  print(line_2.center(130))
class contact_functions:
  contact_fields = ["Name","Mobile_No"]
  contact_database = "contacts.csv"
  contact_data = []

  def create(self):
    os.system('cls')
    title()
    print("       Create Contact: ")
    print("       ---------------")
    print("")

    for fields in self.contact_fields:
      contact_details = input("   Enter "+ fields + ":")
      print("")
      self.contact_data.append(contact_details)
    
    Date = datetime.datetime.today()
    d = Date.strftime("%B %d %Y")
    self.contact_data.append(d)

    with open(self.contact_database, 'a') as file:
      write = csv.writer(file)
      write.writerows([self.contact_data])

    self.contact_data = []
    print("")
    print("Contact created successfully".center(129))
    print("\n")

  def view(self):
    os.system('cls')
    title()

    print("Contacts: ".center(10))
    print("-----------".center(10))
    print("")

    count = 0

    with open(self.contact_database, 'r') as file:
      read = csv.reader(file)
      for data1 in read:
       if len(data1) > 0:
         count += 1
      print("Total contacts: ", count)
      print(' ')

    with open(self.contact_database, 'r') as file:
      read = csv.reader(file)
      if os.path.getsize(self.contact_database) == 0:
        print("Contact Book is empty, Please create contacts".center(129))
      else:
        for fields in self.contact_fields:
          print('{0:<10}'.format(fields).center(10), end = "\t\t")
        print('{0:<10}'.format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format('------','--------------','------'))  
        print(" ")

        for data in read:
          for item in data:
            print('{:<10}'.format(item).center(10), end = "\t\t")
          print(" ")
    print("\n")
    input("\t Press enter key to continue...")
    os.system('cls')

  def search(self):
    os.system('cls')
    title()

    print("Search Contacts: ".center(10))
    print("-----------------".center(10))
    print("")

    self.contact_match = 'false'
    search_value = input("Enter your Name: ")

    for fields in self.contact_fields:
          print('{0:<10}'.format(fields).center(10), end = "\t\t")
    print('{0:<10}'.format("Date"))
    print('{:<10}\t\t{:<10}\t\t{:<10}'.format('------','--------------','------'))  
    print(" ")

    with open(self.contact_database, 'r') as file:
      read = csv.reader(file)
      for data in read:
        if len(data) > 0:
          if search_value == data[0]:
            self.contact_match = 'true'
            print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))
    if self.contact_match == 'false':
      print("")
      print("Sorry!, there is no contacts by this name".center(129))
    print("")
  
  def delete(self):
    os.system('cls')
    title()

    print("Delete Contacts: ".center(10))
    print("-----------------".center(10))
    print("")

    self.contact_match = 'false'
    delete_value = input("Enter your Name: ")
    update_list = []

    with open(self.contact_database, 'r') as file:
      read = csv.reader(file)
      for data in read:
        if len(data) > 0:
          if delete_value != data[0]:
            update_list.append(data)
          else:
            self.contact_match = 'true'
            
    if self.contact_match == 'true':
      with open(self.contact_database, 'w') as file:
        write = csv.writer(file)
        write.writerows(update_list)
        print("")
        print("Contact is deleted successfully!".center(129))
        print("")

    if self.contact_match == 'false':
      print("")
      print("Sorry! data not found")
      print("")


contact_class = contact_functions()
os.system("cls")
title()

while True:
  print("1.View Contacts".center(128))
  print("2.Create Contacts".center(129))
  print("3.Search Contacts".center(129))
  print("4.Delete Contacts".center(129))
  print("5.Exit".center(120))
  print("------------------------".center(131))
  option = int(input("\t\t\t\t\t\tChoose your option: "))

  if option == 1:
    contact_class.view()
    title()

  if option == 2:
    while True:
      contact_class.create()
      ans = input("\t\t\t\tDo you want to create another number?[Y/N]: ")

      if ans == 'Y' or ans == 'y':
        continue
      else: break
    os.system('cls')
    title()

  if option == 3:
    while True:
      contact_class.search()
      print("")
      ans = input("\t\t\t\t\tDo you want to Search another contact number?[Y/N]")
      if ans == 'Y' or ans == 'y':
        continue
      else: break
    os.system('cls')
    title()

  if option == 4:
    while True:
      contact_class.delete()
      print("")
      ans = input("\t\t\t\t\tDo you want to Delete another contact number?[Y/N]")
      if ans == 'Y' or ans == 'y':
        continue
      else: break
    os.system('cls')
    title()


  if option == 5:
    break