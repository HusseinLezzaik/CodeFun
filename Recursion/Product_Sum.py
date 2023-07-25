# Product Sum: Recursive

# O(n) time | O(d) space
def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

# Test Cases
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))  # Expected output: 12

array = [1, 2, 3, 4, 5]
print(productSum(array))  # Expected output: 15