# mojicoder
This is the ESTR3108 course project. An emoji code generator.
The project mainly depends on the idea of [model of #pix2code](https://github.com/tonybeltramelli/pix2code). 
We firstly change the I/O enviornment of it to **grayscale emoji images**.
## First Things First: DSL Compiler and Input Data Management
DSL Compiler usage: 
```
cd compiler
compiler.py emj_file_path.emj
```
PNG image pre-processing usage:
```
cd model/dataprocess
imageprocess.py png_file_path.png
```
