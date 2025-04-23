import sys

phone_name = sys.argv[1]

if phone_name == "apple":
    print("It is a highly secure phone")
elif phone_name == "Oppo":
    print("It is a good camera phone")
elif phone_name == "Redmi":
    print("It is a good speaker phone")
else:
   print("Please provide a valid phone name")
