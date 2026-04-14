# Part 2: Extended NHIES Fortification Analyses

A suite of analyses expanding on Part 1, organized as discrete tasks to support the design and implementation of Namibia's mandatory food fortification program. Work was performed under contract with the Iodine Global Network (IGN).

## Background

With household food consumption and production patterns established in Part 1, Part 2 addresses the follow-on questions needed for fortification policy: Which foods are the best fortification vehicles? How much of each vehicle is consumed per capita? What are the regional micronutrient gaps? What is the current state of salt iodization?

## Tasks

### Tasks 1-2: NHIES Crop Production and Grain Consumption (`1-2_NHIES/`)

Extended analysis of NHIES household-level data with additional demographic breakdowns and time-series consumption patterns.

- `01_crop_production_additional_analysis.ipynb` — Regional crop production by demographics (urban/rural, sex, age, education, income, language)
- `02_grain_consumption_HH_analysis.ipynb` — Monthly grain consumption source patterns (own production vs. purchased) by region, using the 7-day food diary
- `image_editing_process.ipynb` — Generates composite chart overlays for presentation

**Outputs:** `output/01_comparison/` (spreadsheets), `output/02_region/charts/` (SVG regional charts)

### Task 3: Fortification Vehicle Calculations (`3_g-c-d_calc/`)

Calculates grams/capita/day (g/c/d) consumption estimates for candidate fortification vehicles at national and regional levels.

- `03_g-c-d_analysis.ipynb` — Classifies ADePT food items into fortification vehicle categories (wheat, maize, mahangu, salt, milk, oil, sugar), applies nutrient content mappings, and calculates regional daily intake sums
- `03_HH_Consumption_analysis.ipynb` — Household-level prevalence of consuming each fortification vehicle
- `food_item_comparison.ipynb` — Compares food item classifications across sources

**Inputs:** ADePT macro results (Table 3.1 national, Table 3.5 regional)
**Outputs:** `output/output.csv` (regional g/c/d estimates), `output/item_mean.csv` (household consumption prevalence)

### Task 4: ADePT Micronutrient Data Preparation (`4_ADePT/`)

Harmonizes multiple Food Composition Tables (FCTs) into a single standardized dataset for use with the FAO/World Bank ADePT-Food Security Module.

- `04_adept_micronut_cleaning.ipynb` — Reads, cleans, and merges FCTs from West Africa, Kenya, USDA SR24, and South Africa; standardizes micronutrient columns (calcium, iron, zinc, folate, vitamins A/B/C/D/E, etc.); matches to NHIES food items
- `04_FCT2017SA_camelot.ipynb` — Extracts South African FCT data from PDF using Camelot
- `fao_micro_comp.ipynb` — Compares FAO ADePT results across FCT sources

**Outputs:** `output/Namibia_MN_fct_dataset_2020-10-31.csv` (199 harmonized food items with micronutrient values)

### Task 5: A2Z Fortification Formulation (`5_A2Z/`)

Reference materials and Excel-based tools for fortification formulation — no computational notebooks. Contains the A2Z Food Fortification Formulator templates (wheat flour, maize flour, oil, salt, sugar), cost comparisons, and minimum standards documentation.

### Task 6: DHS Salt Iodization Analysis (`6_DHS_salt/`)

Analyzes household salt iodization status across three Namibia Demographic and Health Surveys.

- `2000_nam_dhs_salt_analysis.ipynb` — DHS 2000 salt type, source, and iodine status
- `2006_nam_dhs_salt_analysis.ipynb` — DHS 2006 analysis
- `2013_nam_dhs_salt_analysis.ipynb` — DHS 2013 analysis

Each notebook disaggregates by region, urban/rural, and education level using survey weights.

**Outputs:** `output/DHS_Namibia_salt_analyses.xlsx` (consolidated), plus per-year CSVs

### Tasks 7-8: Salt and Bread/Milk Consumption (`7-8_Salt/`)

Estimates per capita daily consumption of salt, bread, and milk from the NHIES 7-day diary, with unit conversions and outlier removal.

- `drb_salt_analysis.ipynb` — Salt consumption distribution by region (converts teaspoons/tablespoons/cups to grams, calculates g/capita/day, generates KDE density plots)
- `drb_milk_analysis.ipynb` — Milk consumption sources by region

**Outputs:** `output/regional_salt_est.csv`, `output/bread_milk/regional_bread_est.csv`, SVG distribution charts

## Non-Analysis Directories

| Directory | Contents |
|---|---|
| `Communications/` | FCT comparison images, rendered notebook HTML |
| `Contract/` | IGN contract documents, amendments, Terms of Reference |
| `Summary/` | PowerPoint summary presentations for Parts 1-2 and Parts 3-8 (multiple revision rounds) |

## Data Sources

- **NHIES 2015-16** — `Diary_hhV12.dta` (household), `Diary_coicopV12.dta` (7-day food diary)
- **ADePT outputs** — National (Table 3.1) and regional (Table 3.5) food consumption estimates
- **Food Composition Tables** — West African 2012, Kenya, USDA SR24, South African 2017
- **DHS Namibia** — Household recode files for 2000, 2006, 2013 surveys

## Environment

- Python 3.8
- Core: numpy, pandas, matplotlib, seaborn
- Task 4 additionally requires: camelot-py (PDF table extraction)

## License

MIT License — see `1-2_NHIES/LICENSE`
