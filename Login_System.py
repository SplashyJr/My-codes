# These are things the login system should do

# 1. Register - done
# 2. Login - done
# 3. Rename Account Username
# 4. Delete Account
# 5. See account info - done
# 6. Logout - done


def check_New_or_Old():  # this function starts the code to see whether someone has an account or not
    print("Welcome to my Login System! Do you have an account if so enter Y, if not enter N!")
    account = str(input())  # this gets the input for the account

    def register():  # this function registers a persons account if they do not have one
        if account == "N":
            print("Welcome to my Login System! I see that you are new!\nPlease enter a username, then an email, then a password, then repeat the password.")

            print("Username:")
            username = str(input())

            print("Email:")
            email = str(input())

            print("Password:")
            password = str(input())

            print("Repeat Password:")
            repeat_password = str(input())

            if repeat_password == password:  # this sees if the passwords match or not
                print('Thank you for registering an account with us!')
            else:
                print("Passwords do not match!")

            def accountinfo():  # this function lets you see the account information
                print(
                    "Would you like to see your account information.\nIf so type Y if not type N!")
                acc2 = str(input())

                if acc2 == "Y":
                    print("Username:", username, "\nEmail:",
                          email, "\nPassword:", password)
                if acc2 == "N":
                    print("Ok!")

            accountinfo()

    register()

    def login():  # this function lets you login
        if account == "Y":
            print("Login to your account!")

            print("Username:")
            user_name = str(input())

            print("Password:")
            pass_word = str(input())

            print("Thanks for logging in!")

            def account_info_2():  # this function lets you see the account info for a loginned account
                print(
                    "Would you like to see your account information.\nIf so type Y if not type N!")
                acc = str(input())

                if acc == "Y":
                    print("Username:", user_name, "\nPassword:", pass_word)
                if acc == "N":
                    print("Ok!")

            account_info_2()

    login()


check_New_or_Old()
