#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, re
import string
import operator


def transformed(filearg):
	# print filearg
	filearg = filearg.lower()
	filearg = str(''.join([i if ord(i) < 128 else ' ' for i in filearg]))
	filearg = filearg.replace('tata consultancy services','tcs')
	filearg = filearg.replace('hewlett packard','hp')
	filearg = filearg.replace('larsen and toubro','l and t')
	filearg = filearg.replace('private limited', ' ')
	filearg = filearg.replace('p(limited)',' ')
	filearg = filearg.replace('plimited',' ')
	filearg = filearg.replace('(i)',' ')
	filearg = filearg.replace('{p}','private')
	filearg = filearg.replace('(p).','private')
	filearg = filearg.replace('( i )',' ')
	filearg = filearg.replace('lrd.','limited')
	filearg = filearg.replace('(pvt)ltd','private limited')
	filearg = filearg.replace(' ld.','limited')
	filearg = filearg.replace('p.ltd', 'private limited')
	filearg = filearg.replace('p ltd','private limited')
	filearg = filearg.replace('pvt.ltd','private limited')
	filearg = filearg.replace('co india','company india')
	filearg = filearg.replace('co. india','company india')
	filearg = filearg.replace('co ind','company india')
	filearg = filearg.replace('corp ltd','corporation limited')
	filearg = filearg.replace('co.ltd','company limited')
	filearg = filearg.replace('co.ltd.','company limited')
	filearg = filearg.replace('co ltd','company limited')
	filearg = filearg.replace('co llc','company limited liability company')
	filearg = filearg.replace(' lted',' limited')
	filearg = filearg.replace('l.l.c','llc')
	filearg = filearg.replace('limited liability company','llc')
	filearg = filearg.replace('ltd.','limited')
	filearg = filearg.replace('ltd','limited')
	filearg = filearg.replace('l.t.d','limited')
	filearg = filearg.replace(' lmtd',' limited')
	filearg = filearg.replace('limted','limited')
	filearg = filearg.replace('.ltd','limited')
	filearg = filearg.replace('pvt.','private')
	filearg = filearg.replace('pvt','private')
	filearg = filearg.replace('( p)','private')
	filearg = filearg.replace('(p)','private')
	filearg = filearg.replace('(pvt.)','private')
	filearg = filearg.replace(' inc.',' incorporated')
	filearg = filearg.replace(' co.',' company')
	filearg = filearg.replace(' org.',' organization')
	filearg = filearg.replace(',',' ')
	filearg = filearg.replace(':',' ')
	filearg = filearg.replace('--',' ')
	filearg = filearg.replace('-',' ')
	filearg = filearg.replace('@',' ')
	filearg = filearg.replace('$',' ')
	filearg = filearg.replace('`',' ')
	filearg = filearg.replace('.com',' ')
	filearg = filearg.replace('_',' ')
	filearg = filearg.replace('.',' ')
	filearg = filearg.replace('\"',' ')
	filearg = filearg.replace('\'',' ')
	filearg = filearg.replace('#',' ')
	filearg = filearg.replace(';',' ')
	filearg = filearg.replace('&',' and ')
	filearg = filearg.replace('=',' ')
	filearg = filearg.replace('?',' ')

	filearg = filearg.strip().replace('\t', ' ').replace('\r', ' ').replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')

	return filearg


def replacecompanyname(Transformed_companies_name):

	subscompany = {
		'tata consultancy services'        : 'tcs',
		'larsen and toubro'                : 'l and t',
		'hewlett packard'                  : 'hp',
		'mahindra and mahindra'            : 'm and m',
		'hindustan unilever'               : 'hul',
		'state bank of india'              : 'sbi',
		'!dea'                             : 'idea',
		'general motors'                   : 'gm',
		'oil and natural gas corporation'  : 'ongc',
		'hindustan construction company'   : 'hcc',
		'tata business support services'   : 'tbss',
		'procter and gamble'               : 'p and g',
		'indian air force'                 : 'iaf',
		'indian airforce'                  : 'iaf',
		'electronic corporation of'        : 'ecil',
		'indian institute of technology'   : 'iit',
		'indian institute of science'      : 'iisc',
		'bharat heavy electronics'         : 'bhel',
		'hindustan times'                  : 'ht',
		'royal bank of scotland'           : 'rbs',
		'lovely professional university'   : 'lpu',
		'united health group'              : 'uhg',
		'unitedhealth group'               : 'uhg',
		'bharat sanchar nigam'             : 'bsnl',
		'national information centre'      : 'nic',
	    'hdfcbank'                         : 'hdfc bank',
	    'american express'                 : 'amex',
	    'tatasky'                          : 'tata sky',
	    'bharat electronics'               : 'bel',
	    'cocacola'                         : 'coca cola',
	    'govt'                             : 'government',
	    'mc donalds'                       : 'mcdonalds',
	    'mc donald'                        : 'mcdonalds',
	    'public works department'          : 'pwd',
	    'steel authority of'			   : 'sail',
	    'national rural health mission'    : 'nrhm',
	    'make my trip'                     : 'makemytrip',
	    'national aerospace laboratories'  : 'nal',
	    'coal'                             : 'cil',
	    'punjab national bank'             : 'pnb',
	    'glaxosmithkline'                  : 'gsk',
	    'disht v'                          : 'dish tv',
	    'dish t v'                         : 'dish tv',
	    'dishtv'                           : 'dish tv',
	    'citibank'                         : 'citi bank',
	    'dr reddy s'                       : 'dr reddys',
	    'hindustan aeronautics'            : 'hal',
	    'lnt'                              : 'l and t',
	    'cognizent'                        : 'cognizant',
	    'gold s gym'                       : 'golds gym',
	    'hindustan corporation'            : 'hcl',
	    'central reserve police force'     : 'crpf',
	    'military engineering services'    : 'mes',
	    'mahindrasatyam'                   : 'mahindra satyam',
	    'indian oil corporation'           : 'ioc',
	    'tata consulting engineers'        : 'tce'

	} 
	for k in subscompany:
		Transformed_companies_name = Transformed_companies_name.replace(k,subscompany[k])


	return Transformed_companies_name

