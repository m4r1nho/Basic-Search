# ↓ creating a function for sequential search
def sequential_search(seq, x):  # seq = sequence = the vector; x = the value for search
    seq.sort()
    for i in range(len(seq)):  # a loop with condition to value in sequence is equal a 'x'
        if seq[i] == x:
            print(f"Have the number {x} ")
            return True
    print(f"Don't have the number {x} ")


# ↓ creating a function for binary search
def binary_search(seq, x):
    seq.sort()
    left, right = 0, len(seq) - 1
    while left <= right:
        # ↓ the middle value for position
        middle = (left + right) // 2
        if seq[middle] == x:  # checking if it's the same value
            print(f"Have the number {x} ")
            return middle
        # orienting whether to go to the right (increasing the numbers) or to the left (decreasing the numbers)
        elif seq[middle] > x:
            right = middle - 1
        else:
            left = middle + 1
    print(f"Don't have the number {x} ")
