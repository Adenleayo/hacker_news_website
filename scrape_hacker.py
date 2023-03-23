import requests 
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text,'html.parser')

links = soup.select('.titleline')
votes = soup.select('.score')
subtext = soup.select('.title')
#print(votes.text)

def create_hacker_news(links,subtext):
    results = []
    for idx,items in enumerate(links):
        title =links[idx].text
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.subline')
        if len(vote):
            points = int(vote[0].text.replace(' points',''))
            results.append({'title':title, 'links':href, 'points':points})
    return results
hacker_news = create_hacker_news(links,votes)
print(hacker_news)
    
        