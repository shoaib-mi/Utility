import os
os.system("cls")
path = input("Enter the path for TS files > ")
filenames = os.listdir(f'{path}')
exe_path = 'C:\\Program Files\\MKVToolNix'
os.chdir(exe_path)
files_processed = []

for filename in filenames:
	if filename[-3:] == ".ts":
		new_filename = filename[:-3] + ".mkv"
		old_path = path + "\\" + filename
		new_path = path + "\\" + new_filename
		cmd = f'mkvmerge -o "{new_path}" "{old_path}"'
		os.system(cmd)
		files_processed.append(filename)
		os.system("cls")
		i = 1
		for i in range(len(files_processed)): 
			os.system(f'echo "{i+1} ==> {files_processed[i]}"')
		os.system("echo ------------------------------------------------------------")
		os.system("echo ------------------------------------------------------------")
		os.system("echo ------------------------------------------------------------")
		