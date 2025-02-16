import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Drop columns with too many missing values
    columns_to_drop = [
        'Magnitude Error', 
        'Magnitude Seismic Stations', 
        'Horizontal Distance', 
        'Horizontal Error',
        'Depth Error',
        'Depth Seismic Stations',
        'Azimuthal Gap'
    ]
    df.drop(columns=columns_to_drop, inplace=True)

    # Drop rows with missing Magnitude Type
    df.dropna(subset=['Magnitude Type'], inplace=True)

    # Combine Date and Time into a single datetime column
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')

    # Drop rows with missing Datetime
    df.dropna(subset=['Datetime'], inplace=True)

    # Drop the original date and time columns
    df.drop(columns=['Date', 'Time'], inplace=True)

    # Save cleaned data to the data folder
    df.to_csv('data/cleaned_data.csv', index=False)
    print("Data cleaned and saved as 'data/cleaned_data.csv'")

    return df