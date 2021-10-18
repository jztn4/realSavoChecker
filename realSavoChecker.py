import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup

music_name = 'realSavoTV'
query_string = urllib.parse.urlencode({"search_query": music_name})
formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

inspect = BeautifulSoup(clip.content, "html.parser")
yt_title = inspect.find_all("meta", property="og:title")

for concatMusic1 in yt_title:
    pass
    
with open('newUpload.txt', 'r') as r:
	info = r.read()
	if info == concatMusic1['content']:
		print("No New Videos 😭😭😭")
	else:
		print("GO CHECK OUT THE NEW VIDEO 💯💯💯")
		print(concatMusic1['content'])
	with open('newUpload.txt', 'w') as w:
		w.write(concatMusic1['content'])

