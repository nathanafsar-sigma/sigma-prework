def max_min(numbers):
    numbers_int = []
    for num in numbers:
        numbers_int.append(int(num))
    numbers_int.sort()
    return [numbers_int[0], numbers_int[-1]]


numbers = input("Enter a list of numbers separated by commas: ").split(",")
print(max_min(numbers))
