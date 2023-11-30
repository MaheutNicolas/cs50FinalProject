import csv
import os
import sys


def getText():

    path = 'language_files'
    files = os.listdir(path)

    languageDict = {}

    for file in files:
        with open(path+'/'+file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            value = next(reader)[0]
            languageDict[value] = [row[0] for row in reader]

    return languageDict
