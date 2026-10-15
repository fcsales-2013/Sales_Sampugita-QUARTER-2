# Oh! Fun, Fun, Fun, Fun! It is London


print("Hello, Today we will be getting the sum and difference of 2 different numbers!")

# El Global Variables
while True:
    try:
        numerouno = float(input("Input your first number! This is important....."))
        numerodos = float(input("Ok, Bud. Input ANOTHER number... Last time trust, trust"))
        break
    except ValueError:
        print("Ok dude.. Cat is not a number. Again!")
        continue

# El Local Veriables (sum and difference)

def calc_sum():
    global numerouno, numerodos
    sum = numerouno + numerodos
    print(f"Your sum is: {sum}")
def calc_diff():
    global numerouno, numerodos
    diff = numerouno - numerodos
    print(f"Your difference is: {diff}")


calc_sum()
calc_diff()