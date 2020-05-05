def t2p():
	#Establishing vowels and consonants
	vowels = ['a', 'e', 'i', 'o', 'u']
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	#Asking for text
	text = input('Text:')
	splittext = str(text.lower()).split()
	for word in splittext:
		wordsoundlist = []
		for letter in word:
			wordsoundlist.extend(letter)

		progress = 0
		graphemesforword = []
		for entry in wordsoundlist:
			graphemesforword.append('null')
		for entry in wordsoundlist:
			#Rule 1: A_e
			if wordsoundlist[progress] in vowels:
				if len(wordsoundlist) - progress > 1:
					if wordsoundlist[progress + 1] in consonants:
						if len(wordsoundlist) - progress > 2:
							if wordsoundlist[progress + 2] is 'e' or wordsoundlist[progress + 2] is 'a':
								graphemesforword[progress] = 'Long. ' + wordsoundlist[progress]
							elif len(wordsoundlist) - progress > 3:
								if wordsoundlist[progress + 3] is 'e' or wordsoundlist[progress + 3] is 'a': 
									graphemesforword[progress] = 'Long ' + wordsoundlist[progress]
								else:
									graphemesforword[progress] = 'Short ' + wordsoundlist[progress]
							else:
								graphemesforword[progress] = 'Short ' + wordsoundlist[progress]
						else:
							graphemesforword[progress] = 'Short ' + wordsoundlist[progress]
				elif wordsoundlist[progress] is 'o':
					graphemesforword[progress] = 'Long o'

			#Rule 2: The "el" exeption
			if wordsoundlist[progress] is 'e':
				if len(wordsoundlist) - progress > 1:
					if wordsoundlist[progress + 1] is 'l':
						graphemesforword[progress] = ('Short e')
						graphemesforword[progress + 1] = ('Short l')

			#Rule 4: Double l, and Ls
			if wordsoundlist[progress] is 'l':
				if len(wordsoundlist) > 1:
					if wordsoundlist[progress + 1] is 'l':
						graphemesforword[progress + 1] = '-'
						graphemesforword[progress] = 'Long l'
				else:
					graphemesforword[progress] = 'Short l'

			#Rule 5: H or P or T
			if wordsoundlist[progress] is 'h':
				graphemesforword[progress] = 'h'
			if wordsoundlist[progress] is 'p':
				graphemesforword[progress] = 'p'
			if wordsoundlist[progress] is 't':
				graphemesforword[progress] = 't'

			#Rule 6: 'Wor'
			if 'w' in wordsoundlist:
				wpos = wordsoundlist.index('w')
				if len(wordsoundlist) - wpos > 3:
					if wordsoundlist[wpos + 1] is 'o':
						if wordsoundlist[wpos + 2] is 'r':
							graphemesforword[wpos] = 'w'
							graphemesforword[wpos + 1] = 'Short u'
							graphemesforword[wpos + 2] = 'r'

			#Rule 7: Ph and Th
			if 't' in wordsoundlist:
				pos = wordsoundlist.index('t')
				if len(wordsoundlist) - pos > 2:
					if wordsoundlist[pos + 1] is 'h':
						graphemesforword[pos] = 'Th blend'
						graphemesforword[pos + 1] = '-'
			if 'p' in wordsoundlist:
				pos = wordsoundlist.index('p')
				if len(wordsoundlist) - pos > 2:
					if wordsoundlist[pos + 1] is 'h':
						graphemesforword[pos] = 'Short f'
						graphemesforword[pos + 1] = '-'

			if wordsoundlist[0] = 't':
				graphemesforword[0] = 'Th blend'
				graphemesforword[1] = 'Short u'

			print(graphemesforword)

			progress += 1
		if '-' in graphemesforword:
			graphemesforword.remove('-')
		print(graphemesforword)