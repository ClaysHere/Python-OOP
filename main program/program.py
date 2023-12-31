import abc

class BookStore(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def id(self):
        pass
    
    @abc.abstractproperty
    def title(self):
        pass

    @abc.abstractproperty
    def cetakInfo(self):
        pass

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, book):
        pass

class StockObserver(Observer):
    def update(self, book):
        if book.amount < 5:
            print(f'Stock of book "{book.title}" is below 5. Notify the employee!')

class attributeBook:
    def __init__(self, author, page, edition, genre, price):
        self.author = author
        self.page = page
        self.edition = edition
        self.genre = genre
        self.price = price

class printedBook(BookStore, attributeBook):
    id = ''
    title = ''
    def __init__(self, id, title, author, page, edition, genre, price, amount, cover, ISBN):
        super().__init__(author, page, edition, genre, price)
        self.id = id
        self.title = title
        self.amount = amount
        self.cover = cover
        self.ISBN = ISBN

    def cetakInfo(self):
        print(f'ID Buku : {self.id}')
        print(f'Judul Buku : {self.title}')
        print(f'Penulis Buku : {self.author}')
        print(f'Jumlah Halaman : {self.page}')
        print(f'Edisi : {self.edition}')
        print(f'Genre : {self.genre}')
        print(f'Harga Buku : {self.price}')
        print(f'Jumlah Buku : {self.amount}')
        print(f'Cover : {self.cover}')
        print(f'ISBN : {self.ISBN}')
        print()

class Ebook(BookStore, attributeBook):
    id = ''
    title = ''
    def __init__(self, id, title, author, page, edition, genre, price, format, size, licenseKey):
        super().__init__(author, page, edition, genre, price)
        self.id = id
        self.title = title
        self.format = format
        self.size = size
        self.licenseKey = licenseKey

    def cetakInfo(self):
        print(f'ID Buku : {self.id}')
        print(f'Judul Buku : {self.title}')
        print(f'Penulis Buku : {self.author}')
        print(f'Jumlah Halaman : {self.page}')
        print(f'Edisi : {self.edition}')
        print(f'Genre : {self.genre}')
        print(f'Harga Buku : {self.price}')
        print(f'Format File : {self.format}')
        print(f'File Size : {self.size}')
        print(f'License Key : {self.licenseKey}')
        print()

class listBook:
    def __init__(self):
        self.listBookPrinted = []
        self.listEbook = []
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, book):
        for observer in self.observers:
            observer.update(book)

    def inputBookPrinted(self, book):
        try:
            if(self.cekKode(book.id) and self.cekJumlahHalaman(book.page) and self.cekHarga(book.price)):
                self.listBookPrinted.append(book)
                print(f"Book with ID {book.id} successfully added to the catalog.")
                self.notify_observers(book)
            
        except ValueError as e:
            print(f"Error: {e}")

    def inputEBook(self, book):
        try:
            if(self.cekEbook(book.id) and self.cekJumlahHalaman(book.page) and self.cekHarga(book.price)):
                self.listEbook.append(book)
                print(f"Book with ID {book.id} successfully added to the catalog.")
                self.notify_observers(book)
            
        except ValueError as e:
            print(f"Error: {e}")

    def cekKode(self, book_id):
        for existing_book in self.listBookPrinted:
            if existing_book.id == book_id:
                print(f"Book with ID {book_id} already exists in the catalog.")
                return False
        return True

    def cekEbook(self, book_id):
        for existing_book in self.listEbook:
            if existing_book.id == book_id:
                print(f"Book with ID {book_id} already exists in the catalog.")
                return False
        return True
    
    def cekJumlahHalaman(self, page):
        try:
            page = int(page)
        except ValueError as e:
            print('Jumlah halaman harus dalam bentuk angka.')
            return False
        return True
    
    def cekHarga(self, price):
        try:
            price = int(price)
        except ValueError as e:
            print('Harga buku harus dalam bentuk angka.')
            return False
        return True

    def searchBook(self, search_term):
        found_books = []

        for book in self.listBookPrinted:
            if search_term.lower() in book.title.lower():
                found_books.append(book)

        for ebook in self.listEbook:
            if search_term.lower() in ebook.title.lower():
                found_books.append(ebook)

        if not found_books:
            print(f'No books found with the search term: {search_term}')
        else:
            print('Found books:')
            for found_book in found_books:
                found_book.cetakInfo()

    def buyBook(self):
        book_type = input('Enter the type of the book you want to buy (p/e): ')
        book_id = input('Enter the ID of the book you want to buy: ')

        if book_type == "p":
            for book in self.listBookPrinted:
                if book.id == book_id:
                    if book.amount > 0:
                        print(f'You have successfully purchased "{book.title}".')
                        book.amount -= 1
                        return
                    else:
                        print(f'Sorry, "{book.title}" is out of stock.')
                        return

        elif book_type == "e":
            license_key = input('Enter the license key: ')
            for ebook in self.listEbook:
                if ebook.id == book_id:
                    if ebook.licenseKey == license_key:
                        print(f'You have successfully purchased "{ebook.title}".')
                        ebook.licenseKey = 'Used'
                        return
                    else:
                        print('Invalid license key. Purchase failed.')
                        return

        print(f'Book with ID {book_id} not found in the catalog.')

    def cekStock(self, id):
        iter_item = iter(self.listBookPrinted)

        while True:
            try:
                item = next(iter_item)
                if item.id == id:
                    if item.amount < 5:
                        print(f'Stock {item.title} kurang dari 5')
                    else:
                        print(f'Stock {item.title} aman')
                    break
            except StopIteration:
                print('Barang tidak ditemukan')
                break

    def cetakPrintedBook(self):
        if len(self.listBookPrinted) == 0:
            print("Catalog is empty. No books available.")
        else:
            for i in self.listBookPrinted:
                i.cetakInfo()
        
    def cetakEBook(self):
        if len(self.listEbook) == 0:
            print("Catalog is empty. No books available.")
        else:
            for i in self.listEbook:
                i.cetakInfo()


