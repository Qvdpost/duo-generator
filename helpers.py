from classes import Student
import csv
import os

def all_unique(duos):
    if not duos:
        return False

    uniques = set()
    for pair in duos:
        for student in pair:
            if student in uniques:
                return False
            uniques.add(student)
    return True

def load_students():
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        students = {int(uid): Student(uid, name) for uid, name in reader}
    return students

def load_history(file):
    history = set()

    if not os.path.isfile(f'{file}_duos.csv'):
        return history

    with open(f'{file}_duos.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for week in reader:
            [history.add(eval(duo)) for duo in week[1:]]

    return history

def write_duos(file, num, duos):
    if not os.path.isfile(f'{file}_duos.csv'):
        permission = 'w'
    else:
        permission = 'a'

    with open(f'{file}_duos.csv', permission, newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([f'week{num}'] + duos)

def load_duos(file):
    duos = {}
    if not os.path.isfile(f'{file}_duos.csv'):
        return duos

    with open(f'{file}_duos.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for week in reader:
            duos[week[0]] = [eval(duo) for duo in week[1:]]

    return duos

def load_presets():
    with open('pre_set.txt', 'r') as f:
        duos = [eval(duo) for duo in f]
    return duos

def overlapping(duos, other):

    if not duos or not other:
        return False

    if len(set(duos) & set(other)) > 0:
        return True

    return False