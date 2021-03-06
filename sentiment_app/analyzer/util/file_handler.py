import csv

from ..preprocessing import preprocess


def load_data(filename):
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            topic, label, tweet = row
            if (label != "irrelevant") and (label != "neutral"):
                feature = ((topic, preprocess(tweet)), label)
                data.append(feature)

    return data

def load_data_unpreprocessed(filename):
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            topic, label, tweet = row
            if (label != "irrelevant") and (label != "neutral"):
                data.append(row)

    return data
