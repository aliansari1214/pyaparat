import requests
from bs4 import BeautifulSoup
import re
from pyaparat.exceptions import QualityError


qualities = {
	'144': 0,
	'240': 1,
	'360': 2,
	'480': 3,
	'720': 4,
	'1080': 5
}


class Scraper:
	def __init__(self, url, quality):
		self.url = url
		self.quality = quality

	def get_all_links(self):
		result = requests.get(self.url)
		content = BeautifulSoup(result.text, 'html.parser')
		video_links = content.find_all('a', href=re.compile('.mp4'))
		hrefs = [link['href'] for link in video_links]
		return hrefs

	def get_link(self):
		links = self.get_all_links()
		available_qualities = self.get_qualities()
		if self.quality not in available_qualities:
			raise QualityError(f'This quality is not avalable \n available qualities are {available_qualities}')
		else:
			link = links[qualities[self.quality]]
			return link

	def get_qualities(self):
		links = self.get_all_links()
		qua = list(qualities.keys())
		available_qualities = []
		for i in range(len(links)):
			available_qualities.append(qua[i])
		return available_qualities
