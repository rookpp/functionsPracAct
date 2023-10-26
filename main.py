def max_num(one,two,three):
    ar=[one,two,three]
    ar.sort()
    return ar[-1]

def mult_list(numbers):
    result = 1
    for num in numbers:
        if isinstance(num, (int, float)):
            result *= num  
    return result


def rev_string(string):
    print(string[::-1])

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range
def pascal(n):
    for i in range(n):
        num = 1
        print(num, end=" ")
        for j in range(1, i + 1):
            num = num * (i - j + 1) // j
            print(num, end=" ")
        print()
        
