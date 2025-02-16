## Update a book
** Command:**
 book.title = "1988"
>>> book.save()
>>> updated_book = Book.objects.get(id=1)
>>> print(updated_book.title)


** Expected Output:**
1988