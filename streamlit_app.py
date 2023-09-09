import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents new Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Healthy Menu Advice')

fruitchoosed = streamlit.text_input('What fruit would you like information about?','Kiwi')
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" + this_fruitchoosed)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
