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
		for entry in wordsoundlist:
			#Rule 1: Long vowel vs short vowel
			if wordsoundlist[progress] in vowels:
				progress1 = progress + 1
				if len(wordsoundlist) - progress > 1
				if wordsoundlist[progress1] in consonants:
					if len(wordsoundlist) - progress > 2:
						progress2 = progress + 2
						if wordsoundlist[progress2] is 'e':
							print('Long ' + wordsoundlist[progress])
						elif len(wordsoundlist) - progress > 3:
							progress3 = progress + 3
							if wordsoundlist[progress3] is 'e':
								print('Long ' + wordsoundlist[progress])
							else:
								print('Short ' + wordsoundlist[progress])
						else:
							print('Short ' + wordsoundlist[progress])
					else:
						print('Short ' + wordsoundlist[progress])
			progress += 1