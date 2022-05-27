import requests
from bs4 import BeautifulSoup
import csv

file = open('apple.csv', 'w',encoding="utf8", newline='\n')
obj = csv.writer(file)
obj.writerow(["Model", "Price" , "Image_url"])

url = 'https://zoommer.ge/samsung-smartphone'
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.text, 'html.parser')

phone = soup.find('div', class_="popular_products_inside")

samsung = phone.findAll('div', class_='lg_3 lp_3 md_4 sm_6 xs_6 product_item')

for phones in samsung:
    phone_name = phones.h4.text
    image_Url = phones.img.attrs.get('data-mobile-src')
    price = phones.find('div', class_='product_new_price').text
    obj.writerow([phone_name, price,image_Url])
    #print(image_Url)
    print(price)

#ბოდიშით პირველ რიგში გვიან ვტვირთავ. ჯერ ნორმალური საიტი ვერ ვნახე, ბოლოს ძლივს  დავპარსე ზუმერის საიტი და აღმოვაჩინე რომ
#არ აქვს გვერდებზე გადასვლა და ამის ატვირთვა მიწევს :/ 
