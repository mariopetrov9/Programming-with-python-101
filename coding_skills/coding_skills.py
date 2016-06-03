import json
import sys


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    return data


def main():
    language = ""
    data = read_json(sys.argv[1])
    result_dict = {
        'C++': {
            'name': "",
                    'points': 0
        },
        'Java': {
            'name': "",
                    'points': 0
        },
        'C#': {
            'name': "",
                    'points': 0
        },
        'Haskell': {
            'name': "",
                    'points': 0
        },
        'JavaScript': {
            'name': "",
                    'points': 0
        },
        'PHP': {
            'name': "",
                    'points': 0
        },
        'Python': {
            'name': "",
                    'points': 0
        },
        'Ruby': {
            'name': "",
                    'points': 0
        },
        'C': {
            'name': "",
                    'points': 0


        },
        'CSS': {
            'name': "",
            'points': 0
        }

    }
    for people in data:
        for i in range(0, len(data[people])):
            for j in range(0, len(data[people][i]['skills'])):
                language = data[people][i]['skills'][j]['name']
                if data[people][i]['skills'][j]['level'] > \
                        result_dict[language]['points']:
                    result_dict[language]['points'] = data[
                        people][i]['skills'][j]['level']
                    result_dict[language]['name'] = data[people][i][
                        'first_name'] + ' ' + data[people][i]['last_name']
    for item in result_dict:
        print(str(item) + " - " + str(result_dict[item]['name']))


if __name__ == '__main__':
    main()
