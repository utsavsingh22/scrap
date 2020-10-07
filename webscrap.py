import requests
from bs4 import BeautifulSoup
from urllib.request import unquote


url = 'https://www.privacy.gov.ph/data-privacy-act-primer/'


print('HTTP GET: %s', url)
response = requests.get(url)


content = BeautifulSoup(response.text, 'lxml')


all_urls = content.find_all('a')


for url in all_urls:
   
    try:

        if 'pdf' in url['href']:
            # init PDF url
            pdf_url = ''
            
           
            if 'https' not in url['href']:
                pdf_url = 'https://www.privacy.gov.ph/' + url['href']

            
            else:
                pdf_url = url['href']
            
           
            print('HTTP GET: %s', pdf_url)          
            pdf_response = requests.get(pdf_url)
            
          
            filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
            
            with open('./pdf/' + filename, 'wb') as f:
              
                f.write(pdf_response.content)
    
    # skip all the other URLs
    except:
        pass