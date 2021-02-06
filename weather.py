import pandas as pd 
import streamlit as st 
import datetime
import plotly.express as px


@st.cache
def data_formatting():
    weather_df = pd.read_csv("weatherHistory.csv")
    df = weather_df[["Formatted Date" , "Apparent Temperature (C)" ,"Humidity"]].copy()
    df["Formatted Date"] = pd.to_datetime(df["Formatted Date"] , utc = True)
    df["Year"] = df["Formatted Date"].dt.year
    df["Month"] = df["Formatted Date"].dt.month
    return df

@st.cache
def grouping_data(df):
    df_groups = df.groupby(["Year" , "Month"]).mean()
    return df_groups
    print("in group data")


def temp_graph(df_groups):
    st.subheader("Average Apparent Temperature")
    temp_slider = st.slider("Select Month" ,1,12)
    temp_df = df_groups.query('Month == @temp_slider ')
    temp_df.reset_index(inplace = True)
    st.write(px.bar(temp_df , x = "Year" , y = "Apparent Temperature (C)"))
    if st.checkbox("Show Average Apparent Temperature Data"):
        st.write(temp_df[["Year" , "Apparent Temperature (C)"]])
def humidity_graph(df_groups):
    st.subheader("Average Humidity")
    humidity_slider = st.slider("Select month" ,1,12)
    humidity_df = df_groups.query('Month == @humidity_slider ')
    humidity_df.reset_index(inplace = True)
    st.write(px.bar(humidity_df , x = "Year" , y = "Humidity"))
    if st.checkbox("Show Average Humidity Data"):
        st.write(humidity_df[["Year" , "Humidity"]])

st.title("Weather Data Analysis")
st.subheader("In this notebook we study the rise/fall in average apparent temperature and humidity of a month across a decade .")

df = data_formatting()
df_groups = grouping_data(df)
temp_graph(df_groups)
humidity_graph(df_groups)

