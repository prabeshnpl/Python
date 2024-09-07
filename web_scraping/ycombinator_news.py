import requests
from bs4 import BeautifulSoup



def sort_data_by_points(hnlist):
  return sorted(hnlist, key=lambda k:k['Votes'], reverse=True)
  
    
def get_data(links,subtext):
  data = []
  
  for idx , link in enumerate(links):
    
    score_tag = subtext[idx].select('.score')
    if score_tag:
      points = int(score_tag[0].getText().replace(' points',''))
      if points > 100 :
        link_tag = link.find('a')
        href = link_tag.get('href',None)
        title = link.getText()
        data.append({'title':title,'href':href,'Votes':points})
    else :
      link_tag = link.find('a')
      href = link_tag.get('href',None)
      title = link.getText()
      data.append({'title':title,'href':href,'Votes':int()})
   
  return sort_data_by_points(data)

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline') 
subtext = soup.select('.subtext')

mega_links = links + soup2.select('.titleline') 
mega_subtext = subtext + soup2.select('.subtext')


data = get_data(mega_links,mega_subtext)
for idx,a in enumerate(data):
  print(idx,a,'\n')