import collections
import random
import shutil 

class file:
    fname = None
    fr = None
    fw = None
    flen = 0
    def __init__(self, fname) -> None:
        self.fname = fname

class dict(file):
    index = 0
    dict = [""]
    dictFile = None
    dictFileUsed = None
    dictBase = None  
    def __init__(self, dictFile, dictUsedFile, dictBaseFile) -> None:
        self.dictFile =     file(dictFile)
        self.dictFileUsed = file(dictUsedFile)
        self.dictBase = file(dictBaseFile)
        self.dictFile.fr = open(self.dictFile.fname, "r")
        # read dictFile length
        for x in self.dictFile.fr:
            self.dictFile.flen += 1
            self.dict.append(x)
        # if it is almost empty, copy contents of the base, so start all over again.
        if self.dictFile.flen <=2:
            shutil.copyfile(dictBaseFile, dictFile)
            # clear dictUsed
            open(dictUsedFile, 'w').close()

        self.dictFile.fr.close()

    # def __iter__(self):
    #     self.index = random.randint(0, self.dictFile.flen - 1)
    #     return self
    
    # def __next__(self):
    #     x = self.__iter__()
    #     self.move(self.index)
    #     return self.dict.pop(self.index)
    
    def nxt(self):
        self.index = random.randint(0, self.dictFile.flen - 1)
        self.move(self.index)
        return self.dict.pop(self.index)
    
    def move(self, itemInd):
        try:
            with open(self.dictFile.fname, "r") as self.dictFile.fr:
                lines = self.dictFile.fr.readlines()         
                ptr = 1
            with open(self.dictFile.fname, "w") as self.dictFile.fw:                         
                 for ln in lines:
                    if ptr != itemInd:
                        self.dictFile.fw.write(ln)
                    ptr += 1
            with open(self.dictFileUsed.fname, "a") as self.dictFileUsed.fw:
                self.dictFileUsed.fw.write(self.dict[itemInd])
        except:
            print('error I/O')
        else:
            self.dictFile.fw.close()
            self.dictFileUsed.fw.close()
            self.dictFile.fw.close()

try: 
    newWord = dict('wordeli_dict/dict.txt', "wordeli_dict/dictused.txt", "wordeli_dict/base.txt")
    print(newWord.nxt())
except:
    pass