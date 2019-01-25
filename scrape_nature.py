import sys
import argparse
if __name__ == "__main__":
	import re
	import requests
	import bs4

	parser = argparse.ArgumentParser()
	parser.add_argument("--index_url", help="e.g. https://www.nature.com/articles/s41586-018-0836-1", type=str, default="https://www.nature.com/articles/s41586-018-0836-1")
	parser.add_argument("--play",action='store_true',help="specifies for the audio to be played immediately- default is to not play")
	parser.add_argument('--output_file',type=str,help="if not specified- will default to title of the paper")
	parser.add_argument('--speech_rate',type=int,help="default is 220 wpm",default=220)
	parser.add_argument('--voice',type=str,help='Choose any from: Alex\nalice\nalva\namelie\nanna\ncarmit\ndamayanti\ndaniel\ndiego\nellen\nfiona\nFred\nioana\njoana\njorge\njuan\nkanya\nkaren\nkyoko\nlaura\nlekha\nluca\nluciana\nmaged\nmariska\nmei-jia\nmelina\nmilena\nmoira.premium\nmonica\nnora\npaulina\nsamantha\nsara\nsatu\nsin-ji\ntessa\nthomas\nting-ting\nveena\nVictoria\nxander\nyelda\nyuna\nyuri\nzosia\nzuzana\n',default='Alex')
	args = parser.parse_args()
	print('voice '+args.voice)

	response = requests.get(args.index_url)
	soup = bs4.BeautifulSoup(response.text,'html.parser')
	connect={}
	idx = []
	a = soup.find_all('div', attrs={'data-article-body': 'true'})[0].text
	header=soup.find(itemprop="name headline").text.encode('utf8')
	print('header '+ header)
	def remove_bracketted_content(test_str):
		ret = ''
		skip1c = 0
		skip2c = 0
		for i in test_str:
			if i == '(':
				skip1c += 1
			elif i == ')' and skip1c > 0:
				skip1c -= 1
			elif skip1c == 0:
				ret += i
		return ret


	a = remove_bracketted_content(a)
	x=re.sub(r'Pax9','Pax 9',a)
	x=re.sub(r'Pax3','Pax 3',x)
	x=re.sub(r'Suv39h','Suv 39 h',x)
	x=re.sub(r'P53','P 53',x)
	x=re.sub(r'Sox2','Sox 2',x)
	x=re.sub(r'Oct4','Oct 4',x)
	x=re.sub(r'Klf4','Klf 4',x)
	x=re.sub(r'P66a','P 66 a',x)
	x=re.sub(r'Thy1','Thy 1',x)
	x=re.sub(r'Gatad2a','Gatad 2 a',x)
	x=re.sub(r'Gatad2a','Gatad 2 a',x)
	x=re.sub(r'Mbd3','Mbd 3',x)
	x=re.sub(r'SSEA1','S SEA 1',x)
	x=re.sub(r'Chd4', 'Chd 4',x)
	x=re.sub(r'HP1','HP 1 ',x)
	x=re.sub(r'H3K9ac','H 3 Kay 9 AC',x)
	x=re.sub(r'H3K27ac','H 3 Kay 2 7 AC',x)
	x=re.sub(r'H3K9','H 3 Kay 9 ',x)
	x=re.sub(r'H4K20','H 4 Kay 20 ',x)
	x=re.sub(r'H3K4','H 3 Kay 4 ',x)
	x=re.sub(r'H3K27','H 3 Kay 2 7 ',x)
	x=re.sub(r'H4K16','H 4 Kay 16 ',x)
	x=re.sub(r'H2A','H 2 A ',x)
	x=re.sub(r'H2B','H 2 B ',x)
	x=re.sub(r'me3','ME 3',x)
	x=re.sub(r'me2','ME 2',x)
	x=re.sub(r'me1','ME 1',x)
	x=re.sub(r'H1','H 1',x)
	x=re.sub(r'H3','H 3',x)
	x=re.sub(r'ESCs','E S sees',x)
	x=re.sub(r'H2A','H 2 A',x)
	x=re.sub(r'H2B','H 2 B',x)
	x=re.sub(r'et al\.','et al',x)
	x=re.sub(r'3D','three D', x)
	x =re.sub(r'([^ 0-9])(\d+(?:,\d+)*)', r'\1', x)
	x=re.sub(r'\xe2\x80\x9a\xc3\x84\xc3\xa2\xc2\xac\xe2\x88\x9e', ' degrees ', x)
	x=re.sub(r'\xe2\x80\x9a\xc3\xa0\xc3\xad', ' minus ', x)
	x=re.sub(r'\xe2\x80\x9a\xc3\x84\xc3\xac', '-', x)
	x=re.sub(r'\xe2\x80\x9a\xc3\x84\xc3\xb2', '', x)
	x=re.sub(r'\xe2\x80\x9a\xc3\x84\xc3\xb4', '', x)
	#x =re.sub(r'\,d+', '',x)
	x = re.sub(r'\xce\x94', 'delta', x)
	x = re.sub(r'\xce\xb2', 'beta', x)
	x = re.sub(r'\xc3\x85', 'delta', x)
	x = re.sub(r'\xce\xb1', 'angstrom', x)
	x = re.sub(r'\xce\xb6', 'zeta', x)
	x = re.sub(r'\xce\xb5', 'epsilon', x)
	x = re.sub(r'\xce\xa9', 'omega', x)
	x = re.sub(r'\xce\xbb', 'lambda', x)
	x = re.sub(r'\xce\xb5', 'epsilon', x)
	x = re.sub(r'\xe2\x88\x88', 'epsilon', x)
	x = re.sub(r'\xe2\x88\x91', 'sum of', x)
	x = re.sub(r'\xce\xa9', 'omega', x)
	x=x[:x.find('.References')]

	if args.output_file:
		file=open(args.output_file,'w')
		file.write(x.encode('utf8'))
		file.close()
	else:
		file=open(header+'.txt','w')
		file.write(x.encode('utf8'))
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





