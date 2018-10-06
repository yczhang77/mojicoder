import sys
import os
import shutil

if __name__ == '__main__':
    argv = sys.argv[1:]
    input_path = argv[0]
    format = argv[1]
    count = 0
    if format =='svg':
        for file in os.listdir(input_path):
            if file.find('.svg') != -1:
                indexstr = '0'
                if count<10:
                    indexstr+=str(count)
                else:
                    indexstr = str(count)
                os.rename(input_path +'\\' + file, input_path + '\\' + indexstr + file[3:])
                count += 1

    elif format =='emj':
        output_path = argv[2]
        for file in os.listdir(input_path):
            if file.find('.emj')!=-1:
                for cot in range(21):
                    indexstr = '0'
                    file_name = file[:file.find('.emj')] + '_' + str(cot) + '.emj'
                    shutil.copy(input_path +'\\' + file, output_path + '\\' + file_name)
