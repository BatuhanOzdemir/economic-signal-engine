import requests
from pathlib import Path
import yaml
import sys
import pandas as pd
import json

# reading the config files
currentFile = Path(__file__).resolve()
projectPath = currentFile.parents[3]
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
	request = requests.Session()
	params = param_generator(params)
	response = request.get(url+params, headers={"key":"8lqJtipjux"})  #API key is harcoded here but will later be stored in an enviroment variable
	response_raw =json.loads(response.text)
	response_df = pd.DataFrame(response_raw)
	request.close()
	return response_df


def listCategoriesTCMB():
	main_categories = make_request("https://evds2.tcmb.gov.tr/service/evds/categories/",params={"type":"json"})
	main_categories_raw = json.loads(main_categories)
	main_categories_df = pd.DataFrame(main_categories_raw)
	return main_categories_df

def listSubcategoriesTCMB(main_category):
	if main_category == "":
		params = {"mode":2, "code":"", "type":"json"}
		print("All subcategories are returned.")
	else:
		params = {"mode": 2, "code":main_category, "type": "json"}
	sub_categories = make_request("https://evds2.tcmb.gov.tr/service/evds/datagroups/",params=params)
	sub_categories_raw = json.loads(sub_categories)
	sub_categories_df = pd.DataFrame(sub_categories_raw)
	return sub_categories_df

def listSeriesTCMB(subcategory_code):
	series = make_request('https://evds2.tcmb.gov.tr/service/evds/serieList/',params={"type":"json","code":subcategory_code})
	series_raw = json.loads(series)
	series_df = pd.DataFrame(series_raw)
	return series_df



def handle_ingest(args):

	# command line arguments
	source = args.source
	series = args.series
	startdate = args.startdate
	enddate = args.enddate
	type = args.type if args.type is not None else "json"
	aggregation = args.aggregation if args.aggregation else ""
	formulas = args.formulas if args.formulas else ""
	frequency = args.frequency if args.frequency else ""
	listCategories = args.listCategories
	listSubcategories = args.listSubcategories
	listSeries = args.listSeries


	if check_sources(source):
		print(source + " kaynağına bağlanılıyor...")
	source_link = get_the_link(source)


	if listCategories != None:
		if listCategories.lower() == "true":
			categories = listCategoriesTCMB()
			print(categories.to_string())


	if listSubcategories != None:
		subcategories = listSubcategoriesTCMB(listSubcategories)
		print(subcategories)

	if listSeries != None:
		series = listSeriesTCMB(listSeries)
		print(series.to_string())


	params = {"series":series,
	          "startDate":startdate,
	          "endDate":enddate,
	          "type":type,
	          "aggregation":aggregation,
	          "formulas":formulas,
	          "frequency":frequency}

	result = make_request(source_link, params)
	print(result.to_string())

























