import csv
import statistics
import matplotlib.pyplot
import os
import sys

from matplotlib.backends.backend_pdf import PdfPages

matplotlib.pyplot.figure(figsize=(10,6))

paramount_iteration = {}
labels = []

results_all_m = {}
results_all_d = {}

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

        make_results(values, label_index)
        label_index += 1

def make_results(results, label_index):
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

    results_all_m[label_index] = m
    results_all_d[label_index] = d

def my_plot_relative():
    menor = 1000000
    index = -1
    m = []
    d = []
    x = []

    for i in results_all_m:
        if(menor > statistics.mean(results_all_m[i])):
            menor = statistics.mean(results_all_m[i])
            index = i

    for i in results_all_m:
        for j in range(0, len(results_all_m[i])):
            m.append(results_all_m[i][j]/results_all_m[index][j])
            d.append(results_all_d[i][j])
            x.append(j+1)
        matplotlib.pyplot.errorbar(x, m, d, label=labels[i])
        m = []
        d = []
        x = []

with PdfPages('../charts-csv-scripts/charts/'+sys.argv[1]+'-relative.pdf') as pdf:
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
    my_plot_relative()
    matplotlib.pyplot.title(sys.argv[1])
    matplotlib.pyplot.xlabel('Iteração #')
    matplotlib.pyplot.ylabel('Desempenho relativo')
    matplotlib.pyplot.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.tight_layout()
    pdf.savefig()
