import time
import json
import csv

time_ = time.strftime("%d.%m.%Y")


def read_json(path):
    with open(path) as file_data:
        data = json.load(file_data)

    return data


def update_json(data, path):
    with open(path, 'w') as file_data:
        json.dump(data, file_data)


def get_grams(weight):
    if 'kg' in weight:
        return int(weight[:len(weight) - 2]) * 1000
    else:
        return int(weight[:len(weight) - 1])


def parse_command(command):

    return tuple(command.split(" "))


def is_command(command_tuple, command_string):

    return command_tuple[0] == command_string

def meal(food, calories):
    d = datetime.today().strftime('%d.%m.%y')
    with open('panda.csv', 'a', newline='') as csvfile:
        foodwriter = csv.writer(csvfile, delimiter=',')


def main():
    print('Hello and Welcome!')
    print('Choose an option.')
    print('1. meal - to write what are you eating now.')
    print('2. list <dd.mm.yyyy> - lists all the meals that you ate that day,')

    command = input('Enter command>')
    command = parse_command(command)

    if is_command(command, 'meal'):

        meal(command[1])
        weight = input('How much have you eaten? >>')
        weight = get_grams(weight)
        calories_dict = read_json('calories.json')
        if command[1] in calories_dict.keys():
            calories = calories_dict[command[1]] / 100 * weight
            print('OK, this is a total of {0} calories for this meal.'.format(calories))
        else:
            print('I don\'t have {0} in the calories database.'.format(command[1]))
            add_cal = int(input('How much calories per 100g?>>'))
            calories_dict[command[1]] = add_cal
            update_json(calories_dict, 'calories.json')
            calories = calories_dict[command[1]] / 100 * weight
            print('OK, this is a total of {0} calories for this meal.'.format(calories))
    elif is_command(command, 'list'):

        return(list_(command[1]))


if __name__ == '__main__':
    main()
