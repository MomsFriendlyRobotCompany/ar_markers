#!/usr/bin/env python

from __future__ import print_function
import argparse

try:
	from cv2 import imwrite
	from ar_markers.marker import HammingMarker
	from ar_markers import __version__
except ImportError:
	raise Exception('Error: OpenCv is not installed')


def handleArgs():
	parser = argparse.ArgumentParser(description='Generate ar markers')
	# parser.add_argument('-v', '--version', help='print version number', version=__version__)
	parser.add_argument('-g', '--generate', help='generate n random markers', type=int)
	parser.add_argument('-i', '--id', help='generate a marker with a specific id', type=int)
	parser.add_argument('-p', '--path', help='path to write ar markers to, default is current directory', default='.')

	args = vars(parser.parse_args())
	return args


if __name__ == '__main__':
	args = handleArgs()
	path = args['path'] + '/marker_{}.png'

	print(args)

	if args['generate']:
		for i in range(args['generate']):
			marker = HammingMarker.generate()
			imwrite(path.format(marker.id), marker.generate_image())
			print("Generated Marker with ID {}".format(marker.id))
	elif args['id']:
		marker = HammingMarker(id=args['id'])
		imwrite(path.format(marker.id), marker.generate_image())
		print("Generated Marker with ID {}".format(marker.id))
	else:
		marker = HammingMarker.generate()
		imwrite(path.format(marker.id), marker.generate_image())
		print("Generated Marker with ID {}".format(marker.id))
	print('Done!')
