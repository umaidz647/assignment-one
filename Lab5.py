##Umaid Mohammed 100863405 ### Lab5.py

def CheckEvenOdd(mylist):
    even = []
    odd = []
    for num in mylist:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

def CalculateAverage(mylist):
    even_list, odd_list = CheckEvenOdd(mylist)
    avgeven = 0
    avgodd = 0

    if even_list:
        avgeven = sum(even_list) / len(even_list)

    if odd_list:
        avgodd = sum(odd_list) / len(odd_list)

    return avgeven, avgodd

def PrintResults(avgeven, avgodd):
    print("The average of all even numbers is", avgeven)
    print("The average of all odd numbers is", avgodd)

def CalculatePow(mylist):
    for i in range(len(mylist)):
        mylist[i] = pow(mylist[i], i)
    return mylist

while True:
    mylist = []
    while True:
        number = int(input("Enter a number (or -1 to stop): "))
        if number == -1:
            break
        mylist.append(number)

    avgeven, avgodd = CalculateAverage(mylist)
    PrintResults(avgeven, avgodd)
    print(CalculatePow(mylist))

    again = input("Would you like to try again? (yes/no): ")
    if again.lower() != 'yes':
        break
