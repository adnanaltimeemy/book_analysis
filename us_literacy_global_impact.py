# 🌐 us_literacy_global_impact.py
# Simulating global dependencies on U.S. youth literacy trends

import matplotlib.pyplot as plt

# ------------------------------------------------
# Define U.S. literacy scenario (decline or growth)
# ------------------------------------------------

def us_literacy_projection(start=79, years=30, annual_change=-0.5):
    trend = [start]
    for _ in range(years):
        next_val = max(0, min(trend[-1] + annual_change, 100))
        trend.append(next_val)
    return trend

# ------------------------------------------------
# Define dependent sectors globally (normalized scale)
# ------------------------------------------------

sectors = {
    "Global AI Innovation": 0.4,     # 40% dependency on U.S. literacy
    "Scientific Research": 0.35,
    "Open Source Contribution": 0.3,
    "Tech Entrepreneurship": 0.25,
    "Digital Publishing": 0.2
}

# ------------------------------------------------
# Simulate global impact as function of US literacy
# ------------------------------------------------

def global_sector_output(us_trend, dependency):
    base = 100  # Base productivity index
    results = []
    for year, us_lit in enumerate(us_trend):
        factor = us_lit / 100  # Normalize to [0, 1]
        impact = base * (1 - dependency * (1 - factor))
        results.append(impact)
    return results

# ------------------------------------------------
# Plotting function
# ------------------------------------------------

def plot_global_impact(us_trend, sectors):
    plt.figure(figsize=(12, 7))
    for sector, dep in sectors.items():
        output = global_sector_output(us_trend, dep)
        plt.plot(range(2020, 2020 + len(output)), output, label=sector)

    plt.title("📉 Global Sector Productivity Impact from U.S. Youth Literacy Decline")
    plt.xlabel("Year")
    plt.ylabel("Global Sector Productivity Index (Base: 100)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ------------------------------------------------
# Run simulation
# ------------------------------------------------

if __name__ == "__main__":
    us_decline = us_literacy_projection(start=79, years=30, annual_change=-0.5)
    plot_global_impact(us_decline, sectors)
