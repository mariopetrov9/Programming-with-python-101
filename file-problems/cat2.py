import sys


def main():
    for filename in sys.argv[1:]:
        data = open(filename, 'r')
        print('{0} \n'.format(data.read()))
        data.close()

if __name__ == '__main__':
    main()
