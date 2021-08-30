import details

while (1):
    print("____ Hello! Welcome to our Blood Company 'XYZ'____")
    print("____--********--____     1.List of Donors         ____--********--____")
    print("____--********--____  2.Add Hospitals to the List ____--********--____")
    print("____--********--____   3.View Hospital List       ____--********--____")
    print("____--********--____       4.List of users        ____--********--____")
    print("____--********--____     5.Notifications          ____--********--____")
    print("____--********--____   6.Quit this Application    ____--********--____")
    i = (int)(input("Enter Your choice:"))
    if i == 1:
        print("1.Add a Donor")
        print("2.View Donors list")
        print("3.View Donors with rare blood groups")
        j = (int)(input("Your choice:"))
        if j == 1:
            details.Add_donor()
        elif j == 2:
            print("1.View all Donors")
            print("2.View Donors with a specific blood group")
            k = (int)(input("Your choice:"))
            if k == 1:
                details.view_donor()
            if k == 2:
                details.Donor_with_blood()
            else:
                print("Invalid selection")
        elif j == 3:
            print("Donors of blood groups  (AB+ , AB- , B-) are displayed below:")
            details.view_donor_rare_blood()
        else:
            print("Invalid selection-2")
    elif i == 2:
        details.Add_hospital()
    elif i == 3:
        details.View_hospital()
    elif i == 4:
        details.view_users()
    elif i == 5:
        check = details.Emergency_check()
        if check != None:
            print("Emergency!\n There is a Blood Request")
            print("Patient's details:")
            print("Requied blood group:",check[0])
            print("Patient's Name:",check[1])
            print("Contact Number:",check[2])
            print("Hospital Name:",check[3])
            print("Donors are notified below:")
            details.Donor_with_blood_help(check[0])
            print("Notifying Hosipitals and Blood banks:\n press '1' if not required, or press any key")
            a = (int)(input("Your choice:"))
            if a != 1:
                print("Hospitals and Blood banks in the below are Notified")
                details.View_hospital()
            file = open("patients.txt",'a')
            file.write(f"\n{check[0]},{check[1]},{check[2]},{check[3]}")
            file.close()
            print("Patient details were added succesfully.")
        else:
            print("There are no Notifications or blood requests till now")
    elif i == 6:
          import sys
          sys.exit() 
    else:
        print("Invalid selection1")






