#import packages...
from os.path import basename
import copy
import json
import sys

#input judgement..
input_file = ''
if __name__ == '__main__':
    argv = sys.argv[1:]
    length = len(argv)
    if length != 0:
        input_file = argv[0]
    else:
        print('wrong input!!!')
        exit(0)

mapping_path = './dslmapping.json'

type_index = basename(input_file)[:basename(input_file).find('.')]
path = input_file[:input_file.find(type_index)]

input_path = "{}{}.emj".format(path, type_index)
output_path = "{}{}.svg".format(path, type_index)

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
    output_file.write(content)
