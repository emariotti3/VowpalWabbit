import logging
from Context import Context
from Model import Model
from BaseModel import BaseModel

class PPMC(object):

    def __init__(self, order, m):
        self.order = order
        if (not m):
            self.models = [BaseModel()]
            for i in xrange(0, order+1):
                models.append(Model(i))
        else:
            self.models = m

    def compress(text, log_file='PPMC.log'):
        logging.basicConfig(filename=log_file,level=logging.DEBUG)
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
            logging.info("FINISHED RUNNING PPMC. RETURNED INTERVAL:" +"("+str(interval[0])+","+str(interval[1])+")")
        except Exception,e:
            logging.exception(str(e))
        return __binary(interval)

    def __binary(interval):
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


FIVE_STARS_TEXT = "i got them in a very timely manner and they re all very large and green. there seems to be an inordinate amount of the seeds e out a weird beige color, but it still tastes great and is a much better deal than any of the indian markets in town. cheers to frontier."
ONE_STAR_TEXT = "check out the sugar content before you buy!  27 grams/box - the same amount that's in a 12 oz. can of coke!  this is ridiculously high for something that you think is going to be healthy!"
TEST = "ZZZZZZZZZZZZZZZZZZZZZZWWWWWWASDSADSXWWWWWWYYYZZZZz"
ANOTHER_FIVE_STAR = "i drink iron goddess oolong pretty often, it is actually my favorite tea and i have a yixing teapot dedicated to it.  the last batch of ig oolong i ordered did not satisfy as much as this has, and if memory serves it might have been more expensive.  when you order this tea you get a seal-able pouch that contains more than enough oolong to get you through a few months if you are a daily drinker like me.  the tea has a toasty flavor and is not particularly astringent.  the tea is very pleasant and you get a great deal of it for your money."
ANOTHER_ONE_STAR = "this is one of the worse tasting soups i've ever eaten. i hated it, and now i have a full case.  it tastes bitter to me, and my husband wouldn't even try it.  only my cat was trying to reach it on the counter!"
TWO_STAR_REVIEW = "mccann's steel cut oatmeal is the perfect breakfast for people in a hurry.  all you do is put 1/2 cup of oats in a little crockpot with 2 cups of boiling water before you go to bed, then an hour before i get up the crockpot starts on high on a timer so when i get out of the shower the oatmeal is ready to go.  just mix in some blueberries, raisins, craisins, dates, nuts or whatever you want and eat."

def main():
    p = PPMC(4)
    #print "PPMC first 5 stars review:" + str(p.compress(FIVE_STARS_TEXT,4,'PPMC_5.log'))
    #print "PPMC second 5 stars review:" + str(p.compress(ANOTHER_FIVE_STAR,4,'PPMC_5(2).log'))
    #print "PPMC first 1 star review:" + str(p.compress(ONE_STAR_TEXT,4,'PPMC_1.log'))
    #print "PPMC second 1 star review:" + str(p.compress(ANOTHER_ONE_STAR,4,'PPMC_1(2).log'))
    print "PPMC first 2 star review:" + str(p.compress(TWO_STAR_REVIEW,4,'PPMC_2.log'))
    #print "PPMC TEST:" + str(p.compress(TEST,4,'TEST.log'))
main()
