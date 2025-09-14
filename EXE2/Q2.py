# Riki Rubin 326380359
# Hadas Donat 325950954

from functools import reduce

numbers = list(range(1, 1001))
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 == 1, numbers))

# product function (cumulative product)
prod_func = lambda lst: [reduce(lambda a, b: a * b, lst[:i+1]) for i in range(len(lst))]

# linear with next element
lin_func = lambda lst: [x/2 + 2 + (lst[i+1] if i+1 < len(lst) else 0) for i, x in enumerate(lst)]

even_results = prod_func(evens)
odd_results = lin_func(odds)

odd_sum = sum(odd_results)
even_sum = sum(even_results)


if __name__ == "__main__":
    print("Odd sum:", odd_sum)
    print("Even sum:", even_sum)

