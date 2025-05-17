"""
Literacy Impact Analysis
------------------------
This script models the economic and social consequences of literacy rates
in the United States, United Kingdom, and globally, based on data and facts.

Data sources and assumptions:
- US literacy cost: $2.2 trillion annually
- UK literacy cost: £81 billion annually
- Global illiteracy cost: $1.19 trillion annually
- Literacy rates, unemployment, income loss percentages are modeled per source data.
"""

from dataclasses import dataclass

@dataclass
class CountryLiteracyData:
    name: str
    literacy_rate_percent: float
    population_millions: float
    annual_cost_usd: float  # Cost of low literacy to economy in USD
    unemployment_rate_increase_percent: float
    income_loss_percent: float

@dataclass
class LiteracyImpact:
    country_data: CountryLiteracyData

    def affected_population(self) -> float:
        """Estimate the number of people affected by low literacy."""
        illiterate_percent = 100 - self.country_data.literacy_rate_percent
        affected = self.country_data.population_millions * illiterate_percent / 100
        print(f"{self.country_data.name}: Estimated illiterate population = {affected:.2f} million")
        return affected

    def income_loss_per_affected(self) -> float:
        """Estimate average income loss per affected individual."""
        # Using a hypothetical average income for each country (in USD)
        # For simplification:
        avg_income_us = 65000
        avg_income_uk = 43000
        avg_income_global = 10000  # estimated global average

        avg_income = {
            'United States': avg_income_us,
            'United Kingdom': avg_income_uk,
            'Global': avg_income_global
        }.get(self.country_data.name, avg_income_global)

        loss = avg_income * self.country_data.income_loss_percent / 100
        print(f"{self.country_data.name}: Average income loss per affected individual = ${loss:.2f}")
        return loss

    def total_income_loss(self) -> float:
        """Calculate total income loss due to literacy issues."""
        affected = self.affected_population() * 1_000_000  # convert to individuals
        loss_per_person = self.income_loss_per_affected()
        total_loss = affected * loss_per_person
        print(f"{self.country_data.name}: Total income loss due to low literacy = ${total_loss:,.2f}")
        return total_loss

    def unemployment_impact(self) -> float:
        """Estimate additional unemployed population due to literacy."""
        affected = self.affected_population() * 1_000_000
        additional_unemployed = affected * self.country_data.unemployment_rate_increase_percent / 100
        print(f"{self.country_data.name}: Additional unemployed individuals due to low literacy = {int(additional_unemployed):,}")
        return additional_unemployed

    def economic_impact_percent_gdp(self) -> float:
        """Estimate % of GDP lost due to literacy issues."""
        # Assume GDP for simplification (in billions USD)
        gdp_values = {
            'United States': 25_000,  # 2024 approx in billions
            'United Kingdom': 3_200,
            'Global': 105_000
        }
        gdp = gdp_values.get(self.country_data.name, 0)
        if gdp == 0:
            print(f"{self.country_data.name}: GDP data not available.")
            return 0

        # Using annual cost in USD to estimate % GDP lost
        percent_gdp_loss = (self.country_data.annual_cost_usd / (gdp * 1_000_000_000)) * 100
        print(f"{self.country_data.name}: Estimated % GDP loss due to literacy = {percent_gdp_loss:.3f}%")
        return percent_gdp_loss

def main():
    # Data based on your info and public data
    us_data = CountryLiteracyData(
        name="United States",
        literacy_rate_percent=46,  # 54% adults below proficiency
        population_millions=333,
        annual_cost_usd=2.2e12,
        unemployment_rate_increase_percent=100,  # 2x more likely unemployed = 100% increase
        income_loss_percent=60
    )

    uk_data = CountryLiteracyData(
        name="United Kingdom",
        literacy_rate_percent=80,  # 1 in 5 functionally illiterate = 80% proficient
        population_millions=67,
        annual_cost_usd=81e9 * 1.3,  # converting £81 billion to USD approx at 1.3 rate
        unemployment_rate_increase_percent=50,  # estimate
        income_loss_percent=50  # conservative estimate
    )

    global_data = CountryLiteracyData(
        name="Global",
        literacy_rate_percent=86,  # approximate global literacy ~86%
        population_millions=8000,
        annual_cost_usd=1.19e12,
        unemployment_rate_increase_percent=20,  # global average
        income_loss_percent=40
    )

    print("\nLiteracy Impact Analysis Report\n" + "="*35)
    for data in [us_data, uk_data, global_data]:
        impact = LiteracyImpact(data)
        print(f"\nAnalyzing {data.name}...\n" + "-"*25)
        impact.affected_population()
        impact.income_loss_per_affected()
        impact.total_income_loss()
        impact.unemployment_impact()
        impact.economic_impact_percent_gdp()

if __name__ == "__main__":
    main()
