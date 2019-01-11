print("Functions Basic II")
print()
print("Countdown")
def countdown (Num):
    list = []
    for i in range (Num,1,-1):
        list.append(i)
    return(list)
print(countdown(18))

print()

print("Print and Return")

def Print_Return(num1,num2):
    print(num1)
    return(num2)
print(Print_Return(2,3))

print()

print("First Plus Length")
def a_list(mylist):
    first_value = mylist[0]
    lenghtOfList = len(mylist)
    return first_value + lenghtOfList

print(a_list([18, 17, 16, 5, 4, 3, 2]))

print()

print("Values Greater than Second")

def greaterValues(get_list):
    newList = []
    for i in get_list:
        if i > get_list[1]:
            newList = newList + [i]
    if len(newList) > 1:
        print(newList)
        return print("the len is: ",len(newList))
    else:
        return 'false'               
print(greaterValues([2,1,6,8,7,1,3,5,8]))
 
 
print('This Length, That Value')

def lengthAndValue(size,value):
    get_a_list = []      
    for i in range (size):
        get_a_list = get_a_list + [value]
    print(get_a_list)
      
lengthAndValue(4,7)

    
        
    
