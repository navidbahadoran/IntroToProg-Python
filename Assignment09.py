# -------------------------------------------------#
# Title: EmployeeApp
# Dev:   NBahadoran
# Date:  12/08/2018
# Desc: This application manages Customer data
# ChangeLog: (Who, When, What)
#
# -------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Customers,Orders
else:
    raise Exception("This file was not created to be imported")

# -- Data --#
# declare variables and constants
objE = None  # an Customer object
objP=None    # an order object
objF=None    # a DataProcessor object
intId = 0  # an Customer Id
strFirstName = ""  # an Customer's first name
strLastName = ""  # an Customer's last name
strEmail = ""       # an Customer's Email
strInput = ""  # temporary user input
CurrentCustomer=[]       #list of Customers saved when we read the file


# -- Processing --#
# perform tasks

# print menu of options
def PrintCustomerProcessingMenu():
    """print the Menu of Options"""
    print("""
        Menu of Options
            1) Show Current Customer List
            2) Add a new Customer.
            3) Remove an existing Customer.
            4) Save Data to File
            5) Add Order for Customer
            6) Remove Order from the list
            7) Show the list of orders
            8) Exit Program
            """)
# to process new customer
def ProcessNewCustomerData(Id="", FirstName=None, LastName=None,Email=None):
    try:
        # Create Customer object
        objE = Customers.Customer()
        objE.Id = Id
        objE.FirstName = FirstName
        objE.LastName = LastName
        objE.Email=Email
        if Customers.CustomerList.AddCustomer(objE):
            return 1
        else:
            return 0
    except Exception as e:
        print(e)

# to process new order

def ProcessNewOrder(CustomerId=None, OId=None, PId=None, PName=None, PPrice=None):
    try:
        # Create Order object
        objP = Orders.Inventory()
        objP.Id=CustomerId
        objP.OId=OId
        objP.PId=PId
        objP.PName = PName
        objP.PPrice = PPrice
        if Orders.Inventory.AddOrder(objP):
            return 1
        else:
            return 0
    except Exception as e:
        print(e)

#Save data to file
def SaveDataToFile(FileName=None,Ty=None):
    try:
        objF = DataProcessor.File()
        objF.FileName = FileName
        if Ty=="c":
            objF.TextData = Customers.CustomerList.ToString()
            print("Your Customer Data was Saved in CustomerData.txt file")
        elif Ty=="p":
            objF.TextData = Orders.Inventory.ToString()
            print("Your Order was Saved in OrderData.txt file")
        objF.SaveData()
    except Exception as e:
        print(e)

# get data from file
def GetDatafromFile(FileName=None,Ty=None):
    try:
        objF=DataProcessor.File()
        objF.FileName=FileName
        objF.GetData()
        if Ty=="c":
            if objF.TextData:
                objF.TextData.pop(0)
            for item in objF.TextData:
                intId=item.split(",")[0].strip()
                strFirstName=item.split(",")[1].strip()
                strLastName=item.split(",")[2].strip()
                strEmail=item.split(",")[3].strip()
                ProcessNewCustomerData(intId, strFirstName, strLastName, strEmail)
        if Ty=="p":
            if objF.TextData:
                objF.TextData.pop(0)
            for item in objF.TextData:
                CustomerId =item.split(",")[0].strip()
                Oid = item.split(",")[1].strip()
                Pid = item.split(",")[2].strip()
                Pname = item.split(",")[3].strip()
                Pprice = item.split(",")[4].strip()
                ProcessNewOrder(CustomerId, Oid, Pid, Pname, Pprice)
    except Exception as e:
        print(e)

#add customer
def AddCustomer():
    """ Add new Customer"""
    objE = Customers.Customer()
    # Get Customer Id from the User
    while objE.Id == None:
        objE.Id = str(input("Enter a Customer Id:"))
    # Get Customer FirstName from the User
    while objE.FirstName == None:
        objE.FirstName = str(input("Enter a Customer's First Name: ")).title()
    # Get Customer LastName from the User
    while objE.LastName == None:
        objE.LastName = str(input("Enter a Customer's Last Name: ")).title()
    # Get Customer Email from the User
    while objE.Email== None:
        objE.Email = str(input("Enter a Customer's Email: "))
    # Process input
    if ProcessNewCustomerData(objE.Id, objE.FirstName, objE.LastName, objE.Email):
        return 1
    else:
        return 0

# Add order for customer
def AddProduct(CustomerId=None):
    objP=Orders.Inventory()
    while objP.OId ==None:
        objP.OId=input("Please Enter Order's ID:")
    while objP.PId == None:
        objP.PId = input("Please Enter Product's ID:")
    while objP.PName == None:
        objP.PName = input("Please Enter Product's Name:")
    while objP.PPrice == None:
        objP.PPrice = input("Please Enter Product's Price:")
    if ProcessNewOrder(CustomerId,objP.OId,objP.PId,objP.PName,objP.PPrice):
        return 1
    else:
        return 0

#Remove customer
def RemoveCustomer(RemoveId=None):
    objE=Customers.CustomerList()
    objE.RemoveCustomer(RemoveId)

#Remove Order
def RemoveOrder(RemoveOId=None):
    objP=Orders.Inventory()
    objP.RemoveOrder(RemoveOId)






# -- Presentation (I/O) --#
# __main__

# get customer Data from Saved File
GetDatafromFile("CustomerData.txt","c")
CurrentCustomer = Customers.CustomerList.ToString()

# Get order data from file
GetDatafromFile("OrderData.txt","p")




while (True):
    PrintCustomerProcessingMenu()
    choice = input("Please Enter your Option from the above Menu to Perform:")
    if choice == "1":
        print("The Current Data is: ")
        print("------------------------")
        print(Customers.CustomerList())

    elif choice=="2":
        if AddCustomer():
            print("Customer was added")

    elif choice=="3":
        RemoveId=None
        while RemoveId == None:
            RemoveId=input("Please Enter Customer's ID You Would Like to Remove:")
        RemoveCustomer(RemoveId)

    elif choice=="4":
        response = None
        while response not in ("y", "n"):
            response = input("Do You want to Save Your Data?(y/n)")
        if response == "y":
            SaveDataToFile("CustomerData.txt", "c")
            SaveDataToFile("OrderData.txt", "p")
        else:
            print("You will be missed your new data, but previous data still exists in text file.")

    elif choice == "5":
        CustomerId = input("Please Enter Customer's ID You Would Like to add order for:")
        if AddProduct(CustomerId):
            print("Order was added")

    elif choice=="6":
        RemoveOId = None
        while RemoveOId == None:
            RemoveOId = input("Please Enter Order's ID You Would Like to Remove:")
        RemoveOrder(RemoveOId)

    elif choice=="7":
        print("The Current Order is: ")
        print("------------------------")
        print(Orders.Inventory())

    elif choice=="8":
        if CurrentCustomer!=Customers.CustomerList.ToString():
            response = None
            while response not in ("y", "n"):
                response = input("Do You want to Save Your Data before exiting the app?(y/n)")
            if response == "y":
                SaveDataToFile("CustomerData.txt", "c")
                print("Your Data All Saved in the Text File")
                break
            else:
                print("You will be missed all your data, but previous data still exist in text file")
                print("Thanks For Using This Application!")
                break
        else:
            print("Thanks For Using This Application!")
            break
    else:
        print("You Entered a Wrong Option, Please try again.")
        continue


