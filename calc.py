import pandas as pd

# Load the xlsx file
df = pd.read_excel('transactions.xlsx')

# Initialize the total BNB spent in EUR
total_bnb_spent_eur = 0

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    # Check if the transaction used BNB
    if 'BNB' in row['Assets Used']:
        # Split the assets used string into a list of assets and amounts
        assets_used = row['Assets Used'].split('; ')
        # Find the BNB asset and extract the amount
        bnb_amount = 0
        for asset in assets_used:
            if 'BNB' in asset:
                bnb_amount = float(asset.split(' ')[1])
                break
        # Split the exchange rates string into a list of rates
        exchange_rates = row['Exchange Rates'].split('; ')
        # Find the BNB exchange rate and extract the rate
        bnb_rate = 0
        for rate in exchange_rates:
            if 'BNB' in rate:
                bnb_rate = float(rate.split(' ')[-2])
                break
        # Calculate the EUR value of the BNB spent and add it to the total
        bnb_spent_eur = bnb_amount / bnb_rate
        total_bnb_spent_eur += bnb_spent_eur

# Print the total BNB spent in EUR
print(f'Total BNB spent in EUR: {total_bnb_spent_eur:.2f}')