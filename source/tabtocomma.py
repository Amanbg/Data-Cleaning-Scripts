#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import csv


file1 = csv.reader(open("/data/Projects/Adhoc/FuzzyMatching/Matching/Matching_chunk_x/matches-hybrid4_0", "rb"),delimiter=str('\t'))
file2 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/Matching/Matching_chunk_x/matches-hybrid4_0_x.csv','wb'),delimiter=str(','))

for line in file1:
	file2.writerow(line)
