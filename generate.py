import itertools
import random

from helpers import all_unique, load_students, load_history, write_duos, load_presets, load_duos, overlapping

# Set these values!
team_count = 6
team_size = 2

students = load_students()

file = 'review'
use_presets = False


history = load_history(file)

options = set(itertools.combinations([student.uid for student in students.values()], team_size))
count = len(history) // team_count

if use_presets:
    pre_sets = load_presets()
    team_count -= len(pre_sets)

review_duos = load_duos('review')

while True:
    count += 1
    options = options - history

    if len(options) < team_count:
        exit("No more duo options. Finished generating.")

    print(f"Generating week {count}.")
    choice = None
    while not all_unique(choice) or overlapping(choice, review_duos.get(f'week{count}')):
        choice = random.choices(list(options), k=team_count)
        if use_presets:
            choice += pre_sets

    for pair in choice:
        history.add(pair)

    write_duos(file, count, choice)
