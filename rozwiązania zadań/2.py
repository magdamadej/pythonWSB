numbers = [
    [1,2,3,4,5],
    [1,2,3,4],
    [5],
    [1,2,3,4,5,6,7,8]
]

#list comprehension
numbers_filter = [sum(number) if len(number) % 2 == 0 else sum(number) / len(number) for number in numbers if len(number) > 3]

print(numbers_filter)

#klasycznie
numbers_filter_classic = []
for number in numbers:
    if len(number) > 3:
        if len(number) % 2 == 0:
            numbers_filter_classic.append(sum(number))
        else:
            numbers_filter_classic.append(sum(number) / len(number))

print(numbers_filter_classic)