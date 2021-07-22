# import math

# def cans_of_paint(height, width, coverage=5):
#     num_of_cans = (height * width) / coverage
#     print(f"You need {int(math.ceil(num_of_cans))} cans of paint.")

# cans_of_paint(3, 9)

def is_it_prime(num):
    prime_list = [1,2,3,5,7]
    if num == 0:
        print("0 is neither a prime nor composite number.")
    elif num in prime_list:
        print(f"{num} is prime.")
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(f"{num} is not prime.")
    else:
        print(f"{num} is prime.")

for num in range(0, 101):
    is_it_prime(num)
