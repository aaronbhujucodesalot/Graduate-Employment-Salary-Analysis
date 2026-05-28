# Graduate Employment & Salary Analysis

## Project Overview
This project analyses graduate employment and salary outcomes by field of study in New Zealand. The goal is to identify which study areas lead to stronger labour-market outcomes, which fields have higher further-study pathways, and how income changes several years after graduation.

This is designed as a portfolio project for data analyst, business analyst, consulting, and graduate technology roles.

## Business Questions
1. Which fields of study have the highest median annual income after graduation?
2. Which fields provide the best balance between employment rate and income?
3. How does graduate income change from one to nine years after graduation?
4. Which fields have high further-study rates rather than immediate employment?
5. Which fields appear to carry weaker short-term labour-market outcomes?

## Data Source
The official recommended source is the Tertiary Education Commission's Post-study Outcomes data.

TEC states that the data covers graduate destinations and earnings after study, and can be filtered by field of study, demographic information, region, and provider. It includes outcomes 1, 3, 5, 7 and 9 years after graduation.

Important: the CSV included in this repository is a demo sample dataset created for portfolio development. For a production-ready version, replace it with the official TEC national XLSX file.

Official source page:
https://www.tec.govt.nz/sector-governance-and-performance/monitoring-and-auditing-performance/sector-performance-data/post-study-outcomes/data-on-post-study-outcomes-for-tertiary-education-graduates

Technical notes:
https://www.tec.govt.nz/sector-governance-and-performance/monitoring-and-auditing-performance/sector-performance-data/post-study-outcomes/post-study-outcomes-data-technical-information

## Tools Used
- Python
- Pandas
- Matplotlib
- SQLite
- SQL
- Power BI / Tableau dashboard design

## Repository Structure
```text
graduate_employment_salary_analysis/
├── data/
│   ├── graduate_outcomes_sample.csv
│   └── graduate_outcomes.db
├── notebooks/
│   └── analysis.py
├── sql/
│   └── analysis_queries.sql
├── dashboard/
│   └── dashboard_design.md
├── images/
├── report/
│   └── executive_summary.md
└── README.md
```

## Key Metrics
- Median annual income
- Employment rate
- Further-study rate
- Jobseeker rate
- Overseas rate
- Opportunity score = income adjusted by employment rate

## Example Insights
- Medicine, engineering, and information technology produce the strongest income outcomes in the sample dataset.
- Natural and physical sciences show a high further-study pathway, meaning immediate employment alone may understate their long-term value.
- Creative arts has weaker income and employment outcomes in the sample dataset, suggesting graduates may face more variable labour-market pathways.
- Opportunity score is useful because high salary alone does not always mean a large share of graduates are employed.

## How to Run
1. Install dependencies:
```bash
pip install pandas matplotlib
```

2. Run the analysis:
```bash
python notebooks/analysis.py
```

3. Run the SQL queries:
```bash
sqlite3 data/graduate_outcomes.db < sql/analysis_queries.sql
```

## Dashboard Pages
1. Executive Overview
2. Income by Field
3. Employment vs Income
4. Further Study and Jobseeker Risk
5. Long-term Income Growth

## CV Bullet Points
- Built an end-to-end graduate outcomes analytics project using Python, SQL, and dashboard design to compare salary and employment outcomes across fields of study.
- Created reusable SQL queries and Python visualisations to identify high-income fields, employment-risk areas, and long-term income growth patterns.
- Developed an executive-style dashboard framework translating graduate labour-market data into actionable education and career insights.

## Data Source Note:
This repository contains a portfolio dataset structured around publicly documented measures from the New Zealand Tertiary Education Commission (TEC) post-study outcomes framework. The included dataset is for demonstration and portfolio purposes. The project can be adapted to use official TEC datasets where available.
