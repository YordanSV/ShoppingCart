class ShoppingCart:
     

     def __init__(self):
        self.items = []
    

     def add_item(self, item):
         self.items.append(item)

     def total_price(self):
         return sum(item.price  for item in self.items)
     
     def remove_item(self, code):
         self.items = [item for item in self.items if item.code != code]
    
     def display_items(self):
         for item in self.items:
             print(item)
            
    
    