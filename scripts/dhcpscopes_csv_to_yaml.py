#!/usr/bin/env python3
 
import csv
import sys
import yaml

with open(sys.argv[1] + '.yml', "w") as my_output_file: 
     with open(sys.argv[1]) as csvfile:
          next(csvfile, None)  # skip the header
          my_output_file.write("csv_data: " + '\n')
          for row in csv.reader(csvfile):
                    my_output_file.write(" - prefix: \'" +(row[0])+ "\'\n")
                    my_output_file.write("   description: \'" +(row[4])+" "+(row[5])+ "\'\n")
                    my_output_file.write("   interface: \'" +(row[5])+ "\'\n")
                    my_output_file.write("   device: \'" +(row[4])+ "\'\n")
          my_output_file.close()
