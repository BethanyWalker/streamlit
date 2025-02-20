import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

dataframes = ['ol_faithful', 'planets', 'fmri' ]

ol_faithful = sns.load_dataset("geyser")
planets = sns.load_dataset("planets")
fmri = sns.load_dataset("fmri")

st.title(f"Data manipulation and graphs. \n Some information to help you")

choice = st.selectbox("Please choose a dataset: ",
             options = dataframes,
             index= None
             )

if choice == 'ol_faithful':
    st.write("you have chosen: ", choice)
    st.dataframe(ol_faithful)
    df = ol_faithful
elif choice == 'planets':
    st.write("you have chosen: ", choice)
    st.dataframe(planets)
    df = planets
else :
    st.write("you have chosen: ", choice)
    st.dataframe(fmri)
    df = fmri

column_X = st.selectbox("Choose your column X: ",
                 options = df.columns)

column_Y = st.selectbox("Choose your column Y: ",
                 options = df.columns)

selection = st.radio("Choose your graph: ",
         options = ['scatter_chart', 'bar_chart', 'line_chart'])

if selection == 'scatter_chart':
    st.scatter_chart(
        df,
        x=column_X,
        y=column_Y)
elif selection == 'bar_chart':
    st.bar_chart(df,
                 x= column_X,
                 y= column_Y)
else:
    st.line_chart(
        df,
        x= column_X,
        y= column_Y
    )

df_column_X = df[column_X]
df_column_Y = df[column_Y]


checkbox = st.checkbox("heatmap anyone?")
if checkbox:

    if df_column_X.dtype =='object' or df_column_Y.dtype == 'object':
        st.write("please choose a different column \n so as to have numerical values for the heatmap")
    else:    
        st.write("Here is a heatmap")
        selected_columns = [column_X, column_Y]
        df_columns = df[selected_columns]
        print(df_columns)
        plt.figure(figsize=(10, 6))
        sns.heatmap(df_columns.corr(), annot=True, cmap='coolwarm')
        st.pyplot(plt)