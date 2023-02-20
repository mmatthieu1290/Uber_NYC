import streamlit as st
from PIL import Image
#import SessionState

     

### Config
st.set_page_config(
    page_title="Hot spot Uber NYC",
    layout="wide"
)

### HEADER
st.title('Hot spots for Uber in NYC')

days_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

hours_list = ['0-3','3-6','6-9','9-12','12-15','15-18','18-21','21-24']

day_choice = st.sidebar.selectbox("Choose the day in week",days_list)
hour_choice = st.sidebar.selectbox("Choose the hours in the day",hours_list)

st.write('Greater value of "Hot spot" means greater demand.')

im = Image.open(f"images_kmeans/{day_choice}_{hour_choice}.png")

st.image(im)






