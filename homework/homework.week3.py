import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    
    title = song.select_one('td.number')
    title.span.decompose()
    text_title = title.text
    rank = text_title.strip()
    # print(rank)
    
    song_title = song.select_one('td.info > a.title.ellipsis')
    song_title_text = song_title.text
    song_title_only = song_title_text.strip()
    # print(song_title_only)

    artist = song.select_one('td.info > a.artist.ellipsis')
    artist_name = song.select_one('td.info > a.artist.ellipsis')
    artist_name_text = artist_name.text
    artist_name_only = artist_name_text.strip()
    # print(artist_name_only)

    print(rank, song_title_only, artist_name_only)


#랭킹 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#제목 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#가수 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis


