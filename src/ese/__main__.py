import sys
import argparse
from ese.cli.validate import handle_validate
from ese.cli.ingest import handle_ingest
from ese.cli.compute import handle_compute
from ese.cli.signal import handle_signal
from ese.cli.report import handle_report
from ese.cli.run  import handle_run


handle_validate = handle_validate

handle_ingest = handle_ingest

handle_compute = handle_compute

handle_signal = handle_signal

handle_report = handle_report

handle_run = handle_run



def main():
	args = sys.argv[1:]

	parser = argparse.ArgumentParser(prog="ese", usage='%(prog)s [options]')
	subparsers = parser.add_subparsers(dest="command",help="Available commands")

	#validate
	val_parser = subparsers.add_parser("validate",help="Validate configs and show errors")
	val_parser.set_defaults(func=handle_validate)

	#ingest
	ing_parser = subparsers.add_parser("ingest",help="Ingest time series from provider")
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
		args.func()
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
