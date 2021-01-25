#import modules
import random

#defining the input list
input_list = ["narcissist", "selfobsessed", "inferiority", "ideals", "king", "fake", "Crumble"]

bucket_1 = [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(7):
    print(input_list[i], end="")
    left_letters = 27 - len(input_list[i])
    for j in range(left_letters):
        print(chr(random.randrange(97, 97 + 26)), end="")
    print(" ")
    
