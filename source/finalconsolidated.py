
#----------------------------------FINAL SCRIPT---------------
#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import string
import operator

file1 = csv.reader(open("/data/Projects/Adhoc/FuzzyMatching/output/outputfile1.csv", "rb")) #raw companies
file2 = csv.reader(open('/data/Projects/Adhoc/FuzzyMatching/output/cleaning.csv','rb')) # states companies
file3 = csv.reader(open('/data/Projects/Adhoc/FuzzyMatching/output/consolidated_matches_2.csv','rb')) #matches
file4 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/finaldata_2.csv','wb'))

ccid = {} # state clean companies id dict 
rccid = {} #raw clean companies id dict

for line in file2:
	srid = line[2]
	compnyname = line[1]
	corid = line[0]
	if srid in ccid:
		pass
	else:
		ccid[srid] = {'Corpid':str(corid) ,'Company Name': str(compnyname)}
ccid['SrIDNo'] = {'Corpid':str('') ,'Company Name': str('')}
for line in file3:
	rawid = line[0]
	score1 = line[2]
	score2 = line[5]
	score3 = line[8]
	statesid1 = line[4]
	statesid2 = line[7]
	statesid3 = line[10]

	if rawid in rccid:
		pass
	else:
		rccid[rawid] = {'score1':str(score1) ,'sccid1': str(statesid1), 'score2':str(score2) ,'sccid2': str(statesid2), 'score3':str(score3) ,'sccid3': str(statesid3)}

header = True
for line in file1:
	if header:
		file4.writerow(['Raw_Name','Raw_company_ID','Raw_freq','Score1','States_corp_ID1','States_Comp_Name1','Score2','States_corp_ID2','States_Comp_Name2','Score3','States_corp_ID3','States_Comp_Name3'])	
		header = False
		continue
	cleancomid = line[4]
	rawname = line[1]
	rawcompid = line[0]
	rawfreq = line[2]
	if cleancomid in rccid:
		score_dict = rccid[cleancomid]
		#print score_dict
		file4.writerow([rawname ,rawcompid , rawfreq , score_dict['score1']
			, ccid[score_dict['sccid1']]['Corpid'], ccid[score_dict['sccid1']]['Company Name'], score_dict['score2']
			, ccid[score_dict['sccid2']]['Corpid'], ccid[score_dict['sccid2']]['Company Name'], score_dict['score3']
			, ccid[score_dict['sccid3']]['Corpid'], ccid[score_dict['sccid3']]['Company Name']])
	else:
		continue