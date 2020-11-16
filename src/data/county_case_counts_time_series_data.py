#!/usr/bin/env python
# coding: utf-8
import os
import time

from tqdm import tqdm
import pandas as pd

import c3aidatalake


RAW_DATA_DIR = "../raw_data_files"
OUTPUT_DATA_DIR = "../processed_data_files"


# Get the c3ai county ids
county_location_ids = pd.read_csv(os.path.join(RAW_DATA_DIR, "C3-ai-Location-IDs.csv"))
county_location_ids = county_location_ids[county_location_ids['County id'].str.contains('UnitedStates')]
county_location_ids = county_location_ids[county_location_ids['NYT: Case Counts'].notnull()][['County id', 'NYT: Case Counts']]
county_location_ids = list(county_location_ids['County id'])

# Get the case count data from the api
start = time.time()
county_case_counts = []

print("Fetching training data from api...")
for i in tqdm(range(0, len(county_location_ids), 10)):
    casecounts = c3aidatalake.evalmetrics(
        "outbreaklocation",
        {
            "spec" : {
                "ids" : county_location_ids[i:i+10],
                "expressions" : ["NYT_ConfirmedCases", "NYT_ConfirmedDeaths"],
                "start" : "2020-02-28",
                "end" : "2020-04-30",
                "interval" : "DAY",
            }
        }
    )
    county_case_counts.append(casecounts)
    
end = time.time()
print(f"Getting training data took {(end - start) / 60} minutes")

train_df = pd.concat(county_case_counts, axis=1)
train_df = train_df.loc[:,~train_df.columns.duplicated()]

start = time.time()
county_case_counts = []

print("Fetching testing data from api...")
for i in tqdm(range(0, len(county_location_ids), 10)):
    casecounts = c3aidatalake.evalmetrics(
        "outbreaklocation",
        {
            "spec" : {
                "ids" : county_location_ids[i:i+10],
                "expressions" : ["NYT_ConfirmedCases", "NYT_ConfirmedDeaths"],
                "start" : "2020-04-30",
                "end" : "2020-05-31",
                "interval" : "DAY",
            }
        }
    )
    county_case_counts.append(casecounts)
    
end = time.time()
print(f"Getting testing data took {(end - start) / 60} minutes")

test_df = pd.concat(county_case_counts, axis=1)
test_df = test_df.loc[:,~test_df.columns.duplicated()]

# Get the fips id for each county and save the c3ai county id -> fips id mappings in their own csv file
county_ids_to_fips = {}
start = time.time()

print("Fetching fips from the api...")

for cid in tqdm(county_location_ids):
    result = c3aidatalake.fetch(
        "outbreaklocation",
        {
            "spec" : {
                "filter" : f"id == '{cid}'",
                "include": "fips"
            }
        }
    )
    
    county_ids_to_fips[cid] = result['fips.id'][0] if 'fips.id' in result else None

end = time.time()
print(f"Getting fips ids took {(end - start) / 60} minutes")

no_fips_id_cids = []

for cid in county_ids_to_fips:
    if county_ids_to_fips[cid] is None:
        no_fips_id_cids.append(cid)
        
for cid in no_fips_id_cids:
    del county_ids_to_fips[cid]
        
cids = []
fips = []

for cid in county_ids_to_fips:
    cids.append(cid)
    fips.append(county_ids_to_fips[cid])

print(f"Saving the c3ai -> FIPS mappings to {os.path.join(OUTPUT_DATA_DIR, 'county_id_and_fips.csv')}...")

cids = pd.Series(cids, name='County id', dtype=str)
fips = pd.Series(fips, name='FIPS', dtype=str)
cid_fips = pd.concat([cids, fips], axis=1)
cid_fips.to_csv(os.path.join(OUTPUT_DATA_DIR, "c3ai_county_id_to_fips.csv"))

print("Saved!")

# Remove the counties for which c3ai does not have fips ids from our data
training = train_df
testing = test_df

good_columns = []

for c in training.columns:
    bad = False
    for n in no_fips_id_cids:
        if n in c:
            bad = True
            break
    if not bad:
        good_columns.append(c)
        
training = training[good_columns]
testing = testing[good_columns]

