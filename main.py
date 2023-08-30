import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()

with header:
	st.title('Welcome to my awesome data science project - The Menu')
	st.text("A small web app to help you make deciison on what you can cook based on your feeling and what's available in your pantry")

with dataset:
	st.header("The Menu datset")
	st.text("It's a simplpe dataset I created with all the vegan dish I cooked over the years")
	st.text("It has 3 columns, which inlcude 'Theme', 'Dish', 'Ingredient'")
	
	# Showing the dataset
	df = pd.read_csv('Menu.csv')
	st.write(df.head(1))



with features:
	st.header("What you can do?")


	# # Create a Streamlit app
	# st.title("Dish Finder")

	# Ask the user for input
	theme = st.text_input("Enter a theme:")
	ingredient = st.text_input("Enter an ingredient:")

	# Filter the DataFrame based on the user input
	filtered_df = df[(df['Theme'] == theme) & (df['Ingredients'] == ingredient)]

	# Display the matching dishes
	if st.button("Find Dishes"):
	    if len(filtered_df) == 0:
	        st.warning(f"No dishes found for Theme: '{theme}' and Ingredient: '{ingredient}'")
	    else:
	        st.success("Matching Dishes:")
	        for dish in filtered_df['Dish']:
	            st.write(dish)