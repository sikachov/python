__author__ = 'Sikachov Evgeny'

import os

class TreeOfDirs(object):
    def __init__(self,file):
        try:
            inp=open(file,'r')
        except IOError:
            print "No such file or directory: "+file

        self.file=open(file,'r')
        line_path=self.file.readline()
        arr=line_path.split('=')
        b=arr[1].split("\n")
        self.root_path=b[0]
        line_mask=self.file.readline()
        line_arr=line_mask.split('=')
        l=line_arr[1].split("\n")
        self.mask=l[0]

    def BuildTree(self,root_path='/',mask='',result_file_path='output.txt'):
        string=[]
        count=0
        files=os.listdir(root_path)
        sort=filter(lambda x: x.endswith(mask), files)
        out=open(result_file_path,'w')
        for path,dirs,files in os.walk(root_path):
            sort=filter(lambda x: x.endswith(mask), files)
            for i in sort:
                string.append(path+'/'+str(i))
                count+=1
        out.write("was founded "+str(count)+" files with "+mask+" during "
                "searching procedure\n")
        for i in string:
            out.write(i)
            out.write('\n')
        return 0



a=TreeOfDirs('input.txt')
a.BuildTree(a.root_path,a.mask)
