import argparse
import os

def merge_jsonl(directory, output_name):
	jsonl_files = [file for file in os.listdir(directory) if file.endswith(".jsonl")]

	with open(directory + "/" + output_name, "w") as f1:
		for file in jsonl_files:
			with open(directory + "/" + file, "r") as f2:
				lines = f2.readlines()
				if len(lines) != 0: # make sure array is not empty
					f1.write(lines[0] + "\n")

parser = argparse.ArgumentParser(description = "concatenate jsonl files")

parser.add_argument("-d", help = "directory where the jsonl files are stored")
parser.add_argument("-o", help = "name of the output file")

args = parser.parse_args()

merge_jsonl(args.d, args.o)