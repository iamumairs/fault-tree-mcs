#!/usr/bin/env python3
import os
import cutsets


"""
================================================================================
                                Some Examples

- Fault Tree can be given as a CSV file (see toy.csv)
- Fault Tree can be define as follows:

simple_ft = [("TOP", "Or", ["E1", "E2"]),
      ("E1", "Or", ["a", "b"]),
      ("E2", "And", ["c", "d"])]

NOTE: "Or" and "And" should use capitalized first letter

================================================================================
"""

""" Get the name of all fault trees given as .csv files"""

applications = list(filter(lambda x: '.csv' in x, os.listdir('.')))

cs_header = """
================================================================================
                                 Minimal Cutsets
================================================================================
"""
def comput_mcs():
    for ft in applications:
        fault_tree = cutsets.get_ft(ft)
        cs = cutsets.mocus(fault_tree)
        with open(ft[:-4] + '.out',"w") as outfile:
            outfile.write(cs_header)
            for m in cs:
                outfile.write(str(m) + '\n')

comput_mcs()
