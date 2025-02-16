## Update a book
** Command:**
 book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> updated_book = Book.objects.get(id=1)
>>> print(updated_book.title)


** Expected Output:**
1988