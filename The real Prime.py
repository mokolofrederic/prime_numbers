
ValidInput=False
while ValidInput==False:
    try:
        a = int(input("Enter a number between 1-10"))
        for num in range(1,101):
            if all(num%a!=0 for a in range(2,num)):
                print(num)
                ValidInput=True
                print("It is a prime!")
        else:
            print("number not in range")
    except ValueError:
        print("Error, numerical value not used")
       





















