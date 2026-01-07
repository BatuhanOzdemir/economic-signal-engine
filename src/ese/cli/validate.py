import yaml
from pathlib import Path


file_sources = Path("C:\\Users\\batuh\Desktop\economic-signal-engine\configs\sources.yaml")
file_rules = Path("C:\\Users\\batuh\Desktop\economic-signal-engine\configs\\rules.yaml")
file_schedules = Path("C:\\Users\\batuh\Desktop\economic-signal-engine\configs\schedules.yaml")


def handle_validate():

	try:
		with open(file_sources,"r",encoding="utf-8") as sources:
			sources = yaml.safe_load(sources)
			for source in sources["sources"]:
				if source in ["TCMB", "ECB", "FED"]:
					print("Source " + source + " is fine")
				else:
					return False
	except yaml.YAMLError as err:
		print("Something went wrong when opening the sources.")

	try:
		with open(file_rules,"r",encoding="utf-8") as rules:
			rules = yaml.safe_load(rules)
			for rule in rules["rules"]:
				for key in rule.keys():
					if rule[key] == "":
						return False
			print("Rules loaded successfully")
	except yaml.YAMLError as err:
		print("Something went wrong when opening the rules.")

	try:
		with open(file_schedules,"r",encoding="utf-8") as schedules:
			schedules = yaml.safe_load(schedules)
			for schedule in schedules["jobs"]:
				for key in schedule.keys():
					if schedule[key] == "":
						return False
			print("Schedules loaded successfully")
	except yaml.YAMLError as err:
		print("Something went wrong when opening the schedules.")

	print("No configuration issues found")




