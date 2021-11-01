from books import Books
books = []
f = open("books.txt")
readbooks = f.readlines()
f.close()
for i in range(len(readbooks)):
    readbooks[i] = readbooks[i].replace("\n", "")
    readbooks[i] = readbooks[i].split("@")
    books.append(Books(readbooks[i][0], readbooks[i][1], readbooks[i][2], int(readbooks[i][3]), int(readbooks[i][4])))

print(Books.filtr(books,"Luts",2010))