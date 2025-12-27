import sys
import argparse


def handle_validate(args):
	print("Validate")


def handle_ingest(args):
	print("Ingest")


def handle_compute(args):
	print("Compute")


def handle_signal(args):
	print("Signal")


def handle_report(args):
	print("report")


def handle_run(args):
	print("Run")


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
		args.func(args)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
