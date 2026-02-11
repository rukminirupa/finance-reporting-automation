from src.extract import extract_transactions
from src.transform import transform_data
from src.validate import validate_data
from src.report import generate_reports

if __name__ == "__main__":
    print("Starting ETL...")
    df = extract_transactions()

    print("Transforming data...")
    df = transform_data(df)

    print("Validating data...")
    valid_df, invalid_df = validate_data(df)

    print("Generating reports...")
    generate_reports(valid_df, invalid_df)

    print("ETL pipeline completed.")