#!/usr/bin/env python3
 
import csv
import sys
import yaml

with open(sys.argv[1] + '.yml', "w") as my_output_file: 
     with open(sys.argv[1]) as csvfile:
          next(csvfile, None)  # skip the header
          my_output_file.write("csv_data: " + '\n')
          for row in csv.reader(csvfile):
                    my_output_file.write(" - subnet: \'" +(row[0])+ "\'\n")
                    my_output_file.write("   primdpicint: \'" +(row[1])+ "\'\n")
                    my_output_file.write("   backdpicint: \'" +(row[2])+ "\'\n")
                    my_output_file.write("   vrf: \'" +(row[3])+ "\'\n")
                    my_output_file.write("   cinint: \'" +(row[4])+ "\'\n")
                    my_output_file.write("   primarydevice: \'" +(row[5])+ "\'\n")
                    my_output_file.write("   backupdevice: \'" +(row[6])+ "\'\n")
          my_output_file.close()
