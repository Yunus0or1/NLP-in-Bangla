from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.db import connection
from googletrans import Translator
from django import template
from nltk.tokenize import word_tokenize,sent_tokenize
from googletrans import Translator
import nltk
import os



def home(request):
    return render(request, 'a.html', {'what':'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং '})
 
def upload1(request):
	if request.method == 'POST':
	
		handle_uploaded_file(request.FILES['file1'], str(request.FILES['file1']))

		
		from_filename = 'upload/' + request.FILES['file1'].name
		from_file_read = open(from_filename, 'r', encoding="UTF-8")	
		
		
		contents_read = from_file_read.read()
		
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~।'''
		
		no_punct = ""
		
		for char in contents_read:
			if char not in punctuations:
				no_punct = no_punct + char
		
		
		
		frequency = {}
		token = word_tokenize(no_punct)



		for word in token:
			count = frequency.get(word, 0)
			frequency[word] = count + 1


		from_file_read.close()	
		os.remove(from_filename)
		
		zippingResult = zip(frequency.keys(), frequency.values())

		
		return render(request, 'a.html', {
			'countWordResult'		: zippingResult,
			'what'					:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',

			})
		
		

 
	return HttpResponse("Failed to get a file")
	
	
	
	
	
	
def upload2(request):
	if request.method == 'POST':
	
		handle_uploaded_file(request.FILES['file2'], str(request.FILES['file2']))

		
		from_filename = 'upload/' + request.FILES['file2'].name
		from_file_read = open(from_filename, 'r', encoding="UTF-8")	
		
		contents_read = from_file_read.read()
		
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~।'''
		
		no_punct = ""
		
		for char in contents_read:
			if char not in punctuations:
				no_punct = no_punct + char		
		
		words = word_tokenize(no_punct)
		
		

		written_words = []

		
		cursor = connection.cursor()
		
		cursor.execute("select compactLetter from compactword ")
		compactWordResult = cursor.fetchall()
		
		
		
		cursor.execute("select count(compactLetter) from compactword ")
		compactWordCount = cursor.fetchall()
		compactWordCount = compactWordCount[0]
										
										
		
		c=0
		line = ''
		
		for j in range(0,compactWordCount[0]):
			
			char = ''.join(compactWordResult[j-1])
			
			for i in words:
				if (char in i):
					if (i not in written_words):
						if c == 0:
							line = line + char + ':'
							c = 1
						line = line + i+ ','
						written_words.append(i)
			if c==1:
				line = line + '\n'
			c=0
		

		from_file_read.close()	
		os.remove(from_filename)		

		
		
		return render(request, 'a.html', {
			'compactWordResult'		: line,		
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
		
		
        
 
	return HttpResponse("Failed")	
	
def upload3(request):
	if request.method == 'POST':
		
		
		handle_uploaded_file(request.FILES['file3'], str(request.FILES['file3']))

		
		from_filename = 'upload/' + request.FILES['file3'].name
		from_file_read = open(from_filename, 'r', encoding="UTF-8")	
		
		contents_read = from_file_read.read()
		
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~।'''
		
		no_punct = ""
		
		for char in contents_read:
			if char not in punctuations:
				no_punct = no_punct + char
				
		words = no_punct.split()
		
		translator = Translator()
		cursor = connection.cursor()
		
		cursor.execute("select count(id) from permwordmeaning")
		
		totalWords = cursor.fetchall()
		totalWords = totalWords[0][0]
		
		wordmeaningResult = []
		
		for i in range(len(words)):
			
			cursor.execute("select english from permwordmeaning where bangla = %s",[words[i]])
			result = cursor.fetchall()
			
			if result :
				wordmeaningResult.append(result[0][0])
			else :	
				totalWords = totalWords + 1
				t = translator.translate(words[i])
				wordmeaningResult.append(t.text)
				cursor.execute("insert into permwordmeaning (id,bangla,english) values (%s,%s,%s)",[totalWords,words[i],t.text])
			

		
		zippingResult = zip(wordmeaningResult, words)
		
		from_file_read.close()	
		os.remove(from_filename)		
		
		return render(request, 'a.html', {
			'zippingResult'				: zippingResult,	
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
			
			
def upload4(request):
	if request.method == 'POST':
		
		
		handle_uploaded_file(request.FILES['file4'], str(request.FILES['file4']))

		
		from_filename = 'upload/' + request.FILES['file4'].name
		from_file_read = open(from_filename, 'r', encoding="UTF-8")	
		
		contents_read = from_file_read.read()
		
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~।'''
		
		no_punct = ""
		
		for char in contents_read:
			if char not in punctuations:
				no_punct = no_punct + char
				
		words = no_punct.split()
		
		
		translator = Translator()
		cursor = connection.cursor()
		
		cursor.execute("select count(bangla_word) from word_pos_tag")
		totalWordinDatabase = cursor.fetchall()
		totalWordinDatabase = totalWordinDatabase[0][0]
		startinPositionforDatabase = totalWordinDatabase

		
		totalWordsinFile = len(words)
      
		bangla_word = []
		pos_tag_bangla = []
		

    	       
		for i in range(totalWordsinFile):
			

		
			cursor.execute("select pos_tag_bangla from word_pos_tag where bangla_word = %s",[words[i]])
			result = cursor.fetchall()
			
			if result:
				bangla_word.append(words[i])
				pos_tag_bangla.append(result[0][0])
			
				#return HttpResponse(pos_tag_bangla[i])
				
			else :
			
				if (words[i]=='আমি') or (words[i]=='আমরা') or (words[i]=='আমাদের') or (words[i]=='আমাদেরকে') or (words[i]=='তুমি') or (words[i]=='তোমরা') or (words[i]=='তোমাদেরকে') or (words[i]=='তোমাদের') or (words[i]=='সে') or (words[i]=='তারা') or (words[i]=='তাদের') or (words[i]=='তাদেরকে') or (words[i]=='উহা') or (words[i]=='উহাদেরকে') or (words[i]=='ও') or (words[i]=='ওরা') or (words[i]=='ওদেরকে') or (words[i]=='এ')or (words[i]=='এরা') or (words[i]=='এদেরকে') or (words[i]=='তোরা') or (words[i]=='তোদেরকে') or (words[i]=='আপনি ') or (words[i]=='আপনারা') or (words[i]=='আপনাদেরকে') or (words[i]=='আপনাকে')or (words[i]=='তা'):
				
					cursor.execute("insert into word_pos_tag (bangla_word,pos_tag_bangla,pos_tag_english) values (%s,'সর্বনাম','PRP')",[words[i]])	
					
					bangla_word.append(words[i])
					pos_tag_bangla.append('সর্বনাম')
					
				else :	
				
					t = translator.translate(words[i])

					token = word_tokenize(t.text)
					pos_tag = nltk.pos_tag(token)
									
					if (pos_tag[0][1]=='JJ') or (pos_tag[0][1]=='JJR') or (pos_tag[0][1]=='JJS') or (pos_tag[0][1]=='CD') or (pos_tag[0][1]=='RB') or (pos_tag[0][1]=='RBR')or (pos_tag[0][1]=='RBS') or (pos_tag[0][1]=='UH') or (pos_tag[0][1]=='PDT'):
						cursor.execute("insert into word_pos_tag (bangla_word,pos_tag_bangla,pos_tag_english) values (%s,'বিশেষণ',%s)",[words[i],pos_tag[0][1]])
						
						bangla_word.append(words[i])
						pos_tag_bangla.append('বিশেষণ')
						
					
						
					if (pos_tag[0][1]=='DT') or (pos_tag[0][1]=='EX') or (pos_tag[0][1]=='IN') or (pos_tag[0][1]=='TO'):
						cursor.execute("insert into word_pos_tag (bangla_word,pos_tag_bangla,pos_tag_english) values (%s,'অব্যয়',%s)",[words[i],pos_tag[0][1]])	
						
						bangla_word.append(words[i])
						pos_tag_bangla.append('অব্যয়')
						
					if (pos_tag[0][1]=='VB') or (pos_tag[0][1]=='VBD') or (pos_tag[0][1]=='VBG') or (pos_tag[0][1]=='VBN') or (pos_tag[0][1]=='VBP') or (pos_tag[0][1]=='VBZ') or (pos_tag[0][1]=='MD'):
						cursor.execute("insert into word_pos_tag (bangla_word,pos_tag_bangla,pos_tag_english) values (%s,'ক্রিয়া',%s)",[words[i],pos_tag[0][1]])	
						
						bangla_word.append(words[i])
						pos_tag_bangla.append('ক্রিয়া')
						
					if (pos_tag[0][1]=='FW') or (pos_tag[0][1]=='NN') or (pos_tag[0][1]=='NNS') or (pos_tag[0][1]=='NNP') or (pos_tag[0][1]=='NNPS') or (pos_tag[0][1]=='RP') :
						cursor.execute("insert into word_pos_tag (bangla_word,pos_tag_bangla,pos_tag_english) values (%s,'বিশেষ্য',%s)",[words[i],pos_tag[0][1]])
						
						bangla_word.append(words[i])
						pos_tag_bangla.append('বিশেষ্য')
				
			

		word_pos_result = zip(bangla_word, pos_tag_bangla)	

		from_file_read.close()	
		os.remove(from_filename)		
		
		return render(request, 'a.html', {
			'word_pos_result'			: word_pos_result,	
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
			
def search1(request):
	
	searchword = request.POST['search1']
	cursor = connection.cursor()

	cursor.execute("select distinct(english) from permwordmeaning where bangla = %s",[searchword])
	wordSearchResult = cursor.fetchall()
	
	
	
	if wordSearchResult:
		wordSearchResult = wordSearchResult[0][0]
		return render(request, 'a.html', {
			'wordSearchResult'			: wordSearchResult,	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
	else :
		translator = Translator()
		t=translator.translate(searchword)
		
		
		
		if t.src == 'en':
			return render(request, 'a.html', {
			'wordSearchResult'			: "এটি একটি ইংরেজি শব্দ",	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
		else :
			cursor.execute("select count(id) from permwordmeaning")
			countResult = cursor.fetchall()
			
			cursor.execute("insert into permwordmeaning (id,bangla,english) values (%s,%s,%s)",[countResult[0][0]+1,searchword,t.text])
			
			
			
			return render(request, 'a.html', {
				'wordSearchResult'			: t.text,	
				'searchword'				: searchword,
				'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
				})

def search3(request):
	
	searchword = request.POST['search3']
	cursor = connection.cursor()

	cursor.execute("select distinct(bangla) from permwordmeaning where english = %s",[searchword])
	wordSearchResult = cursor.fetchall()
	
	
	
	if wordSearchResult:
		wordSearchResult = wordSearchResult[0][0]
		return render(request, 'a.html', {
			'wordSearchResult'			: wordSearchResult,	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
	else :
		translator = Translator()
		t=translator.translate(searchword,dest='bn')
		
		
		
		if t.src == 'bn':
			return render(request, 'a.html', {
			'wordSearchResult'			: "এটি একটি বাংলা শব্দ",	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
		else :
			cursor.execute("select count(id) from permwordmeaning")
			countResult = cursor.fetchall()
			
			cursor.execute("insert into permwordmeaning (id,bangla,english) values (%s,%s,%s)",[countResult[0][0]+1,t.text,searchword])
			
			
			
			return render(request, 'a.html', {
				'wordSearchResult'			: t.text,	
				'searchword'				: searchword,
				'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
				})				


def search5(request):
	if request.method == 'POST':
		
		searchword = request.POST['search5']
		handle_uploaded_file(request.FILES['file5'], str(request.FILES['file5']))

		

		
		from_filename = 'upload/' + request.FILES['file5'].name
		from_file_read = open(from_filename, 'r', encoding="UTF-8")	
		
		
		contents_read = from_file_read.read()
		
		
		frequency = {}
		token = word_tokenize(contents_read)
		token_clearing_from_punctuation = []


		if searchword in token :
			for i in range(1,len(token)):

				if (token[i] != ',')  :
					token_clearing_from_punctuation.append(token[i])




			for word in token_clearing_from_punctuation:
				count = frequency.get(word, 0)
				frequency[word] = count + 1

			
			from_file_read.close()	
			os.remove(from_filename)


				
			
			return render(request, 'a.html', {
				'searchword'			:searchword,
				'countWordResultfromSearch'		:frequency[searchword],
				'what'					:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',

				})
		
		else :
			return render(request, 'a.html', {
				'searchword'			:searchword,
				'countWordResultfromSearch'		:'0',
				'what'					:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',

				})
	
 
	return HttpResponse("Failed to get a file")
				
def search2(request):
	
	searchword = request.POST['search2']
	cursor = connection.cursor()
	


	cursor.execute("select distinct(pos_tag_bangla) from word_pos_tag where bangla_word = %s",[searchword])
	wordSearchResult = cursor.fetchall()
	

	
	if wordSearchResult:
		wordSearchResult = wordSearchResult[0][0]
		return render(request, 'a.html', {
			'wordSearchResult'			: wordSearchResult,	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
	else :
		return render(request, 'a.html', {
			'wordSearchResult'			: "পদ খুঁজে পাওয়া যায়নি ",	
			'searchword'				: searchword,
			'what'						:'বাংলা ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং ',
			})
		
		
		
		
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
		