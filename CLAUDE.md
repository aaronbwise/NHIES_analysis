# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Analysis of the Namibia Household Income and Expenditure Survey (NHIES) 2015-16 to inform food fortification policy. The project examines household food production and consumption patterns using survey data, supporting the Namibia Food and Nutrition Security Policy (2019-2024).

## Repository Structure

- **Part_1/**: Original NHIES analysis — crop production, grain consumption, regional mapping. Contains the primary analysis notebook (`nhies_analysis_final.ipynb`) and final output charts/tables in `OUTPUT_FINAL/`.
- **Part_2/**: Extended analyses organized by task:
  - `1-2_NHIES/` — Crop production and grain consumption (public-facing notebooks with README)
  - `3_g-c-d_calc/` — Grain consumption-distribution calculations and food item comparisons
  - `4_ADePT/` — FAO ADePT micronutrient analysis; includes food composition table (FCT) extraction via Camelot
  - `5_A2Z/` — A2Z fortification formulation tool inputs
  - `6_DHS_salt/` — DHS salt iodization analysis across 2000, 2006, 2013 surveys
  - `7-8_Salt/` — DRB (Diary Record Book) salt and bread/milk analysis
  - `Communications/`, `Contract/`, `Summary/` — Project deliverables and documentation

## Environment

- Python 3.8 with pipenv (`Part_1/Pipfile`)
- Core dependencies: numpy, pandas, matplotlib, seaborn
- Some notebooks use additional libraries (e.g., camelot for PDF table extraction in `Part_2/4_ADePT/`)

## Shared Utility: `aw_analytics.py`

There are three copies of this module (`Part_1/`, `Part_2/1-2_NHIES/`, `Part_2/6_DHS_salt/`). They are **not identical** — Part_1 and Part_2/6_DHS_salt have the full version with `output_mean_tableau()`, while Part_2/1-2_NHIES has a smaller subset. Key functions:

- `mean_wt(df, var, wt)` — Weighted mean, drops NaN values
- `median_wt(df, var, wt)` — Weighted median via cumulative sum approach
- `output_mean_table(df, var, ind_vars, wt)` — Disaggregated weighted means by grouping variables
- `output_mean_tableau(df, var, ind_vars, wt)` — Same analysis reshaped into Tableau-ready long format

These functions are imported locally by notebooks in their respective directories.

## Data Sources

- NHIES 2015-16 survey microdata (Stata `.dta` files in `Part_1/nhies_files/`)
- Namibia administrative boundary shapefiles (`Part_1/data_all/shapefiles/`)
- DHS survey data for salt/iodine analysis (`Part_2/6_DHS_salt/data/`)
- FAO food composition tables and ADePT outputs (`Part_2/4_ADePT/`)

## Running Notebooks

```bash
cd Part_1
pipenv install
pipenv run jupyter notebook
```

Each Part_2 subdirectory's notebooks expect to be run from within that subdirectory (relative data paths).
