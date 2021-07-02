shipping

def shipping_cost_per_ground(weight):
  
  if weight <=2:
    shipping_ground = 1.50
  elif weight <=6:
   shipping_ground = 3.00
  elif weight <=10:
    shipping_ground = 4.00
  else:
    shipping_ground = 4.75
    
  return 20 + (shipping_ground * weight)
  print(shipping_cost_per_ground(3.5))
  
  premium = 125
  
  def shipping_cost_per_drone(weight):
  
  if weight <=2:
    shipping_drone = 4.50
  elif weight <=6:
   shipping_drone = 9.00
  elif weight <=10:
    shipping_drone = 12.00
  else:
    shipping_drone = 14.25
    
  return shipping_drone * weight
  print(shipping_cost_per_drone(2.5))
  
  
  
  
  
    
