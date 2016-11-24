import logging
import math

from Context import Context
from Model import Model
from BaseModel import BaseModel

class PPMC(object):

    def __init__(self, order, m=None):
        self.order = order
        if (not m):
            self.models = [BaseModel()]
            for i in xrange(0, order+1):
                self.models.append(Model(i))
        else:
            self.models = m

    def compress(self, text, log_file='PPMC.log'):
        #logging.basicConfig(filename=log_file,level=logging.DEBUG)
        text = text.lower()
        interval = (0,1)
        try:
            for pos in xrange(0, len(text)):
                compressed = False
                modelNum = self.order+1
                while not compressed:
                    compression = self.models[modelNum].compress(text, pos, [], interval)
                    compressed = compression[0]
                    interval = compression[1]
                    modelNum -= 1
            #logging.info("FINISHED RUNNING PPMC. RETURNED INTERVAL:" +"("+str(interval[0])+","+str(interval[1])+")")
        except Exception,e:
            logging.exception(str(e))
        return self.__binary(interval)

    def __binary(self, interval):
        in_interval = False
        binary_str = "0."
        number = 0
        i = -1
        while not in_interval:
            n = math.pow(2,i)
            if (interval[0] <= n+number <= interval[1]):
                in_interval = True
            if (n+number <= interval[1]):
                number += n
                binary_str += "1"
            else:
                binary_str += "0"
            i -= 1
        return binary_str

    def models(self):
        return self.models
