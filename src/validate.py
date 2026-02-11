def validate_data(df):
    invalid_conditions = (
        ((df["debit"] == 0) & (df["credit"] == 0)) |
        ((df["debit"] > 0) & (df["credit"] > 0)) |
        (df["balance"] < 0)
    )

    invalid_df = df[invalid_conditions]
    valid_df = df[~invalid_conditions]

    return valid_df, invalid_df