-- Graduate Employment & Salary Analysis
-- SQLite-compatible queries

-- 1. Top fields by median income five years after graduation
SELECT
    field_of_study,
    field_group,
    median_annual_income_nzd,
    employment_rate_pct
FROM graduate_outcomes
WHERE years_after_graduation = 5
ORDER BY median_annual_income_nzd DESC;

-- 2. Best balance of employment and income after five years
SELECT
    field_of_study,
    median_annual_income_nzd,
    employment_rate_pct,
    ROUND((median_annual_income_nzd / 1000.0) * (employment_rate_pct / 100.0), 2) AS opportunity_score
FROM graduate_outcomes
WHERE years_after_graduation = 5
ORDER BY opportunity_score DESC;

-- 3. Income growth from Year 1 to Year 9
WITH income_growth AS (
    SELECT
        field_of_study,
        MAX(CASE WHEN years_after_graduation = 1 THEN median_annual_income_nzd END) AS income_year_1,
        MAX(CASE WHEN years_after_graduation = 9 THEN median_annual_income_nzd END) AS income_year_9
    FROM graduate_outcomes
    GROUP BY field_of_study
)
SELECT
    field_of_study,
    income_year_1,
    income_year_9,
    income_year_9 - income_year_1 AS income_growth_nzd,
    ROUND(100.0 * (income_year_9 - income_year_1) / income_year_1, 1) AS income_growth_pct
FROM income_growth
ORDER BY income_growth_pct DESC;

-- 4. Fields with high further-study rates after one year
SELECT
    field_of_study,
    further_study_rate_pct,
    employment_rate_pct
FROM graduate_outcomes
WHERE years_after_graduation = 1
ORDER BY further_study_rate_pct DESC;

-- 5. Risk view: lower employment and higher jobseeker outcomes after five years
SELECT
    field_of_study,
    employment_rate_pct,
    jobseeker_rate_pct,
    median_annual_income_nzd
FROM graduate_outcomes
WHERE years_after_graduation = 5
ORDER BY employment_rate_pct ASC, jobseeker_rate_pct DESC;