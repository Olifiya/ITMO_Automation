class Page
def __init__(self,url):
self.url=url
def get(self):
print (self.url)
link_page=Page("http://...")
link_page.get()



