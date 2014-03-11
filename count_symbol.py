# -*- coding: cp1251 -*-

class DistributionOfCharacters(object):
    def __init__(self, fileInputDataPath="input.txt",fileOutputDataPath="output.txt"):
        try:
            open(fileInputDataPath)
        except:
            print "File not found"

        self.ascii='''!”’(),-./:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
                   'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'''
        self.input=open(fileInputDataPath,"r")
        self.output=open(fileOutputDataPath,"w")


    def CountOfCharacters(self):
        l=[]
        k=0
        for line in self.input:
            l.append(line)
        for letter in self.ascii:
            for j in l:
                for i in j:
                    if i==letter:
                        k+=1
            print letter.decode('cp1251')+" "+str(k)
            self.output.write(letter+" "+str(k)+"\n")
            k=0



text=DistributionOfCharacters()
text.CountOfCharacters()
