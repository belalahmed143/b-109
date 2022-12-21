from .models import Category

def category(request):
    cate = Category.objects.filter(parent=None)
    context ={
        'cate':cate
    }
    return context