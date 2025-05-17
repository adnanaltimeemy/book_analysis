def simulate_future_loss(country_data, years=10, annual_change_rate_percent=-1.5):
    """
    Simulate future economic cost due to literacy over a number of years.
    annual_change_rate_percent < 0 means literacy improves, reducing cost.
    """
    current_cost = country_data.annual_cost_usd
    print(f"Starting annual cost for {country_data.name}: ${current_cost:,.0f}")
    
    for year in range(1, years+1):
        # Literacy improvement reduces costs, decline increases costs
        current_cost *= (1 + annual_change_rate_percent / 100)
        print(f"Year {year}: Estimated annual cost = ${current_cost:,.0f}")

    print(f"After {years} years, projected annual cost for {country_data.name} is ${current_cost:,.0f}")

# Simulate 10 years for the US assuming literacy improves by 1.5% per year
simulate_future_loss(countries[0], years=10, annual_change_rate_percent=-1.5)

