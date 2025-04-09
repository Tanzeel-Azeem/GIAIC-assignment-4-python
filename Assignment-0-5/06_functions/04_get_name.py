def my_name(name):
    return name

def main():
    name = input("Enter your name: ")
    user_name = name.upper()
    name = my_name(user_name)
    print(f"Hello {name}! Nice to meet you!")

if __name__ == '__main__':
    main()