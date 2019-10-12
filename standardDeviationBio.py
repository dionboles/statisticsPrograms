import math 

def standardDeviationBio(meanNumberOFTrial,Probabity,roundTo):
	return round(math.sqrt(meanNumberOFTrial*Probabity*(1-Probabity)),roundTo)

print("Standard Deviation Bimonial {}".format(standardDeviationBio(500, 0.45,1)))