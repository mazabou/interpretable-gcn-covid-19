import os

import pandas as pd


RAW_DATA_DIR = '../raw_data_files'
OUTPUT_DATA_DIR = '../processed_data_files'


# Total population
pop_df = pd.read_csv(os.path.join(RAW_DATA_DIR, 'PopulationEstimates.csv'), dtype=object)
fips_df = pd.read_csv(os.path.join(OUTPUT_DATA_DIR, 'c3ai_county_id_to_fips.csv'), dtype=object)

pop_col = None

for col in pop_df.columns:
    done = False
    for datum in pop_df[col]:
        if 'POP_ESTIMATE_2019' in str(datum):
            pop_col = col
            done = True
            break
    if done:
        break

pop_df = pop_df[[pop_df.columns[0], pop_col]]
result = fips_df.merge(pop_df, 'left', left_on='FIPS', right_on=pop_df.columns[0])
result = result.rename(columns={'Unnamed: 19': 'us_census_population_2019'})
result['us_census_population_2019'] = result['us_census_population_2019'].apply(lambda x : x.replace(',', ''))
result['us_census_population_2019'] = result['us_census_population_2019'].astype(int)
result = result[['FIPS', 'us_census_population_2019']]
result.to_csv(os.path.join(OUTPUT_DATA_DIR, 'county_level_total_population_2019.csv'))


# Population greater than age 65
census_df = pd.read_csv(os.path.join(RAW_DATA_DIR, 'cc-est2019-alldata.csv'), encoding="ISO-8859-1", dtype=object)
census_df['FIPS'] = census_df['STATE'] + census_df['COUNTY']
census_df = census_df[['FIPS', 'AGEGRP', 'TOT_POP']]
census_df['FIPS'] = census_df['FIPS'].astype(str)
census_df['AGEGRP'] = census_df['AGEGRP'].astype(int)
census_df['TOT_POP'] = census_df['TOT_POP'].astype(int)
census_df = census_df.loc[census_df['AGEGRP'] >= 14]
census_df = census_df[['FIPS', 'TOT_POP']]
pop_by_age = census_df.groupby(['FIPS']).sum().reset_index()
pop_by_age = pop_by_age.rename(columns={'TOT_POP': 'pop_age_gte_65'})
pop_by_age.to_csv(os.path.join(OUTPUT_DATA_DIR, 'county_level_population_with_age_gte_65_2019.csv'), encoding='utf-8')

