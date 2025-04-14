import random

def random_pass():
    print("Welcome to Password Generator")

    charecters = "abcdefghijklmnopqrstuvwyxABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&.,/`~"

    num_of_passsword = int(input("Enter the amount of password you want: "))
    len_of_password = int(input("Enter the Lenght of password you want: "))

    print("==========here's your Password==========")

    for pwd in range (num_of_passsword):
        password = ''
        
        for x in range (len_of_password):
            password += random.choice(charecters)
        print(password)

random_pass()