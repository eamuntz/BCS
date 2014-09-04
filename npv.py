import math
'pair is composed of amount and time period'
def npv(pairs, rate):
	npv = 0
	for each in pairs:
		npv += each[0]/math.pow((1+rate),each[1])
	return npv

def intfind(pv, fv):
	return float(fv)/(pv-1)

def cashFlowRec(timeFrame, amount, rate):
	return

def perpPV(amount, rate):
	return (amount/rate)
	