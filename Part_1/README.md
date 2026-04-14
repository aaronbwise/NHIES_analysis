# Part 1: NHIES Food Consumption and Production Analysis

Analysis of the 2015-16 Namibia Household Income and Expenditure Survey (NHIES) to characterize household food consumption and crop production patterns, informing Namibia's food fortification strategy.

## Background

The Namibia Food and Nutrition Security Policy and Implementation Action Plan (2019-2024) includes strategies to implement mandatory fortification of staple foods and condiments. This analysis uses NHIES microdata to understand what foods households consume, where they source them, and how production and consumption patterns vary across demographics.

## Analysis Scope

The main notebook (`nhies_analysis_final.ipynb`) performs the following:

1. **Data cleaning** — Standardizes binary and categorical variables from the NHIES household questionnaire
2. **Variable creation** — Derives indicators for key food groups:
   - Wheat flour, bread, rice, other cereals
   - Oils and fats
   - Spices
   - Production-consumption gaps for maize, mahangu (pearl millet), and sorghum
3. **Weighted and unweighted analysis** — Disaggregated statistics by:
   - Urban/rural residence
   - Region
   - Income level
   - Primary language spoken
   - Age of household head
4. **Visualization** — Charts showing production vs. consumption patterns by demographic group

## Data Sources

- **NHIES household-level data** — Cleaned CSV derived from the 2015-16 survey
- **7-day food diary** — `nhies_files/DRB/Diary_hhV12.dta` (Stata format)
- **Administrative shapefiles** — OCHA Namibia boundaries (ADM0, ADM1, ADM2) in `data_all/shapefiles/`
- **Reference documentation** — NHIES codebooks, manuals, and questionnaire in `nhies_files/`

## Outputs

Results are in `OUTPUT_FINAL/`:

| Subdirectory | Contents |
|---|---|
| `Charts/` | 30 SVG visualizations — production/consumption by region, income, language, urban/rural for cereals, oil, wheat/rice |
| `Output_Weighted/Formatted/` | Excel workbooks with weighted disaggregated statistics |
| `Output_Unweighted/Formatted/` | Excel workbooks with unweighted disaggregated statistics |
| `Output_Weighted/raw_output/` | Raw CSV tables for each survey question block (q02_58–q07_08) |
| `Output_Unweighted/raw_output/` | Raw CSV tables (unweighted) |
| `Source/` | HTML export and `.py` conversion of the notebook |

## Setup

```bash
pip install pipenv
pipenv install
pipenv run jupyter notebook nhies_analysis_final.ipynb
```

### Dependencies

- Python 3.8
- numpy, pandas, matplotlib, seaborn, scipy

## Shared Utility

`aw_analytics.py` provides weighted statistical functions used throughout the notebook:
- `mean_wt` / `median_wt` — Weighted mean and median
- `output_mean_table` — Disaggregated weighted means by grouping variables
- `output_mean_tableau` — Same analysis reshaped to Tableau-ready long format

## License

MIT License — see `../Part_2/1-2_NHIES/LICENSE`
