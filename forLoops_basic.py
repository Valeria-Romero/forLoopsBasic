for numbers in range(0,151,1):
    print(numbers)

for selectedNumber in range(5, 1001,1):
    if( selectedNumber % 5 == 0 ):
        print(selectedNumber)

for counting in range(1, 101, 1):
    if(counting % 10 == 0):
        print("Coding Dojo")
    elif(counting % 5 == 0):
        print("Coding")
    else:
        print(counting)


sum = 0
for odds in range(0, 500001, 1):
    if(odds%2==1):
        sum = sum + odds
print(sum)

limit = 2018

while limit>=0:
    print(limit)
    limit = limit -4

lowNum=2
highNum=9
mult=3

for numbers in range (lowNum, highNum+1, 1):
    if numbers%3==0:
        print(numbers)