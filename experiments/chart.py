import csv
import statistics
import matplotlib.pyplot
import os
import sys

from matplotlib.backends.backend_pdf import PdfPages

matplotlib.pyplot.figure(figsize=(15,5))

paramount_iteration = {}
labels = []

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
    label_index = 0
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

        my_plot(values, label_index)
        label_index += 1

def my_plot(results, label_index):
    m = []
    d = []
    x = []

    for i in range(0, len(results)):
        m.append(statistics.mean(results[i]))
        if(len(results[0]) == 1):
            d.append(0)
        else:
            d.append(statistics.stdev(results[i]))
        x.append(i+1)

    matplotlib.pyplot.errorbar(x, m, d, label=labels[label_index])


for i in sys.argv[2:len(sys.argv)]:
    labels.append(i.split('/')[1])
    read_output(i)

labels_clean = []
labels_clean.append(labels[0])
for i in range(1, len(labels)):
    if(labels[i] != labels[i-1]):
        labels_clean.append(labels[i])

labels = labels_clean

make_array(paramount_iteration)

matplotlib.pyplot.title(sys.argv[1])
matplotlib.pyplot.xlabel('Iteração')
matplotlib.pyplot.ylabel('Tempo de Execução (s)')
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.savefig("../charts/"+sys.argv[1]+".png", dpi=150)
#matplotlib.pyplot.savefig("../charts/"+sys.argv[1]+".pdf", bbox_inches='tight')
