#!/usr/bin/python

from subprocess import call
import random
import datetime


## Can probably do an all purpose func here just pass list and count

def logger(message="message_default"):
	ts = str(datetime.datetime.now())
	log = open('radio.log','a')
	msg = ts + " : " + message + "\n"
	print(msg)
	log.write(msg)
	log.close()


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getProgram(f="master.lst"):
	flen = file_len(f)
	logger("Loading show list from :" + f)
	r = random.randrange(1,flen -1)
	ttl = 0
	shows = open(f,'r')
	for show in shows:
	    # logger("Playing " + show + " from " + str(f))		
	    ttl = ttl + 1
	    if ttl == r:
		show_url = show
		logger("Playing " + show + " from " + str(f))
		shows.close()
		break
	return show_url
		
	


ttl=1
t=0
logger("Radio Station Initializing")
while(ttl<500):
	print("Starting Radio")
	logger("loading programs iteration: " + str(ttl))
	ttl = ttl + 1
	call(["pradio",getProgram("commercials.lst")])
	#call(["pradio",getProgram("lists/moviePreviews.lst")])
	call(["pradio",getProgram("commercials.lst")])
	call(["pradio",getProgram("lists/master.lst")])
	call(["pradio",getProgram("commercials.lst")])
	call(["pradio",getProgram("lists/news.lst")])
	call(["pradio",getProgram("commercials.lst")])
	# call(["pradio",getProgram("lists/moviePreviews.lst")])






