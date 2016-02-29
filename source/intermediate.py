#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import csv
import string
import operator


columns = ['SRNo','Transformed_companies_name']
file1 = csv.reader(open("/data/Projects/Adhoc/FuzzyMatching/output/outfile_v1.csv", "rb"))
file2 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/outputfile2.csv','wb'))
file3 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/outputfile3.csv','wb'))

ID = 0
header = True
company_name_dict = {}
path  = '/data/Projects/Adhoc/FuzzyMatching/output/'
for line in file1:
	if header:
		file2.writerow(['SRNo','Transformed_companies_name'])	
		header = False
		continue

	Transformed_companies_name_s1 = line[1]
	ID = line[0]

	file2.writerow(line[:2])

	if Transformed_companies_name_s1 in company_name_dict:
		pass
	else:
		company_name_dict[Transformed_companies_name_s1] = {'SRNo' : str(ID)} 

company_list =  company_name_dict.keys()

for cmpny in sorted(company_list):
 	file3.writerow([company_name_dict[cmpny]['SRNo'],cmpny])

for i in range(65,91):
	flag = True
	for cmpn in sorted(company_list):
		res = str(unichr(i+32))
		# print res
		if cmpn.startswith(str(res)):
			if flag == True:
				outpath = csv.writer(open(path+'filename_raw_'+ res + '.csv','wb'),delimiter=str('\t'))
				outpath.writerow(columns)
				flag = False
			outpath.writerow([company_name_dict[cmpn]['SRNo'],cmpn])
		

flag1 = True
for i in range(1,33):
	for cmpn in sorted(company_list):
		res = str(unichr(i+32))
		if cmpn.startswith(str(res)):
			if flag1 == True:
				outpath = csv.writer(open(path+'filename_raw_'+ res + '.csv','wb'),delimiter=str('\t'))
				outpath.writerow(columns)
				flag1 = False
			# print cmpny, company_name_dict[cmpny]['SrIDNo']
			outpath.writerow([company_name_dict[cmpn]['SRNo'],cmpn])



