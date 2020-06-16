import csv
import matplotlib.pyplot
import os
import sys

def read_output(filename):
  paramount_iteration = []
  x = []

  with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
      if(row[1] == '0'):
        paramount_iteration.append(float(row[4]))
        x.append(int(row[2]))

  return paramount_iteration,x

j = 2
for i in sys.argv[2:len(sys.argv)]:
    results,x = read_output(i)
    matplotlib.pyplot.plot(x, results, label=str(j)+"x")
    j *= 2

matplotlib.pyplot.xlabel('Iteração')
matplotlib.pyplot.ylabel('Tempo de Execução (s)')
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.savefig(sys.argv[1]+".png")
