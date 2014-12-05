#!/usr/local/bin/python

import urllib2
import sys
import os
import os.path
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


def download_file(input_file_name,output_directory):

	try:

		index_file_output_file_name = os.path.join( output_directory , "index.txt" )

		ins = open( input_file_name, "r" )
		array = []
		for line in ins:
		    array.append( line )
		ins.close()

		for index,url in enumerate(array):
			try:
				if url.strip() == '':
					continue

				file_data = urllib2.urlopen(url)
				new_file_name = 'url_' + str(index).zfill(5) + '.bin'
				new_complete_path_name = os.path.join(  output_directory , new_file_name )
				output = open(new_complete_path_name,'wb')
				output.write(file_data.read())
				output.close()

				with open(index_file_output_file_name, "a") as myfile:
					line_to_write = new_file_name + ": " + url.strip()
					print "INFO: " + line_to_write
					myfile.write( line_to_write )

			except Exception as inst:
				print "ERROR: unable to fetch url [" + url.strip() + "]:" + str(inst)


	except Exception as inst:
		print "ERROR: could not download files:" + str(inst)




def main(argv):

	url = ''
	output_dir = ''
	filter= ''
	levels = 1
	input_file= ''

	try:
		opts, args = getopt.getopt(argv,"hu:o:f:l:i:")
	except getopt.GetoptError:
		print 'link_extractor.py '
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'link_extractor.py -u <url> -o <output_dir> -f <filter> -l <recursion>'
			sys.exit()
		elif opt in ("-l","--levels"):
			levels = int(arg)	
		elif opt in ("-u", "--url"):
			url = arg			
		elif opt in ("-f", "--filter"):
			filter = arg
		elif opt in ("-o", "--output-dir"):
			output_dir = arg   
		elif opt in ("-i", "--input-file"):
			input_file = arg   						
		else:
			assert False, "unhandled option"      
	
	if url == ''  and input_file == '':
		print 'ERROR: please specify a url or input file'
		sys.exit(2)


	if url != '':
		get_page(url,filter,levels)
	else:	
		if output_dir == '':	
			download_file(input_file,os.getcwd())
		else:
			download_file(input_file,output_dir)	


	
if __name__ == "__main__":
   main(sys.argv[1:])

#url = 

