This is the readme.txt file in example code for HW02 of Scientific ComputingaddAndMax

Your submission (you only need to submit one of the following):
	Python: circleFitByDss.py
	Matlab: circleFitByDss.m

Example input/output files:
	input.txt: input file
	output.standard_python.txt: output file (the correct answer returned by Python)
	output.standard_matlab.txt: output file (the correct answer returned by MATLAB)

Input/output file format:
	Input:
		Each two-row is a set of 2D points, with the first row is X coordinates and the second row is Y coordinates.
		For each two-row, you need to generate a set of [a, b, r]
		For instance, "input.txt" has 20 rows, indicating there are 10 sets of 2D points, and you need to output 10 sets of answers.
	Output:
		A matrix of numbers, with each row being an answer to a set of 2D points.

Example main program to run the test:
	Python: mainTest.py, with the following command to run it.
		python mainTest.py < input.txt > output.python.txt
	Matlab: mainText.m, with the following command (within matlab) to run it.
		mainText input.txt output.matlab.txt

Standard program for MATLAB
	circleFitByDssSP.p is a standard program that can be invoked just like an M file in MATLAB to check against your submission of "circleFitByDss.m".
	In particular, if you type "circleFitByDssSP(data, 1), the program will show the dataset together with the initial/final circles for fitting.

Extra examples for Python
	Here are some more examples for DSS in Python: dss*.py

Hints:
	Python: You may want to use scipy.optimize.fmin to invoke DSS.
	Matlab: You may want to use fminsearch to invoke DSS.
