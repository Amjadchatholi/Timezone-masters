from django.shortcuts import render
from store.models import Product,ReviewRating

# Create your views here.
def index(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
        
    }


    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html') 

def contact(request):
    return render(request, 'contact.html')           

def blog2(request):
    return render(request, 'blog-details.html')   
