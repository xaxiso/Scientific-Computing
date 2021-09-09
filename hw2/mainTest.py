import numpy as np
from scipy import optimize
import math
import statistics as stat
import sys

def circleFitByDss(data):
	def f(x):
		s = 0
		for i in range(len(data[0])):
			# total = total + (math.sqrt((data[0][i]-a)**2+(data[1][i]-b)**2))
			# r = total/(i+1)
			s += abs(math.sqrt((data[0][i]-x[0])**2+(data[1][i]-x[1])**2)-x[2])
		return s

	a = stat.mean(data[0])
	b = stat.mean(data[1])

	total = 0
	for i in range(len(data[0])):
		total += (math.sqrt((data[0][i]-a)**2+(data[1][i]-b)**2))
		# f(a, b, total)
		# x0 = [stat.mean(data[0]), stat.mean(data[1]), math.sqrt((k-stat.mean(data[0]))**2+(h-stat.mean(data[1]))**2)]
	
	r = total/(len(data[0]))

	# print(a, b, r)
	x0 = [a, b, r]

	# for i in range(len(data[0])):
	opt = optimize.fmin(f, x0, disp=False) #inside arg is a guess, not what you're calculating
	return opt

def CircleFitting():
	def Load_Coordinates():
		data = [[float(val) for val in input().split()] for i in range(2)]
		return data

	for _ in range(5):
		data = Load_Coordinates()
		a, b, r = circleFitByDss(data)
		print('{} {} {}'.format(a, b, r))

if __name__ == '__main__':
	CircleFitting()