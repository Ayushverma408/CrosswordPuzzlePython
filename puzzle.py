#import modules
import random

#defining the input list
input_list = ["n a r c i s s i s t ", "s e l f o b s e s s e d ", "i n f e r i o r i t y ", "i d e a l s ", "k i n g ", "f a k e ", "c r u m b l e "]

bucket_1 = [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]


for i in range(7):
    count = 0;
    for k in range(random.randrange(1,15)):
        print(chr(random.randrange(97, 97 + 26)), end=" ")
        count = count + 1
    print(input_list[i], end="")
    left_letters = 25 - (count) - len(input_list[i].replace(" ",""))
    for j in range(left_letters):
        print(chr(random.randrange(97, 97 + 26)), end=" ")
    print(" ")