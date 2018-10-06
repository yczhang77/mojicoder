#import packages...
from os.path import basename
import os
import copy
import json
import sys

#input judgement..
input_file = ''
input_path = ''
mapping_path = './dslmapping.json'

def generate_branch_of_files(input_path, output_path):
    count = 0
    for file in os.listdir(input_path):
        if file.find('.emj') != -1:
            file_path = '{}/{}'.format(input_path, file)
            generate_single_file_code(file_path, output_path)
            print(count)
            count += 1


def generate_single_file_code(input_file, output_path):
    type_index = basename(input_file)[:basename(input_file).find('.')]
    path = input_file[:input_file.find(type_index)]
    input_path = "{}{}.emj".format(path, type_index)
    output_path = "{}{}.svg".format(output_path, type_index)
    with open(mapping_path) as data_file:
        component_mapping = json.load(data_file)
    dsl_file = open(input_path)

    head = '<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n<svg version=\"1.1\" id=\"Layer_1\"\
     xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\"\
      y=\"0px\"\nviewBox=\"0 0 512.001 512.001\" style=\"enable-background:new 0 0 512.001 512.001;\" xml:space=\"preserve\">'
    tail = '</svg>'
    content = copy.deepcopy(head)
    for line in dsl_file:
        line = line.replace('\n', '')
        content += component_mapping[line]
    content += tail
    with open(output_path, 'w') as output_file:
        print(output_path)
        output_file.write(content)

mode = 0;
if __name__ == '__main__':
    argv = sys.argv[1:]
    length = len(argv)
    if length == 3:
        mode = argv[0]
        output_path = argv[2] + '\\'
        if argv[0] == '1':
            input_file = argv[1]
            generate_single_file_code(input_file, output_path)
        elif mode == '2':
            input_path = argv[1]
            generate_branch_of_files(input_path, output_path)
        else:
            print('wrong mode...')
            exit(0)
    else:
        print('wrong input!!!')
        exit(0)
