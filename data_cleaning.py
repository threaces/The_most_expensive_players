import pandas as pd

# reading a data from csv file

file_path = "players.csv"

def reading_csv_file(csv_file_path):

    df = pd.read_csv(csv_file_path)
    return df

# drop na values from data frame

def clean_df(df):

    df = df.dropna()
    df = df.iloc[ : ,0:11]
    df = df.rename(columns={'Markey Value In Millions(£)': 'Market Value In Millions(£)', "Unnamed: 0": "Index"})

    return df

# creating a dataframe for visualization for top10 most expensive players

def top10_most_expensive(df):
    df = df.iloc[0: 10, [1, 4]]
    df = df.sort_values('Market Value In Millions(£)', ascending=True)

    return df

# creating a dataframe for chart with information about top10 in each position

def get_list_of_positions(df):

    list_of_positions = []

    for row, value in df.iterrows():
        if value[2] not in list_of_positions:
            list_of_positions.append(value[2])

    return list_of_positions

def top10_position(df, position):

    df = df[df['Position'] == position]
    df = df.iloc[0:10, :]
    df = df.sort_values('Market Value In Millions(£)', ascending=True)

    return df

list_pos = get_list_of_positions(clean_df(reading_csv_file(file_path)))

# creating a dataframe for chart with information about top10 in each club (included in raw data file)

def get_list_club(df):
    
    list_of_clubs = []

    for row, value in df.iterrows():
        if value[6] not in list_of_clubs:
            list_of_clubs.append(value[6])

    return list_of_clubs

list_of_clubs = get_list_club(clean_df(reading_csv_file(file_path)))

def top10_club(df, club):

    df = df[df['Club'] == club]
    df = df.iloc[0:10, :]
    df = df.sort_values('Market Value In Millions(£)', ascending=True)

    return df

# creating a dataframe with the most expensive young players

def young_players_df(df):

    df = df[df['Age'] <= 21]
    df = df.iloc[0: 10, :]
    df = df.sort_values('Market Value In Millions(£)', ascending=True)

    return df

# creating a dataframe with the most expensive senior players 30+

def senior_players_df(df):

    df = df[df['Age'] >= 30]
    df = df.iloc[0: 10, :]
    df = df.sort_values('Market Value In Millions(£)', ascending=True)

    return df

# creating a dataframe for age distribution

def age_distribution_df(df):

    dict_of_ages = {}

    for row, values in df.iterrows():
        if values[3] not in dict_of_ages:
            dict_of_ages[values[3]] = 1
        else:
            dict_of_ages[values[3]] += 1

    dict_of_ages = dict(sorted(dict_of_ages.items(), key=lambda item: item[0]))
    age_df = pd.DataFrame.from_dict(dict_of_ages, orient='index')
    age_df = age_df.rename(columns={0 : 'Amount of players'})
    return age_df

# dataframe - which country has the biggest amount of players in ranking

def amount_of_players(df):
    dict_of_country = {}

    for row, values in df.iterrows():
        if values[5] not in dict_of_country:
            dict_of_country[values[5]] = 1
        elif values[5] in dict_of_country:
            dict_of_country[values[5]] += 1

    dict_of_country = dict(sorted(dict_of_country.items(), key=lambda item: item[1], reverse=True))

    sum_of_other_nations = 0

    for keys, values in dict_of_country.items():
        if values < 10:
            sum_of_other_nations += values

    final_dict_of_country = {'England': 67, 
    'France': 58, 
    'Spain': 52, 
    'Brazil': 41, 
    'Germany': 29, 
    'Portugal': 26, 
    'Italy': 26, 
    'Argentina': 22, 
    'Netherlands': 17, 
    'Belgium': 14, 
    'Uruguay': 11,
    "Other Countries" : sum_of_other_nations}

    country_df = pd.DataFrame(final_dict_of_country.values(), index=final_dict_of_country.keys(), columns=["Quantity of Players"])
    
    def new_column(row):
        percent = round((row["Quantity of Players"] / 500) * 100, 2)

        return percent

    country_df["% of players in ranking"] = country_df.apply(lambda row: new_column(row), axis=1)

    return country_df




