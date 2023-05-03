# Создайте класc Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# выведите в консоль значение аргумента Loc, объекта search

class Input:

    def __init__(self, loc):
        self.loc = loc

search = Input("input#search")

print(search.loc)

class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
            print(self.url)

home = Page("http://demoga.com/")
home.get()

