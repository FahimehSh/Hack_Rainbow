from hashlib import sha256
import csv
import collections


def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as input_file_name:
        reader = csv.reader(input_file_name)

        dictionary = dict()
        for row in reader:
            dictionary[row[0]] = row[1]
    

        l = []
        for item in list(dictionary.keys()):
            for i in range(1000, 10000):
                hashed_number = sha256(b'%i'% i).hexdigest()
                if hashed_number == dictionary[item]:
                    l.append([item, i])


        with open(output_file_name, 'w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            for item in l:
                writer.writerow(item)


