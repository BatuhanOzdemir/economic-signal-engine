import yaml
import sys
from pathlib import Path


current_file = Path(__file__).resolve()

project_dir = current_file.parents[3]

file_sources = Path(project_dir, "configs", "sources.yaml")
file_rules = Path(project_dir, "configs", "rules.yaml")
file_schedules = Path(project_dir, "configs", "schedules.yaml")


def handle_validate(args):

	try:
		with open(file_sources,"r",encoding="utf-8") as sources:
			sources = yaml.safe_load(sources)
			for source in sources["sources"]:
				if sources["sources"][source] != "":
					print("Source " + source + " is fine")
				else:
					print("Error: Source name or link is wrong or incomplete")
					return sys.exit(1)
	except yaml.YAMLError as err:
		print("Something went wrong when opening the sources.")

	try:
		with open(file_rules,"r",encoding="utf-8") as rules:
			rules = yaml.safe_load(rules)
			for rule in rules["rules"]:
				for key in rule.keys():
					if rule[key] == "":
						print("One or more features of a rule is missing")
						return sys.exit(1)
			print("Rules loaded successfully")
	except yaml.YAMLError as err:
		print("Something went wrong when opening the rules.")

	try:
		with open(file_schedules,"r",encoding="utf-8") as schedules:
			schedules = yaml.safe_load(schedules)
			for schedule in schedules["jobs"]:
				for key in schedule.keys():
					if schedule[key] == "":
						print("Jobs are  fully defined")
						return sys.exit(1)
			print("Schedules loaded successfully")
	except yaml.YAMLError as err:
		print("Something went wrong when opening the schedules.")

	print("No configuration issues found")




