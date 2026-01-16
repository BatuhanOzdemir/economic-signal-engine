import requests
from pathlib import Path
import yaml
import sys
import pandas as pd
import json

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


def param_generator(params):
	param_text = ''
	for key, value in params.items():
		param_text += str(key) + "=" + str(value)
		param_text += '&'
	return param_text[:-1]

def make_request(url,params={}):
	params = param_generator(params)
	request = requests.Session()
	response = request.get(url+params, headers={"key":"8lqJtipjux"})  #API key is harcoded here but will later be stored in an enviroment variable
	request.close()
	return response.content


def listCategories():
	main_categories = make_request("https://evds2.tcmb.gov.tr/service/evds/categories/",params={"type":"json"})
	main_categories_raw = json.loads(main_categories)
	main_categories_df = pd.DataFrame(main_categories_raw)
	return main_categories_df

def listSeries(main_category):
	if main_category != "":
		params = {"mode":2, "code":main_category, "type":"json"}
	else:
		print("Please enter a valid category")
	sub_categories = make_request("https://evds2.tcmb.gov.tr/service/evds/datagroups/",params=params)
	sub_categories_raw = json.loads(sub_categories)
	sub_categories_df = pd.DataFrame(sub_categories_raw)
	return sub_categories_df


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
























