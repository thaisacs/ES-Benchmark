import yaml
import os
import sys

def read_configs(filename):
    with open(filename) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs

def make_cmd(configs):
    cmd = './util/compile.sh ' + configs['efs_ip'] + ' '
    cmd += ' ' + configs['vm_type']
    cmd += ' ' + configs['benchmark']

    return cmd

def main():
    configs = read_configs('config.yml')
    cmd = make_cmd(configs)
    os.system(cmd)

if __name__ == "__main__":
    main()
