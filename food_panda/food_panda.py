import time

time_ = time.strftime("%d.%m.%Y")


def parse_command(command):

    return tuple(command.split(" "))


def is_command(command_tuple, command_string):

    return command_tuple[0] == command_string


def meal(meal):
    filename = 'food_panda.txt'
    data = open(filename, 'a')

    data.write(time_ + ' ' + meal + '\n')
    data.close()

    return 'Ok it is saved'


def list_(eat_time):
    filename = 'food_panda.txt'
    data = open(filename, 'r')
    contain = data.read()
    contain = contain.split('\n')
    ate = []

    for line in contain:
        line.split(' ')
        if eat_time in line:
            ate.append(line[10:])
        else:
            continue

    return ''.join(ate)


def main():
    print('Hello and Welcome!')
    print('Choose an option.')
    print('1. meal - to write what are you eating now.')
    print('2. list <dd.mm.yyyy> - lists all the meals that you ate that day,')

    command = input('Enter command>')
    command = parse_command(command)

    if is_command(command, 'meal'):

        return(meal(command[1]))

    elif is_command(command, 'list'):

        return(list_(command[1]))


if __name__ == '__main__':
    print(main())

