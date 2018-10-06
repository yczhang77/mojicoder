#!/usr/bin/env python
#! encoding:UTF-8
import cairosvg
import os

def exportsvg(fromDir, targetDir, exportType):

    num = 0
    for a,f,c in os.walk(fromDir):#使用walk遍历源目录
        for fileName in c:
            path = os.path.join(a,fileName)#获得文件路径
            if os.path.isfile(path) and fileName[-3:] == "svg":#判断文件是否为svg类型
                num += 1
                fileHandle = open(path)
                svg = fileHandle.read()
                fileHandle.close()
                exportPath = os.path.join(targetDir, fileName[:-3] + exportType)#生成目标文件路径
                exportFileHandle = open(exportPath,'w')

                if exportType == "png":
                    try:
                        cairosvg.svg2png(bytestring=svg, write_to=exportPath)#转换为png文件
                    except:
                        continue

                exportFileHandle.close()



#---------------------------------------
svgDir = '/Users/xingjinbo/Documents/2018-1/ESTR3108_AI/project/mojicoder/dataset/svg_training1'#svg文件夹路径
exportDir = '/Users/xingjinbo/Documents/2018-1/ESTR3108_AI/project/mojicoder/dataset/test_svg2png1'#目的文件夹路径
exportFormat = 'png'#pdf#转换类型
if not os.path.exists(exportDir):
    os.mkdir(exportDir)
exportsvg(svgDir, exportDir, exportFormat)#转换主函数
#---------------------------------------
