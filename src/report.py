import os

def generate_reports(valid_df, invalid_df):
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Summary calculations
    summary = {
        "total_transactions": len(valid_df) + len(invalid_df),
        "valid_transactions": len(valid_df),
        "invalid_transactions": len(invalid_df),
        "total_debit": valid_df["debit"].sum(),
        "total_credit": valid_df["credit"].sum()
    }

    # Convert summary to DataFrame
    import pandas as pd
    summary_df = pd.DataFrame([summary])

    # Save files
    summary_df.to_csv("output/finance_summary.csv", index=False)
    invalid_df.to_csv("output/exception_report.csv", index=False)

    print("\nReports generated successfully.")