'''from unittest import result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, db
import os

class FirebaseManager:
    def __init__(self, firebasekey):
        self.path= "./static/firebase_key/ecommerce-8183b-firebase-adminsdk-pbglr-b054a3c8ff.json"
        self.cred= credentials.Certificate(self.path)
        
        try:
            # Initialize the app with a None auth variable, limiting the server's access
            firebase_admin.initialize_app(self.cred, {
                'databaseURL': 'https://ecommerce-8183b-default-rtdb.firebaseio.com/',
                'databaseAuthVariableOverride': None
            })
        except:
            pass
        
    def get_all_category(self):
        ref= db.reference("/Categories")
        return ref.get()

    def get_all_product(self):
        ref= db.reference("/Products")
        result= ref.get()
        print(result)
        
        return result
    
    def get_specific_product(self, category, name):
        doc_ref= db.reference(f"/Products/{category}")
            
        result= doc_ref.order_by_value('name').get()
        print(result)
        
    def get_all_collection(self):
        doc_ref = self.db.collection(u'Products').document(u'Oil')

        doc = doc_ref.get()
        if doc.exists:
            print(f'Document data: {doc.to_dict()}')
        else:
            print(u'No such document!')

    def get_product(self, collection, product_name):
        result= self.db.collection(collection).document(product_name).get()

        if result.exists:
            print(f"DATA FOUND :: {result.to_dict()}")
            return result.to_dict()

        else:
            print("NO DATA")
            return {}
            '''
class FirebaseManager:
    pass