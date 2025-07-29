from src.cleaning import load_and_clean_data
from src.eda_univariate import run_univariate_analysis
from src.eda_bivariate import run_bivariate_analysis

if __name__ == "__main__":
    print("🚀 Starting NYC Airbnb EDA...")

    df = load_and_clean_data("../data/AB_NYC_2019.csv")

    run_univariate_analysis(df)
    run_bivariate_analysis(df)

    print("✅ EDA complete. Charts saved to /output/charts/")