# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:16:03 2024

@author: Tepy Narin
"""
'''
1). Problem Description: Photos capture significant moments in our lives, and 
serve as a medium for our creative expression. Usually, visuals are created 
with paints and brushes. However, instead of using traditional tools, the 
program is an attempt to creative expression using lines of code instead. 
This program allows users to apply an artistic filter (grayscale) to their
24-bit BMP photo file, transforming the images into interesting visuals. 
The program processes images pixel-by-pixel and user will be prompted to type
in a BMP file into the python console. **note: file must be typed out with 
extension, and the BMP file must locate in the same director as the program/
script. :)   
'''
import os

#MAX IMAGE SIZE
MAX_BMP_SIZE = (1024 * 1024) * 3 #3 MB

def grayscale(red, blue, green):
    return (red + blue + green) // 3

def add_filter():
    #prompt user for input file and output file name
    infile = input("BMP image file: ")
    outfile = input("Output file name: ")
    
    #handling case errors for files
    #get file size
    file_size = os.path.getsize(infile)
    #read the file
    try:
        with open(infile, 'rb') as file:
            #Read forBMP header
            bmp_header = file.read(14) #BMP header = 14 bytes
            if len(bmp_header) < 14  or bmp_header[:2] != b'BM':
                raise ValueError("File is not a valid BMP.")
            elif file_size > MAX_BMP_SIZE:
                print("File exceed size limit")
                return
            else:
                #get pixel
                pixel_data_offset = int.from_bytes(bmp_header[10:14], byteorder='little')
            
            #Read for DIB header
            DIB_header = file.read(40) #Assuming BITMAPINFOHEADER (40 Bytes)
            if len(DIB_header) < 40:
                raise ValueError("DIB header is not BITMAPINFOHEADER.")
            
            #extract image dimensions
            width = int.from_bytes(DIB_header[4:8], byteorder='little', signed=True)
            height = int.from_bytes(DIB_header[8:12], byteorder='little', signed=True)
            
    except FileNotFoundError: #can't locate file
        print(f"{infile} does not exist in the directory")
        return
    except ValueError as e:
        print(f"{infile} is {e}")
        return
    
    #write the filtered BMP file
    try:
        with open(infile, 'rb') as input_file, open(outfile, 'wb') as output_file:
            #write headers to the output file
            output_file.write(bmp_header)
            output_file.write(DIB_header)
            
            #padding
            row_size = (width * 3 + 3) & ~3 #Align to 4 bytes
            padding = row_size - (width * 3)
            
            
            #seek to the pixel data
            input_file.seek(pixel_data_offset)
            
            for row in range(abs(height)): #handle both top-bottom or vice versa
                row_data = bytearray()
                for col in range(abs(width)):
                    bgr = input_file.read(3)
                    if len(bgr) < 3:
                        raise ValueError("Unexpected end of file while reading pixel data")
                    
                    b, g, r = bgr #unpack rgbs
                    grayvalue = grayscale(r, g, b)
                    row_data.extend([grayvalue, grayvalue, grayvalue])
                
                #write the row data to the output file
                output_file.write(row_data)
                
                #skip padding in input file, if any
                input_file.seek(padding, 1)
                
                #Add padding to output file
                output_file.write(b'\x00' * padding)
        return True
    except Exception as e:
        print(f"Error occured: {e}")
        

#call program function
new_img = add_filter()

if new_img is None:
    print("Program failed to apply filter")
else:
    print("Program successfuly applied filter to output file")