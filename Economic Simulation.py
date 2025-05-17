def estimate_future_costs(youth_population, illiteracy_percent, cost_per_illiterate):
    illiterate_youth = youth_population * (illiteracy_percent / 100)
    total_cost = illiterate_youth * cost_per_illiterate
    print(f"\nProjected Illiterate Youth in 2050: {illiterate_youth:,.0f}")
    print(f"Estimated Economic Impact: ${total_cost:,.0f} USD/year")

# Assume 90 million youth in US by 2050, $10,000 annual loss per illiterate person
estimate_future_costs(youth_population=90_000_000, illiteracy_percent=36, cost_per_illiterate=10000)
# This function estimates the future costs associated with illiteracy in the US.
# It calculates the number of illiterate youth and the economic impact based on a given cost per illiterate person.                     
# The function takes three parameters: youth_population, illiteracy_percent, and cost_per_illiterate.
# The youth_population is the projected number of youth in the US by 2050,
# the illiteracy_percent is the percentage of youth that are expected to be illiterate,         
# and the cost_per_illiterate is the estimated annual economic loss per illiterate person.
# The function calculates the number of illiterate youth by multiplying the youth_population by the illiteracy_percent divided by 100.
# It then calculates the total cost by multiplying the number of illiterate youth by the cost_per_illiterate.
# Finally, it prints the projected number of illiterate youth and the estimated economic impact.    
# The function is called with the projected youth population of 90 million, an illiteracy rate of 36%, and a cost of $10,000 per illiterate person.
# The function is called with the projected youth population of 90 million, an illiteracy rate of 36%, and a cost of $10,000 per illiterate person. 
# The function is called with the projected youth population of 90 million, an illiteracy rate of 36%, and a cost of $10,000 per illiterate person.
# The function is called with the projected youth population of 90 million, an illiteracy rate of 36%, and a cost of $10,000 per illiterate person.
# The function is called with the projected youth population of 90 million, an illiteracy rate of 36%, and a cost of $10,000 per illiterate person.