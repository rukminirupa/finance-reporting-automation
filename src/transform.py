def transform_data(df):
    # Ensure debit and credit are numeric
    df["debit"] = df["debit"].astype(float)
    df["credit"] = df["credit"].astype(float)

    # Create a net_amount column
    df["net_amount"] = df["credit"] - df["debit"]

    return df