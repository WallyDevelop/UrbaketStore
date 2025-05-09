from app.models import producto, cliente

class Cart():
    def __init__(self, request):
        self.session = request.session

        self.request = request
        
        cart = self.session.get("session_key")
        if "session_key" not in request.session:
            cart=self.session["session_key"] = {}
        
        self.cart = cart

    def db_add (self, product, quantity):
        product_id =str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else: 
            self.cart[product_id] = str(product_qty)
            self.session.modified = True

            if self.request.user.is_authenticated:
                currente_user=cliente.objects.filter(user__id=self.request.user.id)
                carty = str(self.cart)
                carty = carty.replace("\'","\"")
                currente_user.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id =str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else: 
            self.cart[product_id] = str(product_qty)
            self.session.modified = True

            if self.request.user.is_authenticated:
                currente_user=cliente.objects.filter(user__id=self.request.user.id)
                carty = str(self.cart)
                carty = carty.replace("\'","\"")
                currente_user.update(old_cart=str(carty))
            
    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids =  self.cart.keys()
        products = producto.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True 

        # Lo usamos para guardar todo los cambios que se hagan en el carrito mientras estemos autenticados. 
        if self.request.user.is_authenticated:
            currente_user=cliente.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            currente_user.update(old_cart=str(carty))

    def cart_total(self):
        product_ids = self.cart.keys()
        products = producto.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            value = int(value)
            for produ in products:
                if produ.id == key:
                    total += (produ.precio * value)
        return total
    
    