# Data Dictionary

| Column | Meaning | Type after cleaning |
|---|---|---|
| School ID | School identifier | string |
| School Name | School name | string |
| Borough | NYC borough | string |
| Student Enrollment | Student count | float |
| Percent White | Share of students recorded as White | float (%) |
| Percent Black | Share of students recorded as Black | float (%) |
| Percent Hispanic | Share of students recorded as Hispanic | float (%) |
| Percent Asian | Share of students recorded as Asian | float (%) |
| Average Score (SAT Math) | Average SAT Math score | float |
| Average Score (SAT Reading) | Average SAT Reading score | float |
| Average Score (SAT Writing) | Average SAT Writing score | float |
| Percent Tested | Share of students taking the SAT | string in raw data |
| Latitude / Longitude | Geographic coordinates | float |

## Engineered features

- **Total SAT Score** = Math + Reading + Writing
- **SAT Normalized** = min-max scaled Total SAT Score
- **Tested Normalized** = min-max scaled SAT participation
- **Success Score** = `0.70 × SAT Normalized + 0.30 × Tested Normalized`
- **Success Score 100** = Success Score × 100