if __name__ == '__main__':
	sid = 1
	file1 = csv.reader(open('/data/Projects/Adhoc/FuzzyMatching/Input/final.csv'))
	file2 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/cleaning.csv','wb'))

	columns = ['SrIDNo','Transformed_companies_name']
	file3 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/finaloutput.csv', 'wb'))
	file3.writerow(columns)

	path = '/data/Projects/Adhoc/FuzzyMatching/output/'

	header = True
	company_name_dict = {}
	srid = 0

	for line in file1:
		
		if header:
			file2.writerow(['CORID','Company Name','SID','Transformed_companies_name'])
			header = False
			continue

		if len(line) == 0:
			continue


		count = 0

		SID = 'SID' + str(sid)

		while(count < 4):
			line[1] = line[1].lower()
			Transformed_companies_name = transformed(line[1])
			
			cities = ['/','*','lt','-',')','inc','co','.' ,',','.',',','india','(india)',
					  'coimbatore', 'mumbai','punjab','haryana','goa','new delhi','delhi','pune','maharashtra',
					  'bangalore','agra','ahmedabad','aurangabad','noida','malegaon nashik','nashik','dubai',
					  'kuala lumpur','chandigarh','chennai','perumber','kanpur','yerwada',
					  'faridabad','jalandhar','haridwar','gujarat','kerala','bareilly','ludhiana','mohali',
					  'chakan','nagpur','moradabad','jaipur','una','meerut','ghaziabad','gurgaon','gurgoan',
				      'hyderabad','noida','orissa','lucknow','bhopal','udaipur','kolkata','udaipur (raj.)','udaipur (raj.','thane']

			for city in cities:
				if (Transformed_companies_name.find('bank of india') == -1):
					if Transformed_companies_name.endswith(city):
						Transformed_companies_name = Transformed_companies_name.replace(str(city),' ').strip()
							
			badwords = ['(india) private limited','india private limited','india private',
						'(india )private limited','india limited','(india) limited','llc',
						'private limited','private .limited','privatelimited','limited','(']
				 	#count += 1 

			for words in badwords:
				if Transformed_companies_name.endswith(words):
					Transformed_companies_name = Transformed_companies_name.replace(str(words),' ')

			Transformed_companies_name = re.sub('[\s]+([12][90][0-9]{2})[\s.]+|$',' ',Transformed_companies_name)
			count += 1

		# end of while loop

		Transformed_companies_name = Transformed_companies_name.strip()

		finalstr = ''
		flag = True
		character = Transformed_companies_name.split(' ')

		for char in character:
			if len(char) == 1 and flag == True:
			 	finalstr = finalstr + char
			else:
			 	finalstr = finalstr + ' ' + char
			 	flag = False

		Transformed_companies_name = finalstr.strip()
		
		#call another function for the acronym of the company name
		Transformed_companies_name_s1 = replacecompanyname(Transformed_companies_name)

		if Transformed_companies_name_s1 in company_name_dict:
			pass
		else:
			srid += 1
			company_name_dict[Transformed_companies_name_s1] = {'SrIDNo': 'SrIDNo'+ str(srid)}
		
		# print Transformed_companies_name
		#file2.writerow(line[:2] + [SID ,Transformed_companies_name_s1])
		file2.writerow(line[:2] + [company_name_dict[Transformed_companies_name_s1]['SrIDNo'] ,Transformed_companies_name_s1])
		# sid += 1

company_list =  company_name_dict.keys()
check = 0
for cmpny in sorted(company_list):
 		file3.writerow([company_name_dict[cmpny]['SrIDNo'],cmpny])


res = 0
for i in range(65,91):
	flag = True
	for cmpn in sorted(company_list):
		res = str(unichr(i+32))
		# print res
		if cmpn.startswith(str(res)):
			if flag == True:
				outpath = csv.writer(open(path+'filename_'+ res + '.csv','wb'),delimiter=str('\t'))
				outpath.writerow(columns)
				flag = False
			outpath.writerow([company_name_dict[cmpn]['SrIDNo'],cmpn])
		

flag1 = True
for i in range(1,33):
	for cmpn in sorted(company_list):
		res = str(unichr(i+32))
		if cmpn.startswith(str(res)):
			if flag1 == True:
				outpath = csv.writer(open(path+'filename_'+ res + '.csv','wb'),delimiter=str('\t'))
				outpath.writerow(columns)
				flag1 = False
			# print cmpny, company_name_dict[cmpny]['SrIDNo']
			outpath.writerow([company_name_dict[cmpn]['SrIDNo'],cmpn])
	