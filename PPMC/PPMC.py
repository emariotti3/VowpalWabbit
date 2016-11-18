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

FIVE_STARS_TEXT = "i got them in a very timely manner and they re all very large and green. there seems to be an inordinate amount of the seeds e out a weird beige color, but it still tastes great and is a much better deal than any of the indian markets in town. cheers to frontier."
ONE_STAR_TEXT = "check out the sugar content before you buy!  27 grams/box - the same amount that's in a 12 oz. can of coke!  this is ridiculously high for something that you think is going to be healthy!"
#TEST = "ZZZZZZZZZZZZZZZZZZZZZZWWWWWWASDSADSXWWWWWWYYYZZZZz"
ANOTHER_FIVE_STAR = "i drink iron goddess oolong pretty often, it is actually my favorite tea and i have a yixing teapot dedicated to it.  the last batch of ig oolong i ordered did not satisfy as much as this has, and if memory serves it might have been more expensive.  when you order this tea you get a seal-able pouch that contains more than enough oolong to get you through a few months if you are a daily drinker like me.  the tea has a toasty flavor and is not particularly astringent.  the tea is very pleasant and you get a great deal of it for your money."
ANOTHER_ONE_STAR = "this is one of the worse tasting soups i've ever eaten. i hated it, and now i have a full case.  it tastes bitter to me, and my husband wouldn't even try it.  only my cat was trying to reach it on the counter!"

def main():
    #print "PPMC first 5 stars review:" + str(ppmc(FIVE_STARS_TEXT,4,'PPMC_5.log'))
    #print "PPMC second 5 stars review:" + str(ppmc(ANOTHER_FIVE_STAR,4,'PPMC_5(2).log'))
    #print "PPMC first 1 star review:" + str(ppmc(ONE_STAR_TEXT,4,'PPMC_1.log'))
    print "PPMC second 1 star review:" + str(ppmc(ANOTHER_ONE_STAR,4,'PPMC_1(2).log'))

main()
