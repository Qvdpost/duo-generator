# Duo Generator Application

Make sure `team_count`, `team_size`, `file` and `use_preset`in generate.py are set to your preferred values.
Then in students.csv add each student in your tutorial to the list with a unique id in the first column, and their name in the second column.
Add any amount of dummy students in case you do not have a divisible number of students for your `team_size`.

Then just run `python generate.py` to generate the duos. A file will be created or appended to if it already existed called '{file}_duo.csv'.
Running `python print_duos.py` prompts you for the week and file to parse and prints the teams to the terminal.