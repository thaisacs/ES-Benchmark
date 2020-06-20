import yaml
import os
import sys

def read_configs(filename):
    with open(filename) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs

def make_cmd(configs):
    cmd = './run.sh ' + configs['efs_ip'] + ' ' + configs['dir']
    cmd += ' ' + configs['vm_type'] + ' ' + str(configs['nodes'])
    cmd += ' ' + configs['benchmark'] + ' '

    for i in configs['apps']:
        cmd += i + ' '

    return cmd

def main():
    configs = read_configs(sys.argv[1])
    cmd = make_cmd(configs)
    os.system(cmd)

if __name__ == "__main__":
    main()
