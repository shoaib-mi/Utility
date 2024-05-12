# This code will get list of ttml files inside current directory, and convert them into srt file. The ttml file starts with some redundant (in srt file) information that must be ignored, then the format was as following
#<p begin="00:00:07.639" end="00:00:14.120" style="s2">subtitle content</p>
#and all the lines were the same format without any interruption. if there is an interruption in a file you should fix that interruption then using this code, or edit the code based on your own ttml style.

import os

# Getting list of all subtuitle ttml files and save it in ttml_file_list
ttml_file_list = []
files = os.walk('.')
for __,___, filenames in files:
	for fname in filenames:
		if fname.endswith(".ttml"):
			ttml_file_list.append(fname[0:-5])

# Walk through all ttml files and convert them into srt file
for filename in ttml_file_list:
	ttml_file_lines = open(filename + '.ttml','r').readlines()
	srt_file = open(f'{filename}.srt','w')
	first_line_found = False
	line_number = 1
	for i in range(len(ttml_file_lines)):
		if ttml_file_lines[i][0:9] =='<p begin=':
			# Since we are comparing two sequential elements, then we must process first line before any comparison
			if not first_line_found:
				this_line = ttml_file_lines[i][10:22] + ' --> ' + ttml_file_lines[i][29:41] + '\n'
				srt_file.writelines(["1\n", this_line, ttml_file_lines[i][54:-5].replace('&#39;',"'") + '\n\n'])
				first_line_found = True
				line_number += 1
			else:
				this_line_end = ttml_file_lines[i][29:41]
				this_line_begin = ttml_file_lines[i][10:22]
				next_line_begin = ttml_file_lines[i+1][10:22]
				# check if there is overlap of timeframes and if this line is not final line
				if (this_line_end > next_line_begin) & (len(next_line_begin) == 12):
					this_line = this_line_begin + ' --> ' + next_line_begin + '\n'
					srt_file.writelines([f"{line_number}\n", this_line, ttml_file_lines[i][54:-5].replace('&#39;',"'") + '\n\n'])
					line_number += 1
				else:
					this_line = this_line_begin + ' --> ' + this_line_end + '\n'
					srt_file.writelines([f"{line_number}\n", this_line, ttml_file_lines[i][54:-5].replace('&#39;',"'") + '\n\n'])
					line_number += 1

	srt_file.writelines(['9999\n00:00:00.000 --> 00:00:02.000\n<font color="#008000" size=18>ehmp.co.ir</font>'])
	srt_file.close()