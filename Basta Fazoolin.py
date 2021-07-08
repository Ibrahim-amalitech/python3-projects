from datetime import time
class Menu:
 def __init__(self,name,items,start_time,end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time

 def __repr__(self):
    return self.name +" menu is available from {start_time} to {end_time}".format(start_time=self.start_time,end_time=self.end_time)

 def calculate_bill(self,purchased_items):
    self.purchased_items=purchased_items
    purchase_list=[item_name for item_name in self.purchased_items]
    total_price=0
    for purchase in purchase_list:
      total_price+=self.items[purchase]
    return total_price




# brunch menu
bruch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch=Menu("brunch",bruch_items,time(11,0),time(16,0))

# early_bird menu
early_bird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird=Menu("early_bird", early_bird_items,time(15,0),time(10,0))

# dinner menu
dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner=Menu("dinner",dinner_items,time(17,0),time(23,0))

# kids menu
kids_items={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids=Menu("kids",kids_items,time(11,0),time(21,0))

print(brunch)

# bill for brunch order
brunch_bill=brunch.calculate_bill(["pancakes","home fries","coffee"])
print(brunch_bill)

# bill for early_bird
early_bird_bill=early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)"])
print(early_bird_bill)
menus=[brunch,early_bird,dinner,kids]

class Franchise:
  def __init__(self,address,menus):
   self.address=address
   self.menus=menus
  def __repr__(self):
     return "Our flapship store is located at {address}".format(address=self.address)
  def available_menus(self,time):
    self.time=time
    available_menu_list=[]
    for item in self.menus:
      if self.time >=item.start_time and self.time <= item.end_time:
        available_menu_list.append(item)
    return available_menu_list
        
            
        
     

# franchises
flagship_store  = Franchise("1232 West End Road",menus)
print(flagship_store )
new_installment= Franchise("12 East Mulberry Street",menus)
print(new_installment)

# Tell customers what they can order
print(new_installment.available_menus(time(12,0)))
print(new_installment.available_menus(time(17,0)))
# create business
arepas_menu={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
class Business:
  def __init__(self,name,franchises):
     self.name=name
     self.franchises=franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa = Business("Take a' Arepa", [arepas_place])
print(arepa.franchises)




