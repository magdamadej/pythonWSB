import timeit

code1 = """
numbers = []
for i in range(10):
    numbers.append(i)
"""

code2 = """
numbers = [i for i in range(10)]
"""

# time1 = timeit.timeit(code1, number=1000000)
# time2 = timeit.timeit(code2, number=1000000)
# print(time1, time2)

wyniki_biegu_na_100_m = {
    'Mateusz' : 12,
    'Norbert' : 10,
    'Wojtek' : 15,
    'Bartek' : 13,
}

result = sorted(wyniki_biegu_na_100_m.items(), key = lambda x: x[1])[0][0]
print(result)