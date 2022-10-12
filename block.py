
import json
import time
import os
import hashlib


blockchain_dir = 'blockchain/'

def get_hash(prev_block):
	with open(blockchain_dir + prev_block, 'rb') as f:
		content = f.read()
		return hashlib.sha256(content).hexdigest()

def write_block(penjual, pembeli, harga, luas_tanah):

	blocks_count = len(os.listdir(blockchain_dir))
	prev_block = str(blocks_count)

	data={
		"penjual" : penjual,
		"pembeli" : pembeli,
		"time" : time.time(),
		"harga" : harga,
		"luas_tanah" : luas_tanah,
		"prev_block" : {
			"hash" : get_hash(prev_block),
			"filename" : prev_block
		}
	}
	current_block = blockchain_dir + str(len(os.listdir('blockchain/')) + 1)
	with open(current_block, 'w') as f:
		json.dump(data, f, indent=4, ensure_ascii=False)
		f.write('\n')
def main():
	write_block(penjual="hasbi", pembeli="rangga", harga=90000000, luas_tanah="1h")

if __name__ == '__main__':
	main()