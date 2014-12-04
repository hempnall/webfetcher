import urllib2
#!/bin/python


import sys
import getopt
from bs4 import BeautifulSoup


def get_page(page,filter,level):

	if level == 0:
		return

	try:
		html_page = urllib2.urlopen(page)
		soup = BeautifulSoup(html_page)
		for link in soup.find_all('a'):
			the_href = link.get('href')
			if filter == '':
				print str(the_href)
			else:
				if filter in the_href:
					print str(the_href)
				else:
					get_page(the_href,filter,level - 1 )
	except:
		pass

def main(argv):

	url = ''
	output_file = ''
	filter= ''
	levels = 1

	try:
		opts, args = getopt.getopt(argv,"hu:o:f:l:")
	except getopt.GetoptError:
		print 'link_extractor.py '
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'link_extractor.py -u <url> -o <output_file> -f <filter> -l <recursion>'
			sys.exit()
		elif opt in ("-l","--levels"):
			levels = int(arg)	
		elif opt in ("-u", "--url"):
			url = arg			
		elif opt in ("-f", "--filter"):
			filter = arg
		elif opt in ("-o", "--output-file"):
			output_file = arg   
		else:
			assert False, "unhandled option"      
	
	if url == '' :
		print 'ERROR: please specify a url'
		sys.exit(2)


	
	try:
		get_page(url,filter,levels)
		

	except Exception as inst:
		print 'ERROR: unable to fetch URL: ' + str(inst)

	
if __name__ == "__main__":
   main(sys.argv[1:])

#url = 

