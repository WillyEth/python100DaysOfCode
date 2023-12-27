numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in numbers]
print(squared_numbers)

numbers1 = ["9", "0", "32", "8", "64", "29", "42", "99"]

list_of_integers = [int(n) for n in numbers1]

results_even = [n for n in list_of_integers if n % 2 == 0]
print(results_even)

