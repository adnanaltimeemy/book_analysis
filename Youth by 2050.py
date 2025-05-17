import matplotlib.pyplot as plt

def simulate_youth_literacy_decline(start_literacy_rate, years, decline_rate=0.5):
    """
    Simulates literacy decline among youth over time
    """
    literacy_rates = []
    for year in range(years + 1):
        rate = start_literacy_rate - year * decline_rate
        literacy_rates.append(max(rate, 0))  # Prevent negative values

    return literacy_rates

def plot_youth_literacy_projection(start_year, start_rate, years=30):
    projected = simulate_youth_literacy_decline(start_rate, years)
    years_list = [start_year + i for i in range(len(projected))]

    plt.figure(figsize=(10, 6))
    plt.plot(years_list, projected, marker='o', linestyle='-', color='darkred')
    plt.title("Projected Decline in Youth Literacy (US, 2020–2050)")
    plt.xlabel("Year")
    plt.ylabel("Youth Literacy Rate (%)")
    plt.grid(True)
    plt.axhline(70, color='gray', linestyle='--', label='Critical Threshold')
    plt.legend()
    plt.show()

plot_youth_literacy_projection(start_year=2020, start_rate=79, years=30)
