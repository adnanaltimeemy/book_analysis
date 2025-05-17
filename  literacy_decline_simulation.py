# 🌍 Global Implications of Youth Literacy Decline by 2050

import matplotlib.pyplot as plt

# ------------------------------------------
# Step 1: Define country profiles
# ------------------------------------------

countries = {
    "USA": {"literacy_2020": 79, "gdp": 21.0, "population": 331},
    "UK": {"literacy_2020": 82, "gdp": 3.1, "population": 67},
    "India": {"literacy_2020": 74, "gdp": 3.7, "population": 1400},
    "Nigeria": {"literacy_2020": 62, "gdp": 0.5, "population": 220},
    "Brazil": {"literacy_2020": 89, "gdp": 2.0, "population": 213}
}

literacy_decline_rate = -0.4  # Decline per year (percent)
years = 30  # From 2020 to 2050

# ------------------------------------------
# Step 2: Simulate literacy decline over time
# ------------------------------------------

def simulate_decline(start_literacy, decline_rate, years):
    rates = [start_literacy]
    for _ in range(years):
        next_val = rates[-1] + decline_rate
        next_val = max(0, min(next_val, 100))  # Keep within 0–100%
        rates.append(next_val)
    return rates

# ------------------------------------------
# Step 3: Model impact for each country
# ------------------------------------------

def model_global_impact(countries, decline_rate, years):
    results = {}
    for country, data in countries.items():
        literacy_trend = simulate_decline(data["literacy_2020"], decline_rate, years)
        final_lit = literacy_trend[-1]
        illiteracy_percent = 100 - final_lit
        illiterate_millions = (illiteracy_percent / 100) * data["population"]

        gdp_loss = 0.02 * illiterate_millions  # $20B per 100M illiterate
        misinformation_score = illiteracy_percent / 100  # Normalized
        inequality_index_rise = illiteracy_percent * 0.1  # Synthetic score
        stem_loss = illiteracy_percent * 0.5  # % STEM workforce lost

        results[country] = {
            "final_literacy": round(final_lit, 2),
            "illiterate_millions": round(illiterate_millions, 1),
            "gdp_loss_est_billion": round(gdp_loss, 2),
            "misinfo_risk_score": round(misinformation_score, 2),
            "inequality_rise_index": round(inequality_index_rise, 2),
            "STEM_workforce_loss_%": round(stem_loss, 2)
        }
    return results

# ------------------------------------------
# Step 4: Print summary
# ------------------------------------------

def print_global_summary(results):
    print("🌍 Global Literacy Decline Projection to 2050\n")
    for country, data in results.items():
        print(f"🟢 {country}")
        print(f"  📘 Final Literacy Rate: {data['final_literacy']}%")
        print(f"  🧑‍🤝‍🧑 Illiterate Population: {data['illiterate_millions']} million")
        print(f"  💰 GDP Loss Estimate: ${data['gdp_loss_est_billion']}B")
        print(f"  🧠 Misinformation Vulnerability: {data['misinfo_risk_score']}/1.0")
        print(f"  ⚖️ Inequality Rise Index: {data['inequality_rise_index']}")
        print(f"  👩‍🔬 STEM Workforce Loss: {data['STEM_workforce_loss_%']}%")
        print("-" * 50)

# ------------------------------------------
# Step 5: Visualization
# ------------------------------------------

def plot_country_literacy_trends(countries, years, decline_rate):
    plt.figure(figsize=(10, 6))
    for country, data in countries.items():
        rates = simulate_decline(data["literacy_2020"], decline_rate, years)
        plt.plot(range(2020, 2020 + years + 1), rates, label=country)
    plt.title("Youth Literacy Rate Projections (2020–2050)")
    plt.ylabel("Literacy Rate (%)")
    plt.xlabel("Year")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ------------------------------------------
# Step 6: Run simulation
# ------------------------------------------

if __name__ == "__main__":
    results_2050 = model_global_impact(countries, literacy_decline_rate, years)
    print_global_summary(results_2050)
    plot_country_literacy_trends(countries, years, literacy_decline_rate)
