#Function to show the cost of ground shipping based on weight:
def cost_ground_shipping(weight):
  if weight <= 2:
    return (1.5 * weight) + 20
  elif (weight <= 6) and (weight > 2):
    return (3 * weight) + 20
  elif (weight <= 10) and (weight > 6):
    return (4 * weight) + 20
  elif weight > 10:
    return (4.75 * weight) + 20
  
#The flat costing rate of premium ground shipping  
cost_premium_shipping = 125

#Function to show the cost of drone shipping based on weight:
def cost_drone_shipping(weight):
  if weight <= 2:
    return (4.5 * weight)
  elif (weight <= 6) and (weight > 2):
    return (9 * weight) 
  elif (weight <= 10) and (weight > 6):
    return (12 * weight) 
  elif weight > 10:
    return (14.25 * weight) 

#Function to send to terminal the cost of each shipping type and which is the cheapest
def cheapest_type(weight):
  print('The cost of ground shipping is ' + str(cost_ground_shipping(weight)))
  print('The cost of drone shipping is ' + str(cost_drone_shipping(weight)))
  print('The cost of premium shipping is ' + str(cost_premium_shipping))
  if cost_drone_shipping(weight) < cost_ground_shipping(weight):
    return print('Drone shipping is the cheapest')
  if (cost_ground_shipping(weight) < cost_drone_shipping(weight)) and (cost_ground_shipping(weight) < cost_premium_shipping):
    return print('Regular ground shipping is the cheapest')
  else:
    return print('Premium ground shipping is the cheapest')

#User input the weight of their item, replace X with the real weight
cheapest_type(X)

