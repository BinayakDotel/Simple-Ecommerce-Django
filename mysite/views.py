from unicodedata import category
from django.shortcuts import render
from .DatabaseManager import DataManager 

# Create your views here.
def home(request):
    data_manager= DataManager()
    categories= data_manager.get_all_category()
    products= data_manager.get_all_products()
    
    cat_list=[]
    prod_list=[]
    
    for category in categories:
        cat_list.append(category.category)
        
    for product in products:
        prod_list.append(product)
        
    context= {"categories":cat_list, "products":prod_list}
    print(context)
    
    return render(request, "index.html", context)

def category(request, category):
    data_manager= DataManager()
    categories= data_manager.get_all_category()
    products= data_manager.get_products_by_category(category=category)
    
    cat_list=[]
    prod_list=[]
    
    for category in categories:
        cat_list.append(category.category)
        
    for product in products:
        prod_list.append(product)
        
    context= {"categories":cat_list, "products":prod_list}
    print(context)
    
    return render(request, "index.html", context)

def product(request, product_name, product_id):
    #firebase= FirebaseManager("ecommerce-8183b-firebase-adminsdk-pbglr-b054a3c8ff.json")
    #firebase.get_specific_product(category, product_name)
    
    data_manager= DataManager()
    print(f"THIS IS PRODUCT NAME :: {product_name} and {product_id}")
    p= data_manager.get_product_by_title(title=product_name, product_id=product_id)
    
    return render(request, "product.html", {"product":p})

def addProduct(request):
    data_manager= DataManager()
    categories= data_manager.get_all_category()
    cat_items= []
    for item in categories:
        cat_items.append(item.category)
        
    if request.method=="POST":
        data_manager= DataManager()
        category= request.POST.get('category')
        product_name= request.POST.get('product_name')
        price= request.POST.get('price')
        
        success= data_manager.add_product(category, product_name, price)
        
        return render(request, "add_product.html", {"status":success, "categories":cat_items})
    
    print({"categories":cat_items})
    return render(request, 'add_product.html', {"status": None, "categories":cat_items})

def addCategory(request):   
    if request.method=="POST":
        data_manager= DataManager()
        category= request.POST.get('category')
        success= data_manager.add_category(category=category)

        return render(request, 'add_category.html', {"status":success})

    return render(request, 'add_category.html', {})

def test(request):
    #firebase= FirebaseManager("ecommerce-8183b-firebase-adminsdk-pbglr-b054a3c8ff.json")
    #data= firebase.get_all_product()

    return render(request, "test.html", {"values":"data"})