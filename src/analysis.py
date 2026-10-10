from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/scores.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

SAT_COLUMNS = [
    "Average Score (SAT Math)",
    "Average Score (SAT Reading)",
    "Average Score (SAT Writing)",
]

DEMOGRAPHIC_COLUMNS = [
    "Percent White",
    "Percent Black",
    "Percent Hispanic",
    "Percent Asian",
]


def minmax(series: pd.Series) -> pd.Series:
    """Scale a numeric pandas Series to the [0, 1] range."""
    return (series - series.min()) / (series.max() - series.min())


def prepare_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)

    # SAT-based analysis requires all three SAT components.
    schools = df.dropna(subset=SAT_COLUMNS).copy()
    schools["Total SAT Score"] = schools[SAT_COLUMNS].sum(axis=1)

    # Convert percentages stored as strings such as "91.0%" to numeric values.
    schools["Percent Tested Numeric"] = (
        schools["Percent Tested"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )
    schools = schools.dropna(subset=["Percent Tested Numeric"]).copy()

    for column in DEMOGRAPHIC_COLUMNS:
        schools[column] = (
            schools[column]
            .str.replace("%", "", regex=False)
            .astype(float)
        )

    # Feature scaling and composite score.
    schools["SAT Normalized"] = minmax(schools["Total SAT Score"])
    schools["Tested Normalized"] = minmax(schools["Percent Tested Numeric"])
    schools["Success Score"] = (
        0.70 * schools["SAT Normalized"]
        + 0.30 * schools["Tested Normalized"]
    )
    schools["Success Score 100"] = 100 * schools["Success Score"]

    return schools


def build_outputs(schools: pd.DataFrame) -> None:
    top10 = schools.sort_values("Success Score", ascending=False).head(10).copy()

    final = top10[[
        "School Name",
        "Borough",
        "Total SAT Score",
        "Percent Tested Numeric",
        "Success Score 100",
    ]].copy()
    final["Total SAT Score"] = final["Total SAT Score"].astype(int)
    final["Success Score 100"] = final["Success Score 100"].round(2)
    final.index = range(1, len(final) + 1)
    final.to_csv(OUTPUT_DIR / "top_10_nyc_schools.csv", index_label="Rank")

    borough_summary = schools.groupby("Borough").agg(
        School_Count=("School Name", "count"),
        Average_SAT=("Total SAT Score", "mean"),
        Median_SAT=("Total SAT Score", "median"),
        Average_Percent_Tested=("Percent Tested Numeric", "mean"),
    )
    borough_summary.to_csv(OUTPUT_DIR / "borough_summary.csv")

    print("Top 10 schools")
    print(final)


if __name__ == "__main__":
    schools = prepare_data()
    build_outputs(schools)
