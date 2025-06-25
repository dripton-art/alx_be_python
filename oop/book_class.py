class Book:
    def __init__(self, title=str, author=str, year=int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return("{title} by {author}, published in {year}")

    def __repr__(self):
        return(f"Book('{self.title}', '{self.author}', {self.year})")

    def __del__(self):
        print("Deleting {self.title}")