def main():
    bookstore = listBook()
    stock_observer = StockObserver()
    bookstore.add_observer(stock_observer)
    while True : 
        print('Selamat Data di Conquerors Book Store')
        print('Siapakah Anda?')
        print('1. Customer')
        print('2. Employee')
        print('3. Exit')
        opsi = int(input('Masukan pilihan Anda : '))
        if(opsi == 1):
            while True:
                print('1. Book Catalog')
                print('2. Search Book')
                print('3. Buy Book')
                print('4. Back to Main')
                pil = int(input('Masukkan pilihan : '))
                if(pil == 1):
                    print('Printed Book')
                    bookstore.cetakPrintedBook()
                    print('Ebook')
                    bookstore.cetakEBook()
                if(pil == 2):
                    search_term = input('Enter search term: ')
                    bookstore.searchBook(search_term)
                if(pil == 3):
                    bookstore.buyBook()
                if(pil == 4):
                    break

        elif(opsi == 2):
            while True:
                print('1. Input Book')
                print('2. Search Book')
                print('3. Check Stock')
                print('4. Back to Main')
                pil = int(input('Masukkan pilihan : '))
                if(pil == 1):
                    print('1. Printed Book')
                    print("2. Ebook")
                    choice = int(input('Masukkan pilihan : '))
                    if(choice == 1):
                        id = input('ID Buku : ')
                        title = input('Judul Buku : ')
                        author = input('Penulis : ')
                        page = input('Jumlah Halaman : ')
                        edition = input('Edisi : ')
                        genre = input('Genre : ')
                        price = input('Harga : ')
                        amount = int(input('Jumlah buku : '))
                        cover = input('Cover(Hard/Soft) : ')
                        isbn = input('ISBN : ')
                        book1 = printedBook(id, title, author, page, edition, genre, price, amount, cover, isbn)
                        bookstore.inputBookPrinted(book1)

                    elif(choice == 2):
                        id = input('ID Buku : ')
                        title = input('Judul Buku : ')
                        author = input('Penulis : ')
                        page = input('Jumlah Halaman : ')
                        edition = input('Edisi : ')
                        genre = input('Genre : ')
                        price = input('Harga : ')
                        format = input('File Format : ')
                        size = input('File size : ')
                        licenseKey = input('License Key : ')
                        book2 = Ebook(id, title, author, page, edition, genre, price, format, size, licenseKey)
                        bookstore.inputEBook(book2)

                elif(pil == 2):
                    search_term = input('Enter search term: ')
                    bookstore.searchBook(search_term)

                elif(pil == 3):
                    cekStock = input('Masukkan ID buku yang ingin dicek stocknya : ')
                    bookstore.cekStock(cekStock)

                elif(pil == 4):
                    break

        elif(opsi == 3):
            print('Thank you for visiting 😊')
            break

        else:
            print('No option in choices')
            continue


main()
