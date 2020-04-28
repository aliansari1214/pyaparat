from pyaparat.scraper import Scraper
import requests


class Main:
	def __init__(self, url, quality):
		self.url = url
		self.quality = quality
		self.scraper = Scraper(url, quality)

	def download(self):
		video_url = str(self.scraper.get_link())
		video_name = video_url.split('/')
		with open(video_name[4], 'wb') as f:
			print('Downloading...')
			result = requests.get(video_url, stream=True)
			total = result.headers.get('content-length')

			if total is None:
				f.write(result.content)
			else:
				download = 0
				total = int(total)
				for data in result.iter_content(chunk_size=4096):
					download += len(data)
					f.write(data)
					done = int(50*download / total)
					print("\r[%s%s]" % ('=' * done, ' ' * (50-done)), end='')
		print('\nVideo downloaded...')
