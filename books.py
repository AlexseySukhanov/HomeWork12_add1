class Books:
    def __init__(self, auth, name, publisher, year, pages):
        if not isinstance(auth, str):
            raise TypeError(f'{type(auth).__name__} Surname is not valid')
        self.auth = auth.title()
        self.name = name.title()
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def filtr(self, auth, year):
        lst=[]
        for i in self:
            if i.auth == auth and i.year >= year:
                lst.append(i.name)
        return lst