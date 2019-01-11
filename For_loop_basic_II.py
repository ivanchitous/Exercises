print('Biggie Size')

def makeItBig (get_list):
    makingItBig = []
    for i in get_list:
       if i >= 0:
           makingItBig = makingItBig + [i]
       else:
           makingItBig = makingItBig + ["big"]
    print(makingItBig)

makeItBig([1,2,3,-4,-5,-6,0,1,3,5,-5,-7,-10,100])

print()

print("Count Positives")

def Count_Positives(get_list):
    positive_num = 0
    for i in (get_list):
        if i > 0:
            positive_num += 1
    last_number = len(get_list) - 1
    get_list[last_number] = positive_num
    print(get_list)
        
        
Count_Positives([1,2,3,-4,-5,-6,0,1,3,5,-5,-7,-10,2,5,8,7,8,9])

print()

print ('SumTotal') 
def sum_all(get_list):
   sum_total = 0
   for i in get_list:
       sum_total += i
   
   print(sum_total)
sum_all([1,2,3,4,5])


print ('Average ')
def get_average(get_list):
   sum_total = 0
   for i in get_list:
       sum_total += i
   
   print(sum_total / len(get_list))
get_average([1,2,3,4])


print ('Length ') 
def get_Length(get_list):
   return len(get_list)
print(get_Length([1,2,3,4]))


print ('Maximum ') 
 
def get_max(get_list):
   if len(get_list)<1:
       return "false"
   max_number = get_list[1]
   for i in get_list:
       if i > max_number:
           max_number = i
   return max_number
print(get_max([-1,-2,-3,-4,-5,-8,-1]))


print ('Minimum ')  
def get_min(get_list):
   if len(get_list)<1:
       return "false"
   min_number = get_list[1]
   for i in get_list:
       if i < min_number:
           min_number = i
   return min_number     
print(get_min([-1,-2,-3,-4,-5,-8,-1]))


print("sumTotal, average, minimum, maximum and length of the array.")

def UltimateAnalyze (get_list):
   get_lenght = len(get_list)
   get_sum = 0
   get_min = get_list[1]
   get_max = get_list[1]
   for i in (get_list):
       for i in get_list:
           get_sum += i
           if i < get_min:
               get_min = i
           if i> get_max:
               get_max = i  
       get_aveg = get_sum/len(get_list)
       return get_sum,get_aveg,get_min,get_max,get_lenght
       
print(UltimateAnalyze([1,2,3,4,5,-1]))



print("ReverseList ")

def ReverseList (get_list):
    print(get_list)
    get_list.reverse()
    return get_list
print(ReverseList([1,2,3,4,5,6]))
