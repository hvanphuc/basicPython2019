#!/bin/python
import sys   # import module sys

usage='pythonscript.py <inputfile> <outputfile>'

numberArgv=len(sys.argv)  # số tham số truyền vào
listArgv=sys.argv   # list các tham số truyền vào

if numberArgv < 3:
    print (usage)
else:
    print('Số tham số là:', numberArgv)
    print('Các tham số là:', listArgv)
    print('Tham số đầu tiên là:', listArgv[0])
    print('Tham số thứ 2 là:', listArgv[1])
    print('Tham số thứ 3 là:', listArgv[2])
    print('-----------------------------')
    #main()

def main():
        inputfile=open(sys.argv[1], r ) # mở file và cấp quyền được đọc
        inputContent=inputfile.read() # đọc nội dung của file input
        print(outputContent)
        
        outputfile=open(sys.argv[2], w) # mở file và cấp quyền được ghi, nếu file chưa tồn tại, tạo file mới
        outputContent=outputfile.write(inputContent)
        print(outputContent)