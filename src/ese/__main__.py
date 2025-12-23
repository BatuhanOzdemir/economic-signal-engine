import sys
import argparse
import getopt

args = sys.argv[1:]
short_options = "vicsrrh:"
long_options = ["validate","ingest","compute","signal","report","run","help"]

try:
	arguments, values = getopt.getopt(args,short_options,long_options)
	for currentArg, currentVal in arguments:
		if currentArg in ("-h","--help"):
			print("validate: Checking the configuration\n"
			      "ingest: Pulling data from the source\n"
			      "compute: Calculating the metrics\n"
			      "signal: Produce the signal based on configurations\n"
			      "repot: Produces the report in the desired format\n"
			      "run: Run end to end")

		if currentArg in ("-v","--validate"):
			print("Not yet implemented")
		if currentArg in ("-i", "--ingest"):
			print("NNot yet implemented")
		if currentArg in ("-c", "--compute"):
			print("Not yet implemented")
		if currentArg in ("-s", "--signal"):
			print("Not yet implemented")
		if currentArg in ("-report", "--report"):
			print("Not yet implemented")
		if currentArg in ("-r", "--run"):
			print("Not yet implemented")

except getopt.error as err:
	print(str(err))

