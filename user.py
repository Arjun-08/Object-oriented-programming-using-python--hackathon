def Request():
    blood_request = open("blood_request.txt","w")
    blood_type_required = input("blood_type_requried:")   
    name = input("Enter your Name:")
    hospital = input("Enter the name of Hospital:")
    contact_number = input("Enter the Contact Number:")

    blood_request.write(blood_type_required+","+name+","+hospital+","+contact_number+"\n")
    blood_request.close()

while(1):
    print("1.Request in case Emergency")
    print("2.Exit this Application")
    i = (int)(input("Please enter Your choice:"))
    if i == 1:
        Request()
    elif i == 2:
        import sys
        sys.exit()
    else:
        print("Invalid selection!")
