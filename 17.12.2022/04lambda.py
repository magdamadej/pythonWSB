fun_1 = lambda x: x ** 2 + 3
print(fun_1(30))

fun_2 = lambda word: word.upper()
print(fun_2('python'))

kwadraty = map(lambda x: x ** 2, range(10))
print(list(kwadraty))

def apply_function (x, fn):
    return fn(x)

print(apply_function([10, 20, 30], lambda x: sum(x)/len(x)))
print(apply_function(5, lambda x: x ** 6))

numbers = [-3, -2, -1, 0, 1, 2, 3]
print(sorted(numbers, key=-1))