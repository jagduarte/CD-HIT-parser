#!/usr/bin/env python

import argparse
import os
from itertools import groupby
import json
import csv

parser = argparse.ArgumentParser(description='CD-hit cluster output to json')

parser.add_argument('-c', '--cluster', metavar='.clstr file', dest='cluster', type=str,
                    help='The .clstr file with cluster information.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v','--csv',action='store_true',help='Convert the json output to csv')
args = parser.parse_args()

def clstr_parser():
    cf, cd = open(args.cluster), {}

    cg = (x[1] for x in groupby(cf, key=lambda line: line[0] == '>'))
    for c in cg:
        clust_id = c.__next__()[1:].strip()
        clust_seq = [s.split('>')[1].split('...')[0] for s in cg.__next__()]
        cd[clust_id] = clust_seq
    return cd

def main():
    cd = clstr_parser()
    with open(str(args.cluster)+'.json','w') as j:
        json.dump(cd,j)
    if args.csv:
        with open(str(args.cluster)+'.csv','w') as f:
            w = csv.writer(f)
            w.writerows(cd.items())

if __name__ == '__main__':
    main()
