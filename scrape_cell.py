import sys
import argparse
if __name__ == "__main__":
	import re
	import requests
	import bs4
	parser = argparse.ArgumentParser()
	parser.add_argument("--index_url", help="e.g. https://www.cell.com/cell-metabolism/fulltext/S1550-4131(18)30735-6", type=str, default="https://www.cell.com/cell-metabolism/fulltext/S1550-4131(18)30735-6")
	parser.add_argument("--play",action='store_true',help="specifies for the audio to be played immediately- default is to not play")
	parser.add_argument('--output_file',type=str,help="if not specified- will default to title of the paper")
	parser.add_argument('--speech_rate',type=int,help="default is 220 wpm",default=220)
	parser.add_argument('--voice',type=str,help='Choose any from: Alex\nalice\nalva\namelie\nanna\ncarmit\ndamayanti\ndaniel\ndiego\nellen\nfiona\nFred\nioana\njoana\njorge\njuan\nkanya\nkaren\nkyoko\nlaura\nlekha\nluca\nluciana\nmaged\nmariska\nmei-jia\nmelina\nmilena\nmoira.premium\nmonica\nnora\npaulina\nsamantha\nsara\nsatu\nsin-ji\ntessa\nthomas\nting-ting\nveena\nVictoria\nxander\nyelda\nyuna\nyuri\nzosia\nzuzana\n',default='Alex')
	args = parser.parse_args()
	print('voice '+args.voice)
	response = requests.get(args.index_url)
	soup = bs4.BeautifulSoup(response.text,'html.parser')
	mystring = soup.find_all('div', attrs={'class': 'col-md-7 col-lg-9 article__sections'})[0].text
	#extra_string=soup.find_all('section', {'id': re.compile(r'sec')})
	# full=''
	# for i in extra_string:
	# 	full=full+i.text.encode('ascii','ignore')
	#mystring=mystring+extra_string
	header=soup.select('h1')[0].text.encode('utf8')
	def a(test_str):
		ret = ''
		skip1c = 0
		skip2c = 0
		for i in test_str:
			if i == '[':
				skip1c += 1
			elif i == ']' and skip1c > 0:
				skip1c -= 1
			elif skip1c == 0:
				ret += i
		return ret
	# def a2(test_str):
	# 	regex=re.compile('\\nGoogle Scholar\)')
	# 	ends=[]
	# 	diff=0
	# 	difs=[]
	# 	for m in regex.finditer(test_str):
	# 		ends.append(m.end())
	# 	for m in ends:
	# 		difs.append(diff)
	# 		m=m-sum(difs)
	# 		i=m
	# 		while True:
	# 			if bool(re.match('\(\D+',test_str[i-2:i])):
	# 				#if 'et al' in test_str[i-2:i+5]:
	# 				test_str=test_str[:i-2]+test_str[m:]
	# 				diff=m-i
	# 				break
	# 			else:
	# 				i-=1
	# 	return test_str
	# def a2(test_str):
	# 	regex=re.compile('\\nGoogle Scholar\)')
	# 	starts=[]
	# 	ends=[]
	# 	diff=0
	# 	ret=''
	# 	difs=[]
	# 	for m in regex.finditer(test_str):
	# 		ends.append(m.end())
	# 	for m in ends:
	# 		difs.append(diff)
	# 		m=m-sum(difs)
	# 		i=m
	# 		while True:
	# 			if bool(re.match('\(\D+',test_str[i-2:i])):
	# 				#if 'et al' in test_str[i-2:i+5]:
	# 				starts.append(i-2)
	# 				break
	# 			else:
	# 				i-=1
	# 	start=test_str[:starts[0]]
	# 	starts=starts[1:]
	# 	end=test_str[ends[-1]:]
	# 	ends=ends[:-1]
	# 	for i,j in zip(starts,ends):
	# 		ret=ret+test_str[j:i]
	# 	return start+ret+end

	x = a(mystring)
	x=re.sub(r'(?s)\(.*?Google Scholar\)','',x)
	#x=mystring
	#x=re.sub(r'([a-z])- ([a-z])', r'\1\2', x)
	#x= file.read()
	#x = re.sub(r'[-\d,]+', '', x)
	#x =re.sub(r'([^ 0-9])(\d+(?:,\d+)*)', r'\1', x)
	#x=re.sub(r'\w*\d\w*', '', x).strip()
	# x1 = re.sub('[A-Z][0-100]+', '', x)
	# x2 = re.sub('[A-Z][0-100]+', '', x1)
	# x3 = re.sub('[A-Z][0-100]+', '', x2)
	#x = re.sub(r' ,', '', x)
	x = re.sub(u'\u03b1', 'alpha', x)
	x = re.sub(u'\u03b2', 'beta', x)
	x = re.sub(u'\u025b', 'epsilon', x)
	x = re.sub(u'\u2022', '\n\n', x)
	x = re.sub(r'\xd7', 'by', x)
	x = re.sub(r'\xa0', ' ', x)
	x = re.sub(u'\u2212', ' to the minus ', x)
	x = re.sub(u'\u2013', ' to ', x)
	x = re.sub(u'\u223c', ' approximately ', x)
	x = re.sub(u'\u201c', '', x)
	x = re.sub(u'\u201d', '', x)
	x = re.sub(u'\u2014', '-', x)
	pattern="View Large\n                                            Image\n                                        Figure ViewerDownload Hi-res\n                                            image\n                                        Download (PPT)"
	x=x.replace(pattern,'')
	pattern="View Large\n                                            Image\n                                        Figure ViewerDownload Hi-res\n                                            image\n                                        Download"
	x=x.replace(pattern,'')
	Neandertal="Neandertal"
	x=x.replace(Neandertal,'Neeanderthaal')
	# x = re.sub(r'\xce\x94', ' delta ', x)
	# x = re.sub(r'\xce\xb2', ' beta ', x)
	# x = re.sub(r'\xc3\x85', ' delta ', x)
	# x = re.sub(r'\xce\xb7', ' eta ', x)
	# x = re.sub(r'\xcf\x83', ' sigma ', x)
	# x = re.sub(r'\xcb\x86', '', x)
	# x = re.sub(r'\xce\xb1', ' angstrom', x)
	# x = re.sub(r'\xce\xb6', ' zeta ', x)
	# x = re.sub(r'\xce\xb5', ' epsilon ', x)
	# x = re.sub(r'\xc2\xb1', ' plus or minus ', x)
	# x = re.sub(r'\xce\xa9', ' omega', x)
	# x = re.sub(r'\xce\xbb', ' lambda ', x)
	# x = re.sub(r'\xce\xb5', ' epsilon ', x)
	# x = re.sub(r'\xe2\x88\x88', 'epsilon', x)
	# x = re.sub(r'\xe2\x88\x91', 'sum of ', x)
	# x = re.sub(r'\xce\xba', 'kappa ', x)
	x=re.sub(r'\w+.jpg\s?','',x)
	x=re.sub(r'et al\.','et al',x)
	x=re.sub(r'\xe2\x88\xbc','approximately',x)
	x=re.sub(r'3D', 'three D',x)
	x=re.sub(r'\d+;', '',x)
	x=re.sub(r'\d+ ;', '',x)
	#x=re.sub(r'\d+,', '',x)
	#x=re.sub(r'\d+\.', '.',x)
	#x = re.sub(r'\r\d+', '', x)
	x = re.sub(r'\d+\n', '', x)
	x=re.sub(r'CpG', 'CPG',x)
	x=re.sub(r'\xe2\x88\x97','',x)

	if 'To read this article in full you will need to make a payment' in x:
		x=x[:x.find('To read this article in full you will need to make a payment')]
	else:
		x=x[:x.find('.Acknowledgments')]

	#print(x.encode('utf8'))
	if args.output_file:
		file=open(args.output_file,'w')
		file.write(str(x))
		file.close()
	else:
		file=open(header+b'.txt','w')
		file.write(str(x))
		file.close()

	if args.play:
		import pyttsx3
		engine = pyttsx3.init()
		engine.setProperty('rate', args.speech_rate)
		voices = engine.getProperty('voices')
		for j,i in enumerate(voices):
			if args.voice in str(i.id):
				break
		engine.setProperty('voice', voices[j].id)
		engine.say(x.encode('utf8'))
		engine.runAndWait()
		engine.stop()










# def strip_tags(html, invalid_tags):
#     soup = bs4.BeautifulSoup(html)
#     for tag in soup.findAll(True):
#         if tag.name in invalid_tags:
#             s = ""
#             for c in tag.contents:
#                 if not isinstance(c, NavigableString):
#                     c = strip_tags(unicode(c), invalid_tags)
#                 s += unicode(c)
#             tag.replaceWith(s)
#     return soup
