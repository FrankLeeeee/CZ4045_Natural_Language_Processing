import pandas as pd
import json
import sys
import os
from os.path import join




def main():

	json_file = sys.argv[1]

	print('processing json file: %s ...' %(json_file))

	with open (json_file, 'rb') as f:
	    data = f.read()

	data = data.decode('latin-1').encode().decode()

	columns = list(json.loads(data.split('\n')[0]).keys())
	rows=[list(json.loads(r).values()) for r in data.split('\n')[:-1]]
	df = pd.DataFrame(data = rows , columns= columns)

	print('saved to data.csv ...')

	save_path = join(os.getcwd(), 'core', 'data')

	if not os.path.exists(save_path):
		os.makedirs(save_path)

	df.to_csv(join(save_path, 'data.csv'))

if __name__ == '__main__':
	main()
