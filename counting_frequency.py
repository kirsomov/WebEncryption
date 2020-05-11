import pickle
from collections import Counter


def get_frequency_dict(input_string):
    frequency_dict = dict(Counter(input_string).most_common())
    for key in frequency_dict.keys():
        frequency_dict[key] /= len(input_string)
    return frequency_dict


def dump_dict(dictionary, output_file):
    with open(output_file, 'wb') as output_f:
        pickle.dump(dictionary, output_f)


def dump_frequency(input_string, output_file):
    dump_dict(get_frequency_dict(input_string), output_file)


def load_frequency(symbols_frequency):
    with open(symbols_frequency, 'rb') as symbols_frequency_f:
        return pickle.load(symbols_frequency_f)
