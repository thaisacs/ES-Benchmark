import yaml
import os

def read_configs(filename):
    with open(filename) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs

def make_cmd(configs):
    cmd = 'ansible-playbook ./util/delete.yml --ask-become-pass --extra-vars '
    cmd += '\"pub_key=' + configs['pub_key'] + ' '
    cmd += 'pem_key=' + configs['pem_key'] + ' '
    cmd += 'pg_name=' + configs['placement_group']['name'] + ' '
    cmd += 'sg_name=' + configs['security_group']['name'] + ' '
    cmd += 'efs_name=' + configs['efs']['name'] + ' '
    cmd += 'efs_tag=' + configs['efs']['tag'] + ' '
    cmd += 'pg_strategy=' + configs['placement_group']['strategy'] + '\"'

    return cmd

def main():
    configs = read_configs('config.yml')
    cmd = make_cmd(configs)
    print(cmd)
    os.system(cmd)

if __name__ == "__main__":
    main()
