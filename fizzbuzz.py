for i in range(1, 101):
   #test if number is divisible by 3 & 5
    if i % 3== 0 and i % 5 ==0:
        print("FizzBuzz")
    #Test if number is only divisible by 3
    elif i % 3 == 0:
        print ("Fizz")
    #test if number is only divisble by 5
    elif i % 5 == 0:
        print("Buzz")
    #prints all remaining numbers not meeting criteria above
    else:
        print(i)# add your code here

