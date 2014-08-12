#example of how to parse a .csv file
#run with python parsecsv.py < test.csv
import fileinput
for line in fileinput.input():
    line=line.strip()
    info=line.split(',')
    print info[1]+'+'+info[0]
