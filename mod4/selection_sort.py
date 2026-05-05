#selection_sort
# pop - removes value at specific index
#remove - removes specific value 
#n: minimum value
#i: iterator for our inner loop

nums = [2,4,3,45,6,7,1,5]

def selection_sort(input):
    ordered = []
    length = len(input)
    for j in range(length):
        n = input[0]
        for i in input:
            if i < n:
                n = i 
        ordered.append(n)
        input.remove(n)
        print(ordered)    
    return(ordered)


print(selection_sort(nums))
            


