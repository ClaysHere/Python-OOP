from partClass import *


if __name__ == "__main__":
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
                    search_term = input('Enter book title: ')
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
                    search_term = input('Enter book title: ')
                    bookstore.searchBook(search_term)

                elif(pil == 3):
                    cekStock = input('Masukkan ID buku yang ingin dicek stocknya : ')
                    bookstore.cekStock(cekStock)

                elif(pil == 4):
                    break

        elif(opsi == 3):
            print('Thank you for visiting 😊')
            print()
            break

        else:
            print('No option in choices')
            continue
    
    print('Testing Part - Just for testing')
    unittest.main()
