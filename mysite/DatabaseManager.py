from .models import *

class DataManager:
    def add_category(self, category):
        try:
            c= Category.objects.get(category=category)
            print(c.category)
            print("Category already exists!")
            return False
        except:
            c= Category(category=category)
            c.save()
            print(f"Added New Category {category}")
            return True
        
    def add_product(self, category, product_name, price):
        try:
            c= Category.objects.get(category=category)
            
            p= Product(title=product_name, price=price, c_id=c)
            p.save()
            
            return True
        except:
            print("Category does not exists!")
            return False
        
    def get_all_category(self):
        return Category.objects.all()
    
    def get_all_products(self):
        return Product.objects.all()
    
    def get_products_by_category(self, category):
        c= Category.objects.get(category=category)
        return Product.objects.filter(c_id=c.category_id)
        
    def get_product_by_title(self, title, product_id):
        print(f"THIS IS PRODUCT NAME :: {title} and {product_id} in DB")
        p= Product.objects.get(product_id=product_id, title=title)
        return p