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

    def inputBookPrinted(self, book):
        try:
            if(self.cekKode(book.id) and self.cekJumlahHalaman(book.page) and self.cekHarga(book.price)):
                self.listBookPrinted.append(book)
                print(f"Book with ID {book.id} successfully added to the catalog.")
            
        except ValueError as e:
            print(f"Error: {e}")

    def inputEBook(self, book):
        try:
            if(self.cekEbook(book.id) and self.cekJumlahHalaman(book.page) and self.cekHarga(book.price)):
                self.listEbook.append(book)
                print(f"Book with ID {book.id} successfully added to the catalog.")
            
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
           if(type(page) != int):
               raise ValueError('Jumlah halaman harus dalam bentuk angka.')
        except ValueError as e:
            print(str(e))
            return False
        return True
    
    def cekHarga(self, price):
        try:
           if(type(price) != int):
               raise ValueError('Harga buku harus dalam bentuk angka.')
        except ValueError as e:
            print(str(e))
            return False
        return True

    def searchBook(self):
        pass

    def buyBook(self):
        pass

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
                    bookstore.searchBook()
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
                        page = int(input('Jumlah Halaman : '))
                        edition = input('Edisi : ')
                        genre = input('Genre : ')
                        price = int(input('Harga : '))
                        amount = int(input('Jumlah buku : '))
                        cover = input('Cover(Hard/Soft) : ')
                        isbn = input('ISBN : ')
                        book1 = printedBook(id, title, author, page, edition, genre, price, amount, cover, isbn)
                        bookstore.inputBookPrinted(book1)

                    elif(choice == 2):
                        id = input('ID Buku : ')
                        title = input('Judul Buku : ')
                        author = input('Penulis : ')
                        page = int(input('Jumlah Halaman : '))
                        edition = input('Edisi : ')
                        genre = input('Genre : ')
                        price = int(input('Harga : '))
                        format = input('File Format : ')
                        size = input('File size : ')
                        licenseKey = input('License Key : ')
                        book2 = printedBook(id, title, author, page, edition, genre, price, format, size, licenseKey)
                        bookstore.inputEBook(book2)

                elif(pil == 2):
                    pass

                elif(pil == 3):
                    cekStock = input('Masukkan ID buku yang ingin dicek stocknya : ')
                    bookstore.cekStock(cekStock)

                elif(pil == 4):
                    break

        elif(opsi == 3):
            print('Thank you for visiting 😊')
            break


main()
