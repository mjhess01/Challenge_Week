li = [1, 10, 8, 3, 2]

def find_max(li):
    current_max = 0
    for num in li:
        if current_max < num:
            current_max = num
    print(current_max)

find_max(li)

