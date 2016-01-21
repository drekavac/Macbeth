play = open('macbeth.txt').read().splitlines()
	
phrase = raw_input("Enter a phrase that appears only once in the play: ")

def find_phrase_index(phrase):
#	for line in play:
#		if phrase in line:
#			return play.index(line)

	for index, line in enumerate(play):
		if phrase in line:
			return index

def find_act(index):
	for line in reversed(play[:index]):
		if 'ACT' in line:
			return line
	# return [next(line for line in reversed(play[:index]) if 'ACT' in line)]
	# only thing is that the above statement returs the result in format ['ACT']
	# so I would have to edit the print, like print line[2:-2] for example

def find_scene(index):
	for line in reversed(play[:index]):
		if 'SCENE' in line:
			scene_line = line.split('.')
			return scene_line[0]
	
def find_scene_characters(index):
	scene_index_top = index
	scene_index_bot = index
	
	for line in reversed(play[:index]):
		if 'SCENE' in line:
			scene_index_top = play.index(line) + 1
			# + 1 is to remove Scene being part of the characters
			break			

	for line in play[index:]:
		if 'SCENE' in line:
			scene_index_bot = play.index(line)
			break
			
	scene_characters = []
	for line in play[scene_index_top:scene_index_bot]:
		if '    ' not in line:
			character_line = line.split('.')
			character_line_again = character_line[0].split('[')
			scene_characters.append(character_line_again[0])
	return scene_characters
	
	
def find_passage(index):
	index_top = index
	index_bot = index
	# used count top and bot because of repetive indexing, empty line was 
	# always index 1
	count_top = 0
	count_bot = 0
	
	for line in reversed(play[:index]):
		if ' ' not in line:
			break
		count_top += 1
	index_top = index - count_top
	print "\nSpoken by: ",
	print play[index - count_top - 1]
	for line in play[index - count_top:index]:
		print line
	
	for line in play[index:]:
		if ' ' not in line:
			break
		count_bot += 1
	index_bot = index + count_bot
	for line in play[index:index + count_bot]:
		print line
		
print(find_act(find_phrase_index(phrase)))
print(find_scene(find_phrase_index(phrase)))

characters = list(set(find_scene_characters(find_phrase_index(phrase))))
print "Scene Characters:"
for line in characters:
	if line != '':
		if line == characters[-1]:
			print "%s." % line[2:]
		else:
			print "%s," % line[2:],

find_passage(find_phrase_index(phrase))
