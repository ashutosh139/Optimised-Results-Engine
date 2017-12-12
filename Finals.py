from APIs import my_key1
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
import bs4
import webbrowser
                                                                     #1-NEWS()
#BBC News

def NewsFromBBC():
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=9734eea192564d9daeb6b5dd21c23071" #BBC news api
    open_bbc_page = requests.get(main_url).json()
    # print(open_bbc_page)
    article = open_bbc_page["articles"]
    results = []
    url = []
    for ar in article:
        results.append(ar["title"])
        url.append(ar["url"])
    for i in range(len(results)):
        print(i + 1, results[i])
    print("Want to read further: Enter your Choice(1-10)")
    query = int(input())
    a = url[query - 1]
    OpenInBrowser(a)

#Times of India News
def NewsFromTOI():
    print("Welcome to Times Of India Latest News Column:")
    main_url="https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=9734eea192564d9daeb6b5dd21c23071" #TimesNow api
    open_toi=requests.get(main_url).json()
    articles=open_toi["articles"]
    (url,results)=([],[])
    for ar in articles:
        results.append(ar["title"])
        url.append(ar["url"])
    for i in range(len(results)):
        print(i+1,results[i])
    print("Want to read further:Enter your Choice(1-7)")
    query=int(input())
    a=url[query-1]
    OpenInBrowser(a)
def OpenInBrowser(url):     # Open in Browser
    import webbrowser
    webbrowser.open(url)
                                                                   #2-Search

                                                      # Address finder in just a seconds by
                                                         # Address Search API
                                                         # Address finder in just a seconds by

def FindAddress():                                       #find address of any place by using google API
    import urllib.parse
    import requests
    main_api = 'https://maps.googleapis.com/maps/api/geocode/json?' # google api
    print("Welcome to my Address Finder:")
# address='lhr'
    while True:
        address = input("Enter the address or type q for quit")
        if address == "q":
            break
        url = main_api + urllib.parse.urlencode({"address": address})
        json_data = requests.get(url).json()
        #print(json_data)
        json_status = json_data['status']
    # print('API Status:'+json_status)
        if json_status == 'OK':

            formatted_address = json_data['results'][0]['formatted_address'] #formatted address
            place_id=json_data['results'][0]['place_id']   # generating place id

            details_url="https://maps.googleapis.com/maps/api/place/details/json?placeid="+(place_id)+"&key=AIzaSyAlT2p81gw8F0DijrFSAz_LQF6-Gz3_vag" # google map api
            open_details=requests.get(details_url).json()
            map_url=open_details["result"]["url"]
            print(formatted_address)
            #print(map_url)
        print("Wnat to look in Google map")
        s=input("Enter y for yes otherwise q:")
        if s=="y":
            OpenInBrowser(map_url)
        else:
            break
        #for each in json_data['results'][0]['address_components']:
          #  print(each['long_name'])
          #  print(each['types'])
        # print(url)
def OpenInBrowser(map_url):
    import webbrowser
    webbrowser.open(map_url)

def SearchAnyPlaces():
    import urllib.parse

    #main_api="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+(query)+&key=AIzaSyAlT2p81gw8F0DijrFSAz_LQF6-Gz3_vag
    print("Search for any places like hotels in delhi etc")
    while True:

        query=input("Enter Your Query or q for quit:")
        load={"key":my_key1,"query":query}
        main_api="https://maps.googleapis.com/maps/api/place/textsearch/json?"
        if query=='q':
            break
        search_req=requests.get(main_api,params=load)
        json_data=search_req.json()
        #print(json_data)
        x=(json_data['results'])
        (names,add,rating)=([],[],[])
        for f in x:
            try:
                names.append(f['name'])
                add.append(f['formatted_address'])
                rating.append(f['rating'])
            except:
                pass


        if len(set(names))==1:
            i=1
            for f in x:
                print(i,f['name'], '-->', f['formatted_address'])
                i+=1
        else:
            try:
                for i in range(len(names)):
                    print(i+1,names[i],rating[i])
            except:
                pass

        d=dict(zip(names,zip(add,rating)))
        q = int(input("Want to know address of anyone enter NUMBER:"))
        print(add[q - 1])

# Top Box Office

def TopBoxOffice():
    print("Top Box Office Now Playing:")
    (gross, cast, title, href) = ([], [], [], [])
    my_url = "http://www.imdb.com/chart/boxoffice?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2773216402&pf_rd_r=0FHEFTWD1G1WYFHRHAYS&pf_rd_s=right-7&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_cht_hd"
    page = urllib.request.urlopen(my_url).read()  # page read
    soup = bs4.BeautifulSoup(page, "lxml")  # opening page
    data = soup.find_all("td", {"class", "titleColumn"})
    rating = soup.find_all("span", {"class", "secondaryInfo"})
    for d in data:
        x = d.find_all("a")
        for name in x:
            (href.append(name['href']), cast.append(name["title"]),
            title.append(name.text))  # saving title,gross collection,cast and link in a list
    for r in rating:
        gross.append(r.text)
    for i in range(len(title)):
        print(i + 1, title[i], "-->", cast[i], gross[i])
    q = int(input("Want to know more enter(1-10) as per your choice"))
    open_page = "http://www.imdb.com"
    OpenIMDB(href[q - 1])  # open in Browser
def OpenIMDB(u):
    import webbrowser
    url = "www.imdb.com" + u
    webbrowser.open(url)



def Latest_Mobiles_Search():
    (names,names_url)=([],[])
    print("Trending Mobiles Coming")
    my_url="http://www.gsmarena.com/"
    page=urllib.request.urlopen(my_url).read()
    soup=bs4.BeautifulSoup(page,"lxml")
    data=soup.find_all("table",{"class":"module-fit green"})
    for d in data:
        x=(d.find_all("a"))
        for i in range(len(x)):
            #print(x[i]["href"])
            names_url.append(x[i]["href"])
    for y in x:
        names.append(y.text)
    for i in range(len(names)):
        print(i+1,names[i])
    query=int(input("Enter your choice:(1-10)"))
    #print(names[query-1],names_url[query-1])
    open_url="https://www.gsmarena.com/"+names_url[query-1]
    webbrowser.open(open_url)

#Search Section
def Seacrh():
    print("1-Find Address")
    print("2-Want list of all places")
    q=int(input())
    if q==1:
        FindAddress()
    elif q==2:
        SearchAnyPlaces()
    #list of all places

#News Section
def News():
    print("1-BBC")
    print("2-TimesNow")
    w=int(input())
    if w==1:
        NewsFromBBC()
    if w==2:
        NewsFromTOI()

#Entertainment Section
def Entertainment():
    print("1-Trending Top Box Office Movies")
    w=int(input())
    if w==1:
        TopBoxOffice()

#Mobiles section
def Mobiles():
    print("1-Trending Mobiles")
    w=int(input())
    if w==1:
        Latest_Mobiles_Search()

print("Welcome To The Optimized Results Engine")
#Menu driven Function
def menu(query):
    if query==1:
        News()
    elif query==2:
        Seacrh()
    elif query==3:
        Entertainment()
    elif query==4:
        Mobiles()


print("1-Latest News")
print("2-Search, Location,Places")
print("3-Entertainment section")
print("4-Mobiles")
query=int(input("Enter Your Option"))
menu(query)
