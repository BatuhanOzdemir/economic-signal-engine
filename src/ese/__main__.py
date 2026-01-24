import sys
import argparse
from ese.cli.validate import handle_validate
from ese.cli.ingest import handle_ingest
from ese.cli.compute import handle_compute
from ese.cli.signal import handle_signal
from ese.cli.report import handle_report
from ese.cli.run  import handle_run


def main():
	args = sys.argv[1:]

	parser = argparse.ArgumentParser(prog="ese", usage='%(prog)s [options]')
	subparsers = parser.add_subparsers(dest="command",help="Available commands")

	#validate
	val_parser = subparsers.add_parser("validate",help="Validate configs and show errors")
	val_parser.set_defaults(func=handle_validate)

	#ingest
	ing_parser = subparsers.add_parser("ingest",help="Ingest time series from provider")
	ing_parser.add_argument("--source", default="TCMB",help="Source provider")
	ing_parser.add_argument("--series",help="Select one of the series")
	ing_parser.add_argument("--startdate",help="Enter the start date")
	ing_parser.add_argument("--enddate",help="Enter the end date")
	ing_parser.add_argument("--type", help="Select the type json, xml or csv")
	ing_parser.add_argument("--aggregation", help="Select one of the aggregation "
	                                     "Average:avg, Minimum:min, Maximum:max, Begining:first, End:last, Cumulative:sum")
	ing_parser.add_argument("--formulas", help="Select one of the following formulas "
	                                    "Default=0, Percent Change=1, Difference=2, Yearly Percentage Change=3, "
	                                    "Yearly Difference=4, Percentage Change YoY=5, Difference YoY=6, Moving Average=7"
	                                           "Moving Sum=8")
	ing_parser.add_argument("--frequency", help="Select the frequency of the time series  Daily=1, Workday=2, Weekly=3,"
	                                          "Twice a Month=4, Monthly=5, Three monthly=6, Six Monthly=7, Year=8")
	ing_parser.add_argument("--listCategories",help="Returns available categories")
	ing_parser.add_argument("--listSubcategories",help="Returns list of available subcategories, works with main category ID")
	ing_parser.add_argument("--listSeries",help="Return the series of a subgroup")

	ing_parser.set_defaults(func=handle_ingest)

	#compute
	comp_parser = subparsers.add_parser("compute",help="Compute metrics and store results")
	comp_parser.set_defaults(func=handle_compute)

	#signal
	sig_parser = subparsers.add_parser("signal",help="Evaluate rules and emit signals")
	sig_parser.set_defaults(func=handle_signal)

	#report
	rep_parser = subparsers.add_parser("report",help="Export report (md/json)")
	rep_parser.set_defaults(func=handle_report)

	#run
	run_parser = subparsers.add_parser("run",help="Run end-to-end pipeline")
	run_parser.set_defaults(func=handle_run)

	args = parser.parse_args()

	if hasattr(args,"func"):
		args.func(args)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
