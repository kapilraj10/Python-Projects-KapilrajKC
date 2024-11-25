import requests
from bs4 import BeautifulSoup
import pandas as pd 
url = "https://www.daraz.com.np/baby-diapers/?spm=a2a0e.11779170.categories.1.287d2d2bscb3yh&up_id=119144700&clickTrackInfo=fa1127ec-9add-48e1-aa81-2dd5e3079881__8770__119144700__static__0.09999243970666062__platform__ANDROID__scm__1007.40350.322036.__brandID__0__SellerID__0__IsHitHot__1__IfCart__0__IfOrder__0__IfLeafCatCart__0__IfLeafCatOrd__0__IfBrandCart__0__IfBrandOrd__0__IfCartSeller__0__IfOrdSeller__0__item_sold__0__GmvNow__0.0__item_day_sold__0__ctr__0.0__cvr__0.0__rank__0.0__322036__30350&from=hp_categories&item_id=119144700&version=v2"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
#print(soup)
rows = soup.find('', {'id': 'beacon-aplus'}).find('tbody').find_all('tr')
print(len(rows))

