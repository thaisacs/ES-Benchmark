import csv
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

npb = ['bt.B.info', 'cg.C.info', 'lu.C.info',
        'sp.C.info', 'bt.C.info', 'ft.C.info',
        'sp.B.info']

pyranda = ['3dadvect.info', 'gatech.info']

values = []
x = [1, 2, 4, 8]

def read_output(filename):
    with open('info/'+filename, 'r') as file:
        reader = csv.reader(file, delimiter = '\n')
        for row in reader:
            values.append(float(row[0]))

def calculate():
    for i in range(1, len(values)):
        values[i] = values[0]/values[i]
    values[0] = 1

with PdfPages('speedup.pdf') as pdf:
    for app in npb:
        read_output(str(app))
        calculate()
        string = app.split('.')
        plt.plot(x, values, label=string[0] + '.' + string[1])
        values = []

    for app in pyranda:
        read_output(str(app))
        calculate()
        string = app.split('.')
        plt.plot(x, values, label=string[0])
        values = []

    plt.plot([1, 2, 4, 8], [1, 2, 4, 8], 'k--', label='ideal')

    plt.title('NPB e Pyranda')
    plt.xlabel('Processos MPI #')
    plt.ylabel('Speedup')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), fancybox=True, shadow=True, ncol=5)
    plt.tight_layout()
    plt.grid(True)
    pdf.savefig()
