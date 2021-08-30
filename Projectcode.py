import csv
import details

def admin_login():
    users_id = input("Enter User ID:")
    password = input("Enter Password:")
    with open(r"C:\Users\arjun sagar\OneDrive\Desktop\ADMIN LOGIN DETAILS.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == users_id:
                if row[1] == password:
                    print("You have entered correct details! \n Logged in Succesfully")
                    file.close()
                    import Admin
                    return 0
                else:
                    print("Please enter valid details!")
                    file.close()
                    return 1
            else:
                print("Invalid details!")
                file.close()
                return 1

def users_login():
    users_id = input("Enter user ID:")
    password = input("Enter your Password:")
    with open(r"C:\Users\arjun sagar\OneDrive\Desktop\USER LOGIN DETAILS.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == users_id:
                if row[1] == password:
                    print("You have entered correct details! Logged in Succesfully")
                    file.close()
                    import user
                
                    return 0
                else:
                    print("Please enter valid details!")
                    file.close()
                    return 1
        print("Invalid details!")
        file.close()
    
def new_users():
    users_id = input("Enter new User ID:")
    with open(r"C:\Users\arjun sagar\OneDrive\Desktop\USER LOGIN DETAILS.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == users_id:
                print("This user ID already exist, Kindly choose other ID.")
                file.close()
                return new_users()
        file.close()
    password = input("Enter a new password:")
    name_ = details.name()
    contact_ = details.contact()
    blood_ = details.blood()
    f = open(r"C:\Users\arjun sagar\OneDrive\Desktop\USER LOGIN DETAILS.txt",'a')
    f.write(f"\n{users_id},{password},{name_},{contact_},{blood_}")
    f.close()
    print("Congratulations! Your account has been created succesfully!")
    print("Login to continue")

def Login():
    print("1.user login ")
    print("2.Admin Login")
    print("3.Dont have an account? create an account")
    print("4.Exit this application")
    i = (int)(input("Your choice:"))
    if i == 1:
        if (users_login()):
            print("1.Try again")
            print("2.Go to login page")
            j = (int)(input("Please enter your choice:"))
            if j == 1:
                if (users_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid selection!Heading back to lobby")
                Login()
    elif i == 2:
        if (admin_login()):
            print("1.try again")
            print("2.Go to login page")
            j = (int)(input("Please enter your choice:"))
            if j == 1:
                if (admin_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid selection!Heading back to lobby")
                Login()
    elif i == 3:
        new_users()
    elif i == 4:
        import sys
        sys.exit()
    else:
        print("Enter valid choice!")

while(1):
    Login()
        