#  Question: 
#  Given an array of integers nums sorted in ascending order, find the starting and ending 
#  position of a given number.


def findLast(testsList, query):

    def condition(mid):
        if testsList[mid] == query:
            if (mid + 1) < len(testsList) and testsList[mid + 1] == query:
                return 'right'
            elif (mid == len(testsList)-1) or testsList[mid + 1] > query:
                return 'found'
        elif testsList[mid] > query:
            return 'left'
        elif testsList[mid] < query:
            return 'right'
    
    return binarySearch(0, len(testsList)-1, condition)

def findFirst(testsList, query):

    def condition(mid):
        if testsList[mid] == query:
            if (mid - 1) >= 0 and testsList[mid - 1] == query:
                return 'left'
            elif (mid == 0) or testsList[mid - 1] < query:
                return 'found'
        elif testsList[mid] > query:
            return 'left'
        elif testsList[mid] < query:
            return 'right'
    
    return binarySearch(0, len(testsList)-1, condition)
            

def binarySearch(low, high, condition):
    while high >= low:
        mid = (high + low) // 2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'right':
            low = mid + 1
        elif result == 'left':
            high = mid - 1

    return -1

tests = {
  'input' : {
    'cards' : [1, 1, 7, 10, 27, 38, 38, 40, 40, 40, 40, 70, 99, 99],
    'query' : 40
   }
}

beginPoint = findFirst(tests['input']['cards'], tests['input']['query'])
endPoint = findLast(tests['input']['cards'], tests['input']['query'])

print(f"Startind point = {beginPoint}.")
print(f"Ending point = {endPoint}.")



