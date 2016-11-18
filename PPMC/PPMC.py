import logging
from Context import Context
from Model import Model
from BaseModel import BaseModel

def ppmc(text, order, log_file='PPMC.log'):
    logging.basicConfig(filename=log_file,level=logging.DEBUG)
    text = text.lower()
    interval = (0,1)
    models = [BaseModel()]
    try:
        for i in xrange(0, order+1):
            models.append(Model(i))
        for pos in xrange(0, len(text)):
            compressed = False
            modelNum = order+1
            while not compressed:
                compression = models[modelNum].compress(text, pos, [], interval)
                compressed = compression[0]
                interval = compression[1]
                modelNum -= 1
        logging.info("FINISHED RUNNING PPMC. RETURNED INTERVAL:" +"("+str(interval[0])+","+str(interval[1])+")")
    except Exception,e:
        logging.exception(str(e))
    return interval

FIVE_STARS_TEXT = "i got them in a very timely manner and they're all very large and green. there seems to be an inordinate amount of the seeds e out a weird beige color, but it still tastes great and is a much better deal than any of the indian markets in town. cheers to frontier."
ONE_STAR_TEXT = "check out the sugar content before you buy!  27 grams/box - the same amount that's in a 12 oz. can of coke!  this is ridiculously high for something that you think is going to be healthy!"
TEST = "ZZZZZZZZZZZZZZZZZZZZZZWWWWWWASDSADSXWWWWWWYYYZZZZz"

def main():
    print "PPMC 5 stars review:" + str(ppmc(FIVE_STARS_TEXT,4,'PPMC_5.log'))
    print "PPMC 1 star review:" + str(ppmc(ONE_STAR_TEXT,4,'PPMC_1.log'))
    print "PPMC 5 stars review:" + str(ppmc(TEST,4,'TEST.log'))

main()
