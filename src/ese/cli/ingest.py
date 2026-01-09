import requests
from pathlib import Path
import yaml
import sys

# reading the config files
currentFile = Path(__file__).resolve()
projectPath = currentFile.parent[3]
fileSources = Path(projectPath, "configs", "sources.yaml")


# helper methods
def check_sources(source):

	with open(fileSources, "r", encoding="utf8") as f:
		validSources = yaml.safe_load(f)
		for sources in validSources["sources"]:
			if sources == source:
				return True
	print("Please enter a valid source")
	return sys.exit(1)


def get_the_link(source):
	with open(fileSources, "r", encoding="utf8") as f:
		validSources = yaml.safe_load(f)
		for banks in validSources["sources"]:
			if str(source) == banks:
				link = validSources["sources"][banks]
				break
	return link


def handle_ingest(args):

	# command line arguments
	source = args.source
	series = args.series
	startdate = args.startdate
	enddate = args.enddate
	type = args.type
	aggeration = args.aggeration
	formulas = args.formulas
	frequency = args.frequency

	# checking the source and assigning API link to variable
	check_sources(source)
	source_link = get_the_link(source)

	params = [series, startdate, enddate, type, aggeration, formulas, frequency]






















