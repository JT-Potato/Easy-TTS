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
			#Rule 1: Long vowel vs short vowel
			if wordsoundlist[progress] in vowels:
				if len(wordsoundlist) - progress > 1:
					if wordsoundlist[progress + 1] in consonants:
						if len(wordsoundlist) - progress > 2:
							if wordsoundlist[progress + 2] is 'e':
								graphemesforword[progress] = 'Long ' + wordsoundlist[progress]
							elif len(wordsoundlist) - progress > 3:
								if wordsoundlist[progress + 3] is 'e':
									graphemesforword[progress] = 'Long ' + wordsoundlist[progress]
								else:
									graphemesforword[progress] = 'Short ' + wordsoundlist[progress]
							else:
								graphemesforword[progress] = 'Short ' + wordsoundlist[progress]
						else:
							graphemesforword[progress] = 'Short ' + wordsoundlist[progress]

			#Rule 2: The "el" exeption
			if wordsoundlist[progress] is 'e':
				if len(wordsoundlist) - progress > 1:
					if wordsoundlist[progress + 1] is 'l':
						print('Short e')
			progress += 1
			print(graphemesforword)