data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    letters.append(i) if type(i) == str else numbers.append(i)
del numbers[0]
numbers.insert(1, 2)
b = numbers.pop(0)
numbers.sort()
numbers = [i * i for i in numbers]
letters.append(b)
letters.reverse()
letters[1] = letters[1].upper()
letters[7] = letters[7].lower()
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)
