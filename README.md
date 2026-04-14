# NHIES Fortification Analysis

![Results](NHIES_Parts_1-2.jpg)

Analysis of the Namibia Household Income and Expenditure Survey (NHIES) 2015-16 and related data sources to inform Namibia's mandatory food fortification policy under the Food and Nutrition Security Policy and Implementation Action Plan (2019-2024).

## Structure

### [Part 1](Part_1/) — Food Consumption and Production Analysis

Core analysis of NHIES household microdata: food consumption patterns, crop production, and source diversity disaggregated by region, income, language, and urban/rural residence. Produces weighted and unweighted statistical tables and 30 SVG visualizations.

### [Part 2](Part_2/) — Extended Fortification Analyses

Eight follow-on tasks building on Part 1:

| Task | Directory | Description |
|---|---|---|
| 1-2 | `1-2_NHIES/` | Additional crop production and grain consumption analysis with time-series patterns |
| 3 | `3_g-c-d_calc/` | Grams/capita/day estimates for candidate fortification vehicles (wheat, maize, salt, oil, sugar, milk) |
| 4 | `4_ADePT/` | Micronutrient dataset preparation — harmonizes 4 Food Composition Tables for FAO ADePT |
| 5 | `5_A2Z/` | A2Z fortification formulation tools and reference materials |
| 6 | `6_DHS_salt/` | Salt iodization trends from DHS 2000, 2006, 2013 |
| 7-8 | `7-8_Salt/` | Per capita salt, bread, and milk consumption from the NHIES 7-day diary |

## Tools

- Python 3.8, Jupyter Notebook
- numpy, pandas, matplotlib, seaborn

## License

MIT License
