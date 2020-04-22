import pandas as pd
import streamlit as st


def drop_na_vals(df, col):
    df = df.dropna(subset=[col])
    return df

def view_cols(df):
    for col in df.columns:
        x = df[col].isna().sum()
        y = df[col].count()
        print(f'Column: {col} || Total NA Values: {x}; Total Col Values: {y};  Percent of NA Values: {x/y}')
    return None

def calculate_average(df, col):
    col_sum = df[col].sum()
    total_col_count = df[col].count()
    average = col_sum / total_col_count
    return average 


def replace_nulls(df, col):
    average = calculate_average(df, col)    
    df[col] = df[col].apply(lambda x: average if x != x else x)
    return df

@st.cache
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    df = replace_nulls(df, 'salary')
    return df

st.title('College Campus Class Statistics')

data_load_state = st.text('Loading data...')
df = load_data('data/Placement_Data_Full_Class.csv')
data_load_state.text('Loading data... Done!')

st.subheader('Raw Data')
st.write(df)

st.bar_chart(df['degree_t'])
print(df.columns)

