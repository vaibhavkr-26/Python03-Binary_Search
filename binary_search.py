# Binary search will always works on the sorted list because it compare index value to the target

array = [1,2,3,4,5,6,7,8,9]

print(array)

while True:
    try:
        target = int(input("Enter the target from the above list: "))
        break
    except ValueError:
        print("Please select valid number.")


def binary_search(target):
    # Insiating the start and end for get the first and second element
    # count for in how many loops it get for finding the target
    # len(array) - 1 is used because the python list indexing start from 0 and 
    # len() function count from 1
    start, end, count = 0, len(array) - 1, 0
    
    # Run until array finshied or (start > end) which is also mean end
    while start <= end:
        # Finding the exact mid of the array on each loop beacuse
        # we update the mid if the target is in other half side
        mid = (start + end) // 2 

        if array[mid] == target:
            # it will return in tuple format
            return True, count
        
        # If the mid < target then its in the half-left side of the array
        elif array[mid] > target:
            end = mid - 1
            count += 1
        
        # If the mid > target then its in the half-right side of the array
        elif array[mid] < target:
            start = mid + 1
            count += 1
    
    # Return false if element not found
    return False, count

found, steps = binary_search(target)

# if found then it will return True(Boolean), so the statement is tue
if found:
    print("Found", steps)
else:
    print("Not Found", steps)
    



    