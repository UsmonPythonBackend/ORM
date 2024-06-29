from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    books = Book.objects.all()
    context = {'all_books': books}
    return render(request, 'books.html', context=context)

def authors(request):
    authors = Author.objects.all()
    context = {'all_authors': authors}
    return render(request, 'authors.html', context=context)