# Clean up the data into a more usable format
new_columns = ['Fips', 'Date', 'Confirmed_Cases', 'Confirmed_Cases_missing', 'Confirmed_Deaths', 'Confirmed_Deaths_missing']
county_ids = list(cid_fips['County id'])

# Training data
print(f"Formatting training data...")
dates = list(training['dates'])
fips = []
dates_series = []
case_count = []
case_missing = []
death_count = []
death_missing = []

for d in tqdm(dates):
    for c in county_ids:
        fips.append(cid_fips[cid_fips['County id'] == c]['FIPS'].values[0])
        data = training[training['dates'] == d]
        dates_series.append(d)
        case_count.append(data[c + '.NYT_ConfirmedCases.data'].values[0])
        case_missing.append(data[c + '.NYT_ConfirmedCases.missing'].values[0])
        death_count.append(data[c + '.NYT_ConfirmedDeaths.data'].values[0])
        death_missing.append(data[c + '.NYT_ConfirmedDeaths.missing'].values[0])
        
fips = pd.Series(fips, name='fips', dtype=str)
dates_series = pd.Series(dates_series, name='date', dtype=str)
case_count = pd.Series(case_count, name='case_count', dtype=float)
case_missing = pd.Series(case_missing, name='case_missing', dtype=float)
death_count = pd.Series(death_count, name='death_count', dtype=float)
death_missing = pd.Series(death_missing, name='death_missing', dtype=float)

new_training = pd.concat([fips, dates_series, case_count, case_missing, death_count, death_missing], axis=1)

# Testing data
print(f"Formatting testing data...")
dates = list(testing['dates'])
fips = []
dates_series = []
case_count = []
case_missing = []
death_count = []
death_missing = []

for d in tqdm(dates):
    for c in county_ids:
        fips.append(cid_fips[cid_fips['County id'] == c]['FIPS'].values[0])
        data = testing[testing['dates'] == d]
        dates_series.append(d)
        case_count.append(data[c + '.NYT_ConfirmedCases.data'].values[0])
        case_missing.append(data[c + '.NYT_ConfirmedCases.missing'].values[0])
        death_count.append(data[c + '.NYT_ConfirmedDeaths.data'].values[0])
        death_missing.append(data[c + '.NYT_ConfirmedDeaths.missing'].values[0])
        
fips = pd.Series(fips, name='fips', dtype=str)
dates_series = pd.Series(dates_series, name='date', dtype=str)
case_count = pd.Series(case_count, name='case_count', dtype=float)
case_missing = pd.Series(case_missing, name='case_missing', dtype=float)
death_count = pd.Series(death_count, name='death_count', dtype=float)
death_missing = pd.Series(death_missing, name='death_missing', dtype=float)

new_testing = pd.concat([fips, dates_series, case_count, case_missing, death_count, death_missing], axis=1)

# Get the rolling average case counts over a 7-day window in each county and add as a data column
print("Adding the rolling averages of case counts to the data...")

train_len = len(new_training)
test_len = len(new_testing)
combined = pd.concat([new_training, new_testing])
fips = combined['fips'].unique()
dfs = []
for f in fips:
    df = combined.loc[combined['fips'] == f]
    df = df.sort_values('date')
    df = pd.concat([df, df.rolling(7).mean()['case_count'].rename('case_count_rolling_average')], axis=1)
    dfs.append(df)
combined_w_rolling_mean = pd.concat(dfs).sort_values(['date', 'fips'])
combined_w_rolling_mean['case_count_rolling_average'] = combined_w_rolling_mean['case_count_rolling_average'].fillna(0)
training = combined_w_rolling_mean[0:train_len]
testing = combined_w_rolling_mean[train_len:train_len + test_len]

# Save the final data
print(f"Saving the data to {os.path.join(OUTPUT_DATA_DIR, 'county_case_counts_time_series_data_train.csv')} and {os.path.join(OUTPUT_DATA_DIR, 'county_case_counts_time_series_data_test.csv')}...")
training.to_csv(os.path.join(OUTPUT_DATA_DIR, "county_case_counts_time_series_data_train.csv"))
testing.to_csv(os.path.join(OUTPUT_DATA_DIR, "county_case_counts_time_series_data_test.csv"))
print("Saved!")

