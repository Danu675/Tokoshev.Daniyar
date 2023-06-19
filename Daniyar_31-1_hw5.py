Geeks = {
    'Address': 'Toktogula 175',
    'Courses': ['Android', 'Backend', 'Frontend'],
    'Bag': {'fails', 'errors', 'stack'}
}
del Geeks["Bag"]
Geeks["Address"] = "Bisness Centr Victory"
Geeks["Number"] = "996507052018"
Geeks["Instagram"] = "geeks_edu"
new = "Ios development", "Android development", "UX/UI Designer", "Basics of programming", "Project Manager"
Geeks["Courses"].extend(new)
new_new = set(new)
Geeks['Opening date'] = '20.05.18'
print("Number of courses available: ", len(Geeks['Courses']))
for key, value in Geeks.items():
    print(f'{key}: {value}')
