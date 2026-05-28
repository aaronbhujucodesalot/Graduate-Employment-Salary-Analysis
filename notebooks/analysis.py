import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "graduate_outcomes_sample.csv"
IMG = BASE / "images"
IMG.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

print("Dataset shape:", df.shape)
print(df.head())

# KPI table: Year 5 outcomes
year5 = df[df["years_after_graduation"] == 5].copy()
year5["opportunity_score"] = (year5["median_annual_income_nzd"] / 1000) * (year5["employment_rate_pct"] / 100)

print("\nTop fields by income after 5 years")
print(year5.sort_values("median_annual_income_nzd", ascending=False)[
    ["field_of_study", "median_annual_income_nzd", "employment_rate_pct"]
])

print("\nTop fields by opportunity score")
print(year5.sort_values("opportunity_score", ascending=False)[
    ["field_of_study", "median_annual_income_nzd", "employment_rate_pct", "opportunity_score"]
])

# Chart 1: Median income after 5 years
top_income = year5.sort_values("median_annual_income_nzd", ascending=True)
plt.figure(figsize=(10, 6))
plt.barh(top_income["field_of_study"], top_income["median_annual_income_nzd"])
plt.title("Median Annual Income by Field of Study - 5 Years After Graduation")
plt.xlabel("Median Annual Income (NZD)")
plt.ylabel("Field of Study")
plt.tight_layout()
plt.savefig(IMG / "median_income_year5.png", dpi=200)
plt.close()

# Chart 2: Employment vs income
plt.figure(figsize=(8, 6))
plt.scatter(year5["employment_rate_pct"], year5["median_annual_income_nzd"])
for _, row in year5.iterrows():
    plt.annotate(row["field_of_study"].split()[0], 
                 (row["employment_rate_pct"], row["median_annual_income_nzd"]),
                 fontsize=8)
plt.title("Employment Rate vs Median Income - 5 Years After Graduation")
plt.xlabel("Employment Rate (%)")
plt.ylabel("Median Annual Income (NZD)")
plt.tight_layout()
plt.savefig(IMG / "employment_vs_income_year5.png", dpi=200)
plt.close()

# Chart 3: Income growth
pivot = df.pivot(index="field_of_study", columns="years_after_graduation", values="median_annual_income_nzd")
growth = pivot[[1, 9]].copy()
growth["growth_pct"] = ((growth[9] - growth[1]) / growth[1] * 100).round(1)
growth = growth.sort_values("growth_pct", ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(growth.index, growth["growth_pct"])
plt.title("Income Growth from Year 1 to Year 9 After Graduation")
plt.xlabel("Income Growth (%)")
plt.ylabel("Field of Study")
plt.tight_layout()
plt.savefig(IMG / "income_growth_year1_to_year9.png", dpi=200)
plt.close()

print("\nCharts saved in /images")