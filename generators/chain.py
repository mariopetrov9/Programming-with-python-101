import glob

def chain(iterable_one, iterable_two):
    for elem in iterable_one:
        yield elem
    for elem in iterable_two:
        yield elem

# print(list(chain(range(0, 4), range(4, 8))))
#  [0, 1, 2, 3, 4, 5, 6, 7]


def compress(iterable, mask):
    mapped = zip(iterable, mask)
    for elem in mapped:
        if elem[1]:
            yield elem[0]

# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
# ["Panda"]


def cycle(iterable):
    while True:
        for elem in iterable:
            yield elem


# endless = cycle(range(0, 10))
# for item in endless:
#     print(item)


class BookReader:
    def __init__(self, path):
        self.path = path + '/*.txt'
        self.number_chapter = 0
        self.files_text = ""
        self.until_chapter = 0

    def __iter__(self):
        return self

    def __call__(self):
        for f in glob.glob(self.path):
            with open(f, 'r') as opened_file:
                readed = opened_file.read()
                self.number_chapter += readed.count("Chapter ")
                self.files_text += readed
        print(self.files_text)

    def __next__(self):
        for f in glob.glob(self.path):
            with open(f, 'r') as opened_file:
                # str_lines = ""
                for line in opened_file.readlines():
                    if line.startswith("#"):
                        yield str(line)

fib = BookReader("/home/krasi_b2/HackBulgaria/week13/Book")

command = input("Enter a command: ")
if command is " ":
    for number in fib:
        print(number)


# book_reader("/home/krasi_b2/HackBulgaria/week13/Book")