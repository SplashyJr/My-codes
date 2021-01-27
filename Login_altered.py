# These are things the login system does:

# 1. Register and save new account info
# 2. Login and find existing account info
# 3. Rename Account Username
# 4. See account info

# Only uncomment this the first time to create a text file to store account info, otherwise it will erase any saved account text whenever run.
# f5=open("login_save",'w+')
# f5.write("List of accounts")
# f5.write('\n')
# f5.close

print("Welcome to my Login System! Do you have an account if so enter Y, if not enter N!")
st = str(input())
account = st.split()  # this gets the input for the account
acc2 = 'y'

if account[0] == "N" or account[0] == "n":
    while acc2 == 'y' or acc2 == 'Y':
        print("Welcome to my Login System! I see that you are new!\nPlease enter a username,then a password, then repeat the password.")

        print("Username:")
        username = str(input())

        print("Password:")
        password = str(input())

        print("Repeat Password:")
        repeat_password = str(input())

        if repeat_password == password:  # this sees if the passwords match or not
            print('Thank you for registering an account with us!')
        else:
            print("Passwords do not match!")
            while repeat_password != password:
                print("please make sure passwords match")
                repeat_password = str(input())

        print("Username:", username, "\nPassword:", password)
        print("Would you like to change your account information.\nIf so type Y if not type N!")
        app = str(input())
        acc2 = app[0]
        if acc2 == "Y" or acc2 == 'y':
            continue
        else:
            print("Ok!")

    # Stores account info in text file.
    reg = username+password
    f5 = open("login_save", 'a+')
    f5.write(reg)
    f5.write('\n')
    f5.close()


else:
    print("Login to your account!")

    print("Username:")
    username = str(input())

    print("Password:")
    password = str(input())

    # Converts info into a format that is comparable to what is saved in the text file.
    reg = username+password+'\n'

    # Opens text file and grabs text saved on it, turning it into a list.
    f5 = open("login_save", 'r')
    L = f5.readlines()
    f5.close()
    # A loop that searches through the text list and compares it to login info to find if the account exists.
    for x in L:
        if x == reg:
            print("Info found. Thanks for logging in!")
            break
    else:
        print("Info not found, please restart and try again")
