import random

print("+++++++++++++++++++++++++++++++++++++++++")
print("     Guess the numeber form 1-100 :D")
print("+++++++++++++++++++++++++++++++++++++++++")

try:
    Correctnumber = random.randint(1,100)
    def enternumber():
        try:
            guess = int(input("Guess the numeber form 1-100: "))
            if guess == Correctnumber:
                print("Congratulation Correct number")
            elif guess > Correctnumber:
                print("it's Too much than Correct number Try Again")
                enternumber()
            elif guess < Correctnumber:
                print("it's less than Correct number Try Again")
                enternumber()

        except ValueError:
            print("Please enter number")
            enternumber()

    enternumber()

except Exception:
    pass

