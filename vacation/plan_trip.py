def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  rent = days * 40
  if days >= 7:
    rent -= 50
  elif days >= 3 and days <= 6:
    rent -= 20
  return rent

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) 
  + spending_money + plane_ride_cost(city)

print type(rental_car_cost(5))
print type(hotel_cost(4))
print type(plane_ride_cost("Los Angeles"))

print trip_cost("Lost Angeles", 5, 600)
  