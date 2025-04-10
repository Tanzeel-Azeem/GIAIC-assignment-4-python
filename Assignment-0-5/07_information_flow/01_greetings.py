
def greetings (name: str):
    return(f"Greetings {name}!")




def main():
  name = input("What is your name? ")
  print(greetings(name))
if __name__ == '__main__':
    main()