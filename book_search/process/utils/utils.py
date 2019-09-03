
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def string_to_file(string, file):
    text_file = open(file, "w")
    text_file.write(str(string))
    text_file.close()


def file_to_string(file_locaiton, as_lines=False):
    with open(file_locaiton, 'r') as file:
        if as_lines:
            data = file.read().replace('\n', '')
        else:
            data = file.readline()

    return data