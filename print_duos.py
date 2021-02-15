from helpers import load_students, load_duos

students = load_students()

file = input('Which file: ')
week = input('Which week: ')
duos = load_duos(file)

print(f"{file.capitalize()} Teams voor week {week}")
for num, duo in enumerate(duos[f'week{week}']):
    print(f"Team {num + 1}: {students[duo[0]]}, {students[duo[1]]}")