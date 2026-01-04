import yaml
from pathlib import Path


file_sources = Path("C:\\Users\\batuh\Desktop\economic-signal-engine\configs\sources.yaml")
def handle_validate():
	try:
		with open(file_sources,"r",encoding="utf-8") as sources:
			sources = yaml.safe_load(sources)
			for source in sources["sources"]:
				if source in ["TCMB","ECB","FED"]:
					print("Sources are fine")
					return True
				else:
					print("Wrong Sources")
					return False

	except yaml.YAMLError as err:
		print("Ooops something went wrong.")



