'''
Created on 13 Mar 2021

@author: Rus

Required Function and its parameters

Example:
search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)

Parameters:
query   :   query string that we want to search for.
tld     :   tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang    :   lang stands for language.
num     :   Number of results we want.
start   :   First result to retrieve.
stop    :   Last result to retrieve. Use None to keep searching forever.
pause   :   Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return  :   Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
'''
#import requests, bs4
#from lazySlavey import listlist
from googlesearch import search

print("Preparing Google Search Module...")

def srch(query):
    print(f"Searching \"{query}\"...")
    ctr = 0
    results = str()
    if query != "__69__":
        for itemURL in search(query, tld="com", num=5, stop=5, pause=2):
            ctr += 1
            results += f"\n{ctr}. {itemURL}"
            #print(f"Found: {itemURL}")
        if results != str():
            #print(f"Search results:{results}")
            return f"Search results:{results}"
        else:
            print(f"Your search \"{query}\" did not match any documents.")
            return f"Your search `{query}` did not match any documents."
    else:
        return "Nice."

"""
#Spaghetti code I DON'T want to touch

url = 'https://google.com/search?q=' + input("Search: ") 

# Fetch the URL data using requests.get(url), 
# store it in a variable, request_result. 
result = requests.get(url) 
print(f"{type(result)}; {result}")
# Creating soup from the fetched request 
#soup = bs4.BeautifulSoup(result.text)
soup = bs4.BeautifulSoup(result.text, "html.parser") 
#print(soup) 
 
# soup.find.all( h3 ) to grab 
# all major headings of our search result, 
titles=soup.find_all( 'h3' )  
# Iterate through the object 
# and print it as a string. 
for info in titles: 
    itemURL = info.get_u()
    print(f"{info.getText()} | \n-----")
"""
