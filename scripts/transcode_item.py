import argparse
import os
import sys

sys.path.insert(0, os.getcwd())

import transcoder


parser = argparse.ArgumentParser(description='add item to transcode queue')

parser.add_argument('path', help='file path to transcode')

args = parser.parse_args()

quality = transcoder.TranscodeQuality(2_000_000, 'aac', 2, '128k')

item = transcoder.TranscodeItem(args.path, quality, None)

transcoder.transcode_queue.put(item)

print('place in queue:', transcoder.transcode_queue.size)
