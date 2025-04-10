user_data = []

def get_user_data(first_name, last_name, email):
    return first_name, last_name, email


def main():
    first_name :str = input("Enter your first name: ")
    last_name :str = input("Enter your last name: ")
    email : str = input ("Enter your email: ")
    user_data = get_user_data(first_name, last_name, email)
    print(user_data)

if __name__ == "__main__":
    main()