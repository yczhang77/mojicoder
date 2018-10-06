import numpy as np
import os
import sys
import random

#includes all possible tags except for "redFace"...
face = ["circleFace"]
elsethings = ["blueRing","LeftSteam","RightSteam","sunglasses",
"LeftBrow","RightBrow","cryEyes","smallLeftBrow",
"smallRightBrow","blue_tearLeft","blue_sweatLeft","laugh_tearLeft","laugh_tearRight",
"very_pieLeftBrow","very_naRightBrow","small_z","big_z","shaming"]
mouths = ["waveMouth","cMouth","down_cMouth","lineMouth","small_cMouth","hookMouth","small_downMouth",\
"ovalMouth","very_lowMouth","toothMouth","kissMouth","chaMouth","spannerMouth","catMouth",\
"tongueMouth","shipMouth","surpriseMouth","lueMouth","sweetMouth","down_cMonth","waaMouth"]
LeftEye = ["defaultLeftEye","cLeftEye","angryLeftEye","up_cLeftEye","pieLeftEye","coolLeftEye",\
"small_vLeftEye","bulingLeftEye","very_lowLeftEye","ringLeftEye",\
"moneyLeftEye","half_circleLeftEye","heartLeftEye","lineLeftEye",\
"chaLeftEye","uppercLeftEye","very_low_upLeftEye","vshapeLeftEye",\
"surpriseLeftEye","pandaLeftEye","defaultLeftEye"]
RightEye = ["defaultRightEye","cRightEye","angryRightEye","up_cRightEye","naRightEye","coolRightEye",\
"small_vRightEye","bulingRightEye","very_lowRightEye","ringRightEye","moneyRightEye",\
"half_circleRightEye","heartRightEye","lineRightEye","chaRightEye","uppercRightEye",\
"ver_low_upRightEye","vshapeRightEye","surpriseRightEye","pandaRightEye", "suspectRightEye"]

indices = {"face": face, "leftEye": LeftEye, "rightEye": RightEye,\
            "mouth": mouths, "else": elsethings}

def generate_emj (dictionary, output_path, output_size = 1000):
    content = dictionary['face'][0] + '\n'
    LE = ''
    RE = ''
    MO = ''
    EL = ''
    for count in range(output_size):
        if count%5 == 0:
            LE = random.choice(dictionary['leftEye']) + '\n'
            RE = random.choice(dictionary['rightEye']) + '\n'
        else:
            randomnum = random.randint(0, len(RightEye)-1)
            LE = dictionary['leftEye'][randomnum] + '\n'
            RE = dictionary['rightEye'][randomnum] + '\n'
        MO = random.choice(dictionary['mouth']) + '\n'
        EL = random.choice(dictionary['else']) + '\n'
        result = content + LE + RE + MO + EL
        file_path = output_path + '\\' + 'training_data' + str(count) + '.emj'
        open(file_path, 'w').write(result)


if __name__ == '__main__':
    argv = sys.argv[1:]
    filename = 'training_data'
    if len(argv) != 0:
        output_path = argv[0]
        if len(argv) != 1:
            output_size = int(argv[1])
            generate_emj(indices, output_path, output_size)
        else:
            generate_emj(indices, output_path)
    else:
        print("wrong number of arguments: [.py output_path number_of_output ]")








    #comment
