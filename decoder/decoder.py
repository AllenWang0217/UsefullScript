# -*- coding: UTF-8 -*-
import os
import re
import struct
import argparse

def get_hex_data(input_file):
    f = open(input_file)
    input_data = f.read()
    input_data = input_data.replace("\n", "")
    input_data = input_data.replace("\r", "")
    input_data = input_data.replace(" ", "")
    input_data = input_data.replace("0x", "")
    input_data = input_data.replace("0X", "")
    input_data = input_data.replace(",", "")
    f.close()
    return input_data

def get_bin_data(input_data):
    len_s = int(len(input_data)/2) # 计算字节的个数
    bin_data = [] # 定义一个空的list
    i = 0
    for i in range(0, len_s): # 循环将解析出来的字节填充到list中
        chs = input_data[2*i : 2*i + 2]
        num = int(chs, 16)
        bin_data.append(num)
    return bin_data

def write_bin_file(filename, list_dec):
    with open(filename, 'wb') as fp:
        for x in list_dec:
            a = struct.pack('B', x)
            fp.write(a)

def copy_proto_file(proto_file):
    cmd = 'cp ' + proto_file + ' ./'
    os.system(cmd)

def rm_proto_file(proto_file):
    proto = proto_file.split('/')[len(proto_file.split('/')) - 1]
    cmd = 'rm ' + proto
    os.system(cmd)

def decode(input_file, msg_type, proto_file, output_file):
    hex_data = get_hex_data(input_file)
    bin_data = get_bin_data(hex_data)
    copy_proto_file(proto_file)
    (shortname, extension) = os.path.splitext(input_file) # 去掉.txt后缀的文件名
    bin_file = shortname + '.bin'
    write_bin_file(bin_file, bin_data)

    proto = proto_file.split('/')[len(proto_file.split('/')) - 1]
    cmd = 'cat ' + bin_file + ' | protoc --decode=' + msg_type + ' ' + proto + '>' + output_file
    print cmd
    os.system(cmd)

    os.system('rm ' + proto)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', default='input/input.txt', help='The input file for the hex stream')
    parser.add_argument('-m', '--msg_type', default='Test1', help='The message type to be decoded')
    parser.add_argument('-p', '--proto_file', default='input/Test1.proto', help='The message type must be defined in PROTO_FILE or their imports.')
    parser.add_argument('-o', '--output_file', default='output/output.txt', help='The output file for the parsed pb message')
    args = parser.parse_args()
    input_file = args.input_file
    msg_type = args.msg_type
    proto_file = args.proto_file
    output_file = args.output_file
    decode(input_file, msg_type, proto_file, output_file)

    os.system('cat ' + output_file)

