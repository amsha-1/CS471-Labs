from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    name =request.GET.get("name")or 'world!'
 #   return render(request,"bookmodule/index.html", {"name":name})

def index2(request,vall=0):
    return HttpResponse("value1= "+str(vall))

#def viewbook(request, bookId):
#    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 #   book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 #   targetBook = None
  #  if book1['id'] == bookId: targetBook = book1
   # if book2['id'] == bookId: targetBook = book2
   # context = {'book':targetBook}
   # return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
