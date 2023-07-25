# Fruit Into Basket: https://leetcode.com/problems/fruit-into-baskets/

# O(n) time | O(1) space
def totalFruit(fruits):
    window_start = 0
    max_fruits = 0
    fruit_freq = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1

        max_fruits = max(max_fruits, window_end-window_start+1)

    return max_fruits


# Test Cases
print(totalFruit([1,2,1]))  # Expected output: 3
print(totalFruit([0,1,2,2]))  # Expected output: 3