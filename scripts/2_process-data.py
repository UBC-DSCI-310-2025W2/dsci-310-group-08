# imports
import pandas as pd

data_raw = pd.read_csv("../data/raw/parks_raw.csv")

data_processed = data_raw.sort_values(["city", "year"])
data_processed["rank_last_time"] = data_processed.groupby("city")["rank"].shift(1)
data_processed['rank_last_time'] = data_processed['rank_last_time'].fillna(data_processed['rank'])
data_processed = data_processed[~data_processed["year"].isin([2012,2013,2014])]
data_processed = data_processed.drop(columns=['restroom_data','restroom_points','splashground_data',
                                              'splashground_points','total_points','total_pct',
                                              'city_dup','park_benches'])

city_to_state = {
    'Albuquerque': 'NM', 'Anaheim': 'CA', 'Anchorage': 'AK', 
    'Arlington, Texas': 'TX', 'Arlington, Virginia': 'VA', 'Atlanta': 'GA', 
    'Aurora': 'CO', 'Austin': 'TX', 'Bakersfield': 'CA', 'Baltimore': 'MD', 
    'Baton Rouge': 'LA', 'Boise': 'ID', 'Boston': 'MA', 'Buffalo': 'NY', 
    'Chandler': 'AZ', 'Charlotte': 'NC', 'Charlotte/Mecklenburg County': 'NC',
    'Chesapeake': 'VA', 'Chicago': 'IL', 'Chula Vista': 'CA', 'Cincinnati': 'OH', 
    'Cleveland': 'OH', 'Colorado Springs': 'CO', 'Columbus': 'OH', 
    'Corpus Christi': 'TX', 'Dallas': 'TX', 'Denver': 'CO', 'Des Moines': 'IA', 
    'Detroit': 'MI', 'Durham': 'NC', 'El Paso': 'TX', 'Fort Wayne': 'IN', 
    'Fort Worth': 'TX', 'Fremont': 'CA', 'Fresno': 'CA', 'Garland': 'TX', 
    'Glendale': 'AZ', 'Greensboro': 'NC', 'Henderson': 'NV', 'Hialeah': 'FL', 
    'Honolulu': 'HI', 'Houston': 'TX', 'Indianapolis': 'IN', 'Irvine': 'CA', 
    'Irving': 'TX', 'Jacksonville': 'FL', 'Jersey City': 'NJ', 'Kansas City': 'MO', 
    'Laredo': 'TX', 'Las Vegas': 'NV', 'Lexington': 'KY', 'Lincoln': 'NE', 
    'Long Beach': 'CA', 'Los Angeles': 'CA', 'Louisville': 'KY', 'Lubbock': 'TX', 
    'Madison': 'WI', 'Memphis': 'TN', 'Mesa': 'AZ', 'Miami': 'FL', 
    'Milwaukee': 'WI', 'Minneapolis': 'MN', 'Nashville': 'TN', 'New Orleans': 'LA', 
    'New York': 'NY', 'Newark': 'NJ', 'Norfolk': 'VA', 'North Las Vegas': 'NV', 
    'Oakland': 'CA', 'Oklahoma City': 'OK', 'Omaha': 'NE', 'Orlando': 'FL', 
    'Philadelphia': 'PA', 'Phoenix': 'AZ', 'Pittsburgh': 'PA', 'Plano': 'TX', 
    'Portland': 'OR', 'Raleigh': 'NC', 'Reno': 'NV', 'Richmond': 'VA', 
    'Riverside': 'CA', 'Sacramento': 'CA', 'San Antonio': 'TX', 'San Diego': 'CA', 
    'San Francisco': 'CA', 'San Jose': 'CA', 'Santa Ana': 'CA', 'Scottsdale': 'AZ', 
    'Seattle': 'WA', 'St. Louis': 'MO', 'St. Paul': 'MN', 'St. Petersburg': 'FL', 
    'Stockton': 'CA', 'Tampa': 'FL', 'Toledo': 'OH', 'Tucson': 'AZ', 'Tulsa': 'OK', 
    'Virginia Beach': 'VA', 'Washington, D.C.': 'DC', 'Wichita': 'KS', 
    'Winston-Salem': 'NC'
}
data_processed['state'] = data_processed['city'].map(city_to_state)

data_processed['year'] = data_processed['year'].astype('category')
data_processed['city'] = data_processed['city'].astype('category')
data_processed['state'] = data_processed['state'].astype('category')
data_processed['rank'] = data_processed['rank'].astype('int')
data_processed['rank_last_time'] = data_processed['rank_last_time'].astype('int')
data_processed = data_processed.drop(columns=data_processed.filter(regex='data$').columns)

# export processed data to csv in the processed folder
data_processed.to_csv("../data/processed/parks_processed.csv", index=False)

# verify the script works
print(data_processed.head(10)) 