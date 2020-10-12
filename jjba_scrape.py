import sys, math, webbrowser, requests, re
from bs4 import BeautifulSoup
from tqdm import tqdm

if __name__ == '__main__': #if its being run directly from the  command line
		source = 'https://storage.kanzaki.ru/ANIME___/JoJo%27s_Bizarre_Adventure/JoJo%27s%20Bizarre%20Adventure%20-%20Diamond%20is%20Unbreakable%2001-39/'
		html = requests.get(source) #gets the html from the link
		soup = BeautifulSoup(str(html.text), "html.parser") 
		all_links = soup.find_all('a') #extracts the <a> tag in the html for the hyperlink
		all_links = all_links[1:] #excludes the first <a> tag bc its not the first episode

		for i, next_link in enumerate(all_links):
			print('Downloading episode', i+1 ,'of {}'.format(next_link.text))
			request = requests.get(source+next_link['href'], stream = True) 
			file = open('./{}.mp4'.format(next_link.text), 'wb') 
			for chunk in (request.iter_content(1025)): 
				 file.write(chunk)
			file.close() 
			print("Finished downloading episode ", i+1)

