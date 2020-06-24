import os
import csv
import matplotlib.pyplot
from matplotlib.backends.backend_pdf import PdfPages

filename = 'experimental_results.summary.csv'

price = {}

def read_output(filename):
    i = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if(i > 0):
                try:
                    my_plot(row[0], row[1], float(row[3]))
                except:
                    print()
            i = 1

def define_array():
    price['t3.large-2'] = 2*0.0832
    price['t3.large-4'] = 4*0.0832
    price['t3.large-8'] = 8*0.0832
    price['m4.large-2'] = 2*0.1
    price['m4.large-4'] = 4*0.1
    price['m4.large-8'] = 8*0.1
    price['m5.large-2'] = 2*0.096
    price['m5.large-4'] = 4*0.096
    price['m5.large-8'] = 8*0.096

def my_plot(app, cfg, time):
    print(app)
    print(cfg)
    print(time)
    matplotlib.pyplot.plot(price[cfg]*time/60, time, 'ro')

def main():
    define_array()
    with PdfPages('teste.pdf') as pdf:
        read_output(filename)
        #matplotlib.pyplot.title(sys.argv[1])
        matplotlib.pyplot.xlabel('Iteração')
        matplotlib.pyplot.ylabel('Tempo de Execução (s)')
        matplotlib.pyplot.legend(loc="best")
        matplotlib.pyplot.grid(True)
        pdf.savefig()

if __name__ == "__main__":
    main()
