import streamlit as st
import pandas as pd
import seaborn as sns

nyc = sns.load_dataset("taxis")
nyc_borough = nyc['pickup_borough'].unique()
#nyc_borough
st.title(f"Welcome to the webpage of the awesome :rainbow[Beth]")
options = st.selectbox("Please indicate the borough you wanna visit",
             options = nyc_borough,
             index= None
             )

if options == "Manhattan":
    st.write("you have chosen: ", options)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Above_Gotham.jpg/1920px-Above_Gotham.jpg")
elif options == "Queens":
    st.write("you have chosen: ", options)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Long_Island_City_New_York_May_2015_panorama_3.jpg/1920px-Long_Island_City_New_York_May_2015_panorama_3.jpg")
elif options == "Bronx":
    st.write("you have chosen: ", options)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Yankee_Stadium_overhead_2010.jpg/1920px-Yankee_Stadium_overhead_2010.jpg")
elif options == "Brooklyn":
    st.write("you have chosen: ", options)
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/00/Brooklyn_Bridge_Manhattan.jpg")
else:
    st.write("you have chosen: ", options)
    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemRrbmUxOW04cGVvbnI0bTc1ZzIyOGJrcGNrZDA4eW11emluNGgyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XWXnf6hRiKBJS/giphy.gif")
