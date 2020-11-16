#!/usr/bin/env python
# coding: utf-8
import os

import pandas as pd


RAW_DATA_DIR = "../raw_data_files"
OUTPUT_DATA_DIR = "../processed_data_files"


print(f"Saving the county FIPS ids with latitude and longitude to {os.path.join(OUTPUT_DATA_DIR, 'county_locations.csv')}")
cid_fips = pd.read_csv(os.path.join(OUTPUT_DATA_DIR, "c3ai_county_id_to_fips.csv"), dtype=object)
county_centers = pd.read_csv(os.path.join(RAW_DATA_DIR, "county_centers.csv"), dtype=object)
county_centers = county_centers.rename(columns={'fips': 'FIPS'})
locations = cid_fips.merge(county_centers, how='left', left_on='FIPS', right_on='FIPS')[['County id', 'FIPS', 'clon10', 'clat10']]
locations.loc[locations['County id'] == 'OglalaLakota_SouthDakota_UnitedStates', 'clon10'] = 43.3300
locations.loc[locations['County id'] == 'OglalaLakota_SouthDakota_UnitedStates', 'clat10'] = -102.5500
locations.loc[locations['County id'] == 'OglalaLakota_SouthDakota_UnitedStates']
locations.to_csv(os.path.join(OUTPUT_DATA_DIR, "county_locations.csv"))
print("Saved!")

