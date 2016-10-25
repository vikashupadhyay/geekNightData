import csv
import sys
import pyexcel as pyexcel

def fileReader(filepath, fileName):
    cla = sys.argv[3].split()
    filter_data = [cla]
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for each_data in reader:
            filter_data.append(map(lambda x:each_data[x],cla))
    pyexcel.save_as(array=filter_data, dest_file_name=fileName)
if __name__ == '__main__':
    fileReader(sys.argv[1],sys.argv[2])