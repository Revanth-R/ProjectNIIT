#level_2
x=input("Enter the url:")
word=str(input("Enter the word:"))
num=0
import requests
from bs4 import BeautifulSoup
r=requests.get(x)
soup = BeautifulSoup(str(r.text),'html.parser')
html_doc=str(r.text)
with open('count.txt','w') as file:
    file.write(html_doc)
with open('count.txt','r') as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                num=num+1
print("The Count of word is:",num)            
        
        
