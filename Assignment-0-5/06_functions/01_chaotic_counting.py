import random

STOPING_NUMBER = 0.2

def choatic_counting ():
    for i in range (10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)
    

def done ():
   if random.random() < STOPING_NUMBER:
       return True
   return False


def main():
    print("\nI'm starting counting")
    choatic_counting()
    print("I finished counting\n")

if __name__ == "__main__":
    main()