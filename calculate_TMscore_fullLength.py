#!/usr/bin/python
#########################################
#
#	calculate_TMscore_fullLength.py
#
#	@Author: Sutanu
#	@Version: May 24, 2019
#   Ref: Y. Zhang, J. Skolnick, Scoring function for automated assessment of protein structure template quality, Proteins, 57: 702-710 (2004)
#
#########################################

import os
import sys
import optparse

TMscore = "/home/apps/TMscore/TMscore"


#take input arguments
parser=optparse.OptionParser()
parser.add_option('--t', dest='targetDir',
        default= '',    #default empty!
        help= 'target directory')
parser.add_option('--n', dest='nativeDir',
        default= '',    #default empty!
        help= 'netive directory')
(options,args) = parser.parse_args()
targetDir = options.targetDir
nativeDir = options.nativeDir


def tm(predictPDB,nativePDB):
    	os.system(TMscore + " " + predictPDB + " " + nativePDB + " > tmscore.txt")
    	f = open("tmscore.txt")
    	for line in f:
        	line = line.strip()
        	if line.startswith("TM-score    ="):
                	#print line 
                	line = line.split()
                	tm = line[2]
                	break
    	os.remove("tmscore.txt")
    	f.close()
    	return tm

sys.stdout.write("Targets,TM-score")

for target in os.listdir(nativeDir):
	if not target.endswith(".pdb"):
		continue
	native_target = nativeDir + target
	protein = target.split(".")[0]

	for pred in os.listdir(targetDir):
		if pred.startswith(protein):
			predictPDB = targetDir + pred
			break
	try:
		sys.stdout.write("\n" + protein + "," + tm(predictPDB,native_target))
	except:
		continue
