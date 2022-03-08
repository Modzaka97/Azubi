
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-----------Welcome to Ecobank--------------")
print("------To access your account information---")
print("---------type your account number----------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")

ValueX =  0
balance = 0

account_num = int(input("Enter your 6 digit account number\n"))
full_name = str(input("Enter your full name in this format. \nFirstname Lastname\n"))

EcoID = str(account_num) + full_name
accounts =[-6,12,30000,1221,13313001,3133000]
EcoID_user =["101001Samuel Asare", "101002Recheal Blankson", "101003Elikem Bansah", "101004Eugenia Teye", "102001Kwasi Modzaka", "102002Ernestina Tawiah" ]

#Code below find a matching EcoID from user input with an EcoID_user already in database
#it then saves the placeholder value into value X

if EcoID in EcoID_user:
    ValueX = EcoID_user.index(EcoID)
else: print("Invalid response, try again")

balance = accounts[ValueX]

#account type
acc_typ = 0

typ_value = str(account_num)[2]
if int(typ_value) == 1:
    acc_typ = "savings"
elif int(typ_value) == 2:
    acc_typ = "current"
else: print("Invalid response, try again")


print("Hello " + str(full_name) + " your " + str(acc_typ) + " account balance is $" + str(balance))
