with open('results.txt') as file:
    lines = file.readlines()
results_dict = {}
for i in lines[1:]:
    name = i.split()[0]
    rate = i.split()[1]
    results_dict[name] = {"оценка": int(rate)}
sorted_results = sorted(results_dict.items(), key=lambda x: x[1]['оценка'], reverse=True)
for i in results_dict.items():
    print(i)
print('топ 3 лучших)):')
for i, (name, result) in enumerate(sorted_results[:3], 1):
    print(f'{i}. {name}:{result["оценка"]}')
with open('sorted_results.txt', 'w') as file:
    file.write('results\n')
    for name, result in sorted_results:
        file.write(f'{name} {result["оценка"]}\n')
with open('sorted_results.txt') as file:
    print(f'Содержимое файла sorted_results.txt:\n{file.read()}')
