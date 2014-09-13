from BeautifulSoup import BeautifulSoup
import urllib2
import csv

#url to begin with
base_url="http://projects.propublica.org/docdollars/search?company%5Bid%5D=19&amp;page=1&amp;period%5B%5D=2012&amp;services%5B%5D=&amp;state%5Bid%5D=5&amp;term=&amp;utf8=%E2%9C%93"
#m=base_url[73]

#set empty dataframes. we need these so we have somewhere to put what we grab
pages=[]
data = []

#mcguyver-style hack which allows me to go from page=1 to page=1+n (it's in the middle of the string)
for i in range(0,5):
	m=int("1")+i
	m1=str(m)
	if m<10:
		base_url2=base_url[:77]+m1+base_url[78:]
	#next line is not necessary, i included it to make sure i parsed the string correctly
	#print base_url2
	page=urllib2.urlopen(base_url2)
	soup = BeautifulSoup(page.read())

	table = soup.find('table', attrs={'id':'payments_list'})
	table_body = table.find('tbody')

	rows = table_body.findAll('tr')
	for row in rows:
    		cols = row.findAll('td')
    		info = []
    		for item in cols:
    			cols = item.text.strip().encode('utf-8')
    			info.append(cols)
		data.append(info)
print data

#to save as csv
with open("output2.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerows(data)
