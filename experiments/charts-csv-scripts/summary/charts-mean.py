import csv
import numpy as np
import statistics
import matplotlib.pyplot as plt
import os
import sys

from matplotlib.backends.backend_pdf import PdfPages

avg_pi = []
first_pi = []
second_pi = []
avg_five = []
avg_ten = []
labels = []
names = []

new_avg_pi = []
new_labels = []
new_first_pi = []
new_second_pi = []
new_avg_five = []
new_avg_ten = []

def read_output(filename):
    i = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if(i > 0):
                avg_pi.append(float(row[6]))
                first_pi.append(float(row[8]))
                second_pi.append(float(row[9]))
                avg_five.append(float(row[10]))
                avg_ten.append(float(row[11]))
                labels.append(row[1])
                names.append(row[0])
            i = 1

def normalize():
    global new_avg_pi
    global new_labels
    global new_first_pi
    global new_second_pi
    global new_avg_five
    global new_avg_ten

    for i in range(0, len(avg_pi), 3):
        buffer = avg_pi[i] + avg_pi[i+1] + avg_pi[i+2]
        buffer = buffer/3
        new_avg_pi.append(buffer)
        buffer = first_pi[i] + first_pi[i+1] + first_pi[i+2]
        buffer = buffer/3
        new_first_pi.append(buffer)
        buffer = second_pi[i] + second_pi[i+1] + second_pi[i+2]
        buffer = buffer/3
        new_second_pi.append(buffer)
        buffer = avg_five[i] + avg_five[i+1] + avg_five[i+2]
        buffer = buffer/3
        new_avg_five.append(buffer)
        buffer = avg_ten[i] + avg_ten[i+1] + avg_ten[i+2]
        buffer = buffer/3
        new_avg_ten.append(buffer)
        new_labels.append(labels[i])
        new_name = names[i]

        if(len(new_labels) == 9):
            plot('mean'+new_name+'.pdf', new_name)
            new_avg_pi = []
            new_labels = []
            new_first_pi = []
            new_second_pi = []
            new_avg_five = []
            new_avg_ten = []

def plot(name, legend):
    with PdfPages(name) as pdf:

        width = 1.02
        rate = width/6

        fig = plt.figure(figsize=(15,6))
        ax = plt.subplot(111)

        x = np.arange(len(new_labels))

        ax.grid(True, zorder=0)
        ax.bar(x - 2*rate, new_avg_pi, rate, color='r', label='média-PIs', zorder=3)
        ax.bar(x - rate, new_first_pi, rate, color='b', label='1st-PI', zorder=3)
        ax.bar(x, new_second_pi, width=rate, color='k', label='2nd-PI', zorder=3)
        ax.bar(x + 1*rate, new_avg_five, rate, color='m', label='média(2-6)', zorder=3)
        ax.bar(x + 2*rate, new_avg_ten, rate, color='c', label='média(2-11)', zorder=3)

        plt.title(legend)
        plt.xlabel('Configuração do Cluster')
        plt.ylabel('Tempo de Execução PI (s)')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fancybox=True, shadow=True, ncol=5)
        ax.set_xticks(x)
        ax.set_xticklabels(new_labels)


        fig.tight_layout()
        pdf.savefig()

read_output('experimental_results.summary.csv')
normalize()
