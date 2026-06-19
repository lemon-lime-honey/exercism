"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    if tuple(azara_record[1]) == tuple(rui_record[1]):
        return True
    return False

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'

def clean_up(combined_record_group):
    report = ''
    form = "('{one}', '{two}', ('{three}', '{four}'), '{five}')\n"
    for record in combined_record_group:
        report += form.format(one = record[0], two = record[2], three = record[3][0], four = record[3][1], five = record[4])
    return report
