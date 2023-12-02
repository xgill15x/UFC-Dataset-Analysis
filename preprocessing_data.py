import pandas as pd
import helper

def main():
    df = pd.read_csv('data.csv')

    numerical_columns = df.select_dtypes(include=['number'])
    for column in numerical_columns:
        helper.fill_na_with_median(df, column)

    # Write the DataFrame to a CSV file
    df.to_csv("preprocessed_data.csv", index=False)

if __name__=='__main__':
    main()
