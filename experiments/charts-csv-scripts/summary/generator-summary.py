import os
import pathlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

filename = 'experimental_results.summary.csv'

def echo_head():
    cmd = 'echo "test-case,cfg,date,total_time-time,total_time-main,beta,avg-PIs,n-PIs,1st-PI,2nd-PI,avg(2-6),avg(2-11)" > ' + filename
    os.system(cmd)

def echo_new_line(test_case, cfg, date, time, main, beta, avg, n, first, second, avg1, avg2):
    cmd = 'echo ' + test_case + ',' + cfg + ',' + date + ',' + time + ',' + main + ',' + beta + ',' + avg + ',' + n + ',' + first + ',' + second + ',' + avg1 + ',' + avg2 + ' >> ' + filename
    os.system(cmd)

def run():
    contents = pathlib.Path("../../experimental_results").iterdir()
    for path in contents:
        contents_cfg = pathlib.Path(path).iterdir()
        for path_cfg in contents_cfg:
            contents_date = pathlib.Path(path_cfg).iterdir()
            for path_date in contents_date:
                test_case = ''
                cfg = ''
                date = ''
                time, main = '', ''
                beta, avg = 0.0, 0.0
                n = 0
                first, second, avg1, avg2 = 0.0, 0.0, 0.0, 0.0

                for subdir, dirs, files in os.walk(path_date):
                    for file in files:
                        filepath = subdir + os.sep + file

                        filename_split = file.split('.')
                        subdir_split = subdir.split('/')

                        test_case = subdir_split[3]
                        cfg = subdir_split[4]
                        date = subdir_split[5]

                        if(filename_split[len(filename_split)-1] == 'out'):
                            file = open(filepath, "r")
                            lines = file.readlines()
                            for line in lines:
                                if('Total time' in line):
                                    main_string = line.split(',')[1]
                                    main = main_string.replace('\n', '')
                                if('Beta' in line and ',0,' in line):
                                    beta_string = line.split(',0,')[1]
                                    beta = beta_string.replace('\n', '')
                                if('PI avg' in line and ',0,' in line):
                                    string = line.split(',0,')[1]
                                    string = string.split(',')
                                    avg = string[0]
                                    n = int((string[1]).replace('\n', ''))
                                if('Paramount Iteration,0,1,' in line):
                                    first_string = line.split(',')
                                    first_string = first_string[len(first_string)-1]
                                    first = float(first_string.replace('\n', ''))
                                if('Paramount Iteration,0,2,' in line):
                                    second_string = line.split(',')
                                    second_string = first_string[len(first_string)-1]
                                    second = float(first_string.replace('\n', ''))
                                    avg1 += second
                                if('Paramount Iteration,0,3,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,4,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,5,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,6,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,7,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,8,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,9,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,10,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                                if('Paramount Iteration,0,11,' in line):
                                    value = line.split(',')
                                    value = value[len(value)-1]
                                    value = float(value.replace('\n', ''))
                                    avg1 += value
                                    avg2 += value
                        elif(filename_split[len(filename_split)-1] == 'err'):
                            file = open(filepath, "r")
                            lines = file.readlines()
                            #for line in lines:
                            #    if('wall clock' in line):
                            #        line_split = line.split(' ')
                            #        time_string = line_split[len(line_split)-1]
                            #        time = time_string.replace('\n', '')
                        elif(filename_split[len(filename_split)-1] == 'time'):
                            file = open(filepath, "r")
                            lines = file.readlines()
                            for line in lines:
                                if('real' in line):
                                    time = line.split(' ')[1]
                                    time = time.replace('\n', '')
                avg1 = avg1/5
                avg2 = avg2/10
                echo_new_line(test_case, cfg, date, time, main, str(beta), str(avg), str(n), str(first), str(second), str(avg1), str(avg2))

def main():
    echo_head()
    run()

if __name__ == "__main__":
    main()
