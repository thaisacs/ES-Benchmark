import csv
import statistics
import matplotlib.pyplot
import os
import sys

from matplotlib.backends.backend_pdf import PdfPages

matplotlib.pyplot.figure(figsize=(15,5))

paramount_iteration = {}
#def read_output(filename):
#  paramount_iteration = []
#  x = []
#
#print(name.split('/'))
#
#  with open(filename, 'r') as file:
#    reader = csv.reader(file, delimiter = ',')
#    for row in reader:
#      if(row[1] == '0'):
#        paramount_iteration.append(float(row[4]))
#        x.append(int(row[2]))
#
#  return paramount_iteration,x

def read_output(filename):

    name_split = filename.split('/')
    key = name_split[0] + ":" + name_split[1]
    date = name_split[2]

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if(row[1] == '0'):
                if(not key in paramount_iteration):
                    paramount_iteration[key] = {}
                    paramount_iteration[key][date] = []
                    (paramount_iteration[key][date]).append(float(row[4]))
                else:
                    if(not date in paramount_iteration[key]):
                        paramount_iteration[key][date] = []
                        (paramount_iteration[key][date]).append(float(row[4]))
                    else:
                        (paramount_iteration[key][date]).append(float(row[4]))

def make_array(results):
    for i in results:
        values = []

        key = list((results[i]).keys())[0]
        for j in range(0, len(results[i][key])):
            values.append([])

        for j in range(0, len(results[i][key])):
            for l in range(0, len(results[i])):
                values[j].append(0)


        m = 0
        for j in results[i]:
            for k in range(0, len(results[i][key])):
                values[k][m] = results[i][j][k]
            m += 1

        my_plot(values)

def my_plot(results):
    m = []
    d = []
    x = []

    for i in range(0, len(results)):
        m.append(statistics.mean(results[i]))
        d.append(statistics.stdev(results[i]))
        x.append(i)

    matplotlib.pyplot.errorbar(x, m, d, label="2x")


for i in sys.argv[2:len(sys.argv)]:
    read_output(i)

make_array(paramount_iteration)

matplotlib.pyplot.title(sys.argv[1])
matplotlib.pyplot.xlabel('Iteração')
matplotlib.pyplot.ylabel('Tempo de Execução (s)')
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.savefig("../charts/"+sys.argv[1]+".png", dpi=150)
