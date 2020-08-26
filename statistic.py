# -*- coding: UTF-8 -*-
import os
import argparse

class Result:
    def __init__(self, total_line = 0, comment_line = 0, blank_line = 0):
        self.total_line = total_line
        self.comment_line = comment_line
        self.blank_line  = blank_line
    def __add__(self, rhs):
        self.total_line += rhs.total_line
        self.comment_line += rhs.comment_line
        self.blank_line  += rhs.blank_line
        return self
    def printf(self):
        print "代码行数：",self.total_line
        print "注释行数:",self.comment_line,"占%0.2f%%"%(self.comment_line*100/self.total_line) 
        print "空行数:", self.blank_line, "占%0.2f%%"%(self.blank_line * 100 / self.total_line) 

 
def statistic_in_file(curr_file):
    result = Result()
    with open(curr_file, 'r') as rfile:
        lines = rfile.readlines()
        result.total_line = len(lines)
        for line in lines:
            #检查是否为注释
            if line.startswith("//"):
                result.comment_line += 1
            #检查是否为空行
            elif line =='\n':
                result.blank_line += 1
    result.printf() 
    print ''
    return result

def statistic_in_folder(path):
    result = Result()
    if os.path.isfile(path):
        if os.path.splitext(path)[1] == '.h' or os.path.splitext(path)[1] == '.cpp':
            print 'file path: ', path
            result += statistic_in_file(path)       
    else: 
        for dir in os.listdir(path):
            result += statistic_in_folder(os.path.join(path, dir))
    return result
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root_path', default='./')
    args = parser.parse_args()
    root_path = args.root_path
    result = Result()
    result += statistic_in_folder(root_path)
    print 'root path: ', root_path
    result.printf()
