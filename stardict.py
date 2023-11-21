import datetime
import os
import sys
import pystardict
from pystardict import Dictionary
import random
import trans
class mydict(Dictionary):
    k = None 
    
    def __init__(self, filename_prefix, in_memory=True):
        super().__init__(filename_prefix, in_memory)
    
    def random(self):
        self.k = list(self.keys())
        i = random.randint(0, len(self.k) - 1)
        return  self.k[i]



dicts_dir = os.path.join(os.path.dirname(__file__))
engGeoDict = mydict(os.path.join(dicts_dir, 'stardicts/eng-geo', 'eng-geo_lexicondict'))
enRuDict = mydict(os.path.join(dicts_dir, 'stardicts/stardict-eng_rus_full-2.4.2', 'eng_rus_full'))


def getFromDict():
    
    eng  = engGeoDict.random()
    geo = engGeoDict.get(eng) 
    # ru = enRuDict.dict[eng]
    transcr = trans.transctipt(geo)
    print(eng + " — " + geo + ' [' + transcr + "]")
    return eng + " — " + geo + ' [' + transcr + "]"
    # print(ru) 

#TODO save as jpg with formatted html, search for an image and make a post 

getFromDict()