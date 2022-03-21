from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('csv_output.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for page in range(1, 18):

    source = requests.get('https://coreyms.com/page/' + str(page)).text

    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('article', class_='post'):
        headline = article.h2.a.text
        print(headline)

        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:
            video_source = article.find(
                'iframe', class_='youtube-player')['src']
            video_id = video_source.split('/')[4].split('?')[0]
            youtube_link = f'https://youtube.com/watch?v={video_id}'
        except Exception as e:
            print('No video found')

        print(youtube_link)

        print()

        csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()
