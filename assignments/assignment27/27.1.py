# class BookStore

class BookStore:
    noofbooks = 0

    def __init__(self,name,author):
        self.name = name
        self.author = author
        BookStore.noofbooks += 1


    def Display(self):
        print(f"{self.name} by {self.author}. No of books: {BookStore.noofbooks}")   

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()


        


        

