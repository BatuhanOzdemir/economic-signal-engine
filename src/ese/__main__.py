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
	group = parser.add_mutually_exclusive_group(required=False)
	group.add_argument("--help",help="Lists the commands")
	subparsers = parser.add_subparsers(dest="command",help="Available commands")

	#validate
	val_parser = subparsers.add_parser("--validate",help="Validate configs and show errors")
	val_parser.add_argument("--help",help="Not yet implemented")
	val_parser.set_defaults(func=handle_validate(args))

	#ingest
	ing_parser = subparsers.add_parser("--ingest",help="Ingest time series from provider")
	ing_parser.add_argument("--help",help="Not yet implemented")
	ing_parser.set_defaults(func=handle_ingest(args))

	#compute
	comp_parser = subparsers.add_parser("--compute",help="Compute metrics and store results")
	comp_parser.add_argument("--help",help="Not yet implemented")
	comp_parser.set_defaults(func=handle_compute(args))

	#signal
	sig_parser = subparsers.add_parser("--signal",help="Evaluate rules and emit signals")
	sig_parser.add_argument("--help",help="Not yet implemented")
	sig_parser.set_defaults(func=handle_signal(args))

	#report
	rep_parser = subparsers.add_parser("--report",help="Export report (md/json)")
	rep_parser.add_argument("--help",help="Not yet implemented")
	rep_parser.set_defaults(func=handle_report(args))

	#run
	run_parser = subparsers.add_parser("--run",help="Run end-to-end pipeline")
	run_parser.add_argument("--help",help="Not yet implemented")
	run_parser.set_defaults(func=handle_run(args))

	args = parser.parse_args()

if __name__ == "__main__":
	main()
