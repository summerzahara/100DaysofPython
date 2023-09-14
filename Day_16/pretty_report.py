from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Doctor Name", ["Meredith Grey", "Alex Karev", "George O'Malley", "Izzie Stevens", "Christina Yang"])
table.add_column("Doctor Specialty", ["General Surgery", "Pediatric Surgery", "Trauma Surgery", "Neuro Surgery", "Cardiothoracic Surgery"])

table.align = "l"

print(table)