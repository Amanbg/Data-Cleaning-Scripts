#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, re
import string
import operator


file1 = csv.reader(open("/data/Projects/Adhoc/FuzzyMatching/Input/customjobcompanies_v2.csv", "rb"))
file2 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/outputfile1.csv','wb'))

columns = ['SRNo','Transformed_companies_name','Count']
file3 = csv.writer(open('/data/Projects/Adhoc/FuzzyMatching/output/outfile.csv', 'wb'))
file3.writerow(columns)

def transformed(filearg):
	filearg = str(''.join([i if ord(i) < 128 else ' ' for i in filearg]))
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
	id = 1
	header = True
	company_name_dict = {}
	srid = 0
	for line in file1:

		if header:
			file2.writerow(['ID', 'Company Name', 'Freq','Transformed_companies_name', 'SRNo'])
			header = False
			continue

		if len(line) == 0:
			continue
		

		count = 0 

		ID = 'ID' + str(id)
		try:
			while(count < 4):
				Transformed_companies_name = transformed(line[0])

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
				 	 
				for words in badwords:
					if Transformed_companies_name.endswith(words):
						Transformed_companies_name = Transformed_companies_name.replace(str(words),' ')

				Transformed_companies_name = re.sub('[\s]+([12][90][0-9]{2})[\s.]+|$',' ',Transformed_companies_name)
				count += 1

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
				company_name_dict[Transformed_companies_name_s1]['Count'] += int(float(line[1]))
			else:
				srid += 1
				company_name_dict[Transformed_companies_name_s1] = {'SRNo' : 'SRNo' + str(srid), 'Count':int(float(line[1]))}




			file2.writerow([ID] + line[:2] + [Transformed_companies_name_s1, company_name_dict[Transformed_companies_name_s1]['SRNo']])

			id += 1
						
		except: 
			continue

sorted_dict = sorted(company_name_dict.items(), key=operator.itemgetter(1),reverse=True)

for key,value in sorted_dict:
	file3.writerow([company_name_dict[key]['SRNo'], key, company_name_dict[key]['Count']])			
	
