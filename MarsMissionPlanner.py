def mars(distance, speed):
    time =distance / speed
    return round(time, 2)

def cost(distance, usage, price_per_liter):
    cost = (distance * usage) * price_per_liter
    return cost

pathfinder_speed = 40000
persverance_speed = 75000
starship_speed = 120000

distance_to_mars = 225000000
usage_per_km = 0.3
price_per_liter = 1.8

#pathfinder
pathfinder_time = mars(distance_to_mars, pathfinder_speed)
pathfinder_cost = cost(distance_to_mars, usage_per_km, price_per_liter)

#persverance
persverance_time = mars(distance_to_mars, persverance_speed)
persverance_cost = cost(distance_to_mars, usage_per_km, price_per_liter)

#starship
starship_time = mars(distance_to_mars, starship_speed)
starship_cost = cost(distance_to_mars, usage_per_km, price_per_liter)

print("Pathfinder")
print(f"Time to Mars: {pathfinder_time}")
print(f"Cost of fuel: {pathfinder_cost}")
print("\nPerseverance")
print(f"Time to Mars: {persverance_time}")
print(f"Cost of fuel: {persverance_cost}")
print("\nStarship")
print(f"Time to Mars: {starship_time}")
print(f"Cost of fuel: {starship_cost}")