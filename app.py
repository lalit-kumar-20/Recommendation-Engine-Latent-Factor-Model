from copyreg import pickle
import streamlit as st
import pickle 
import pandas as pd
import numpy as np
st.title('Ratings Predictor For a User')
artist_list=pickle.load(open('C:/Users/me/Desktop/python_project/app.py/artists.pkl','rb'))
artist_listt=artist_list.columns
def recommend(user_id):
      top_df= artist_list[user_id].sort_values(ascending=False)
      return top_df
    
def disimilarly_recommended(user_id): 
     bottom_df= artist_list[user_id].sort_values(ascending=True)
     return bottom_df
    
selected_user_id = st.selectbox(
     'Enter The UserID For Getting Top Recommended Movies',
   artist_listt  )

if st.button('Recommend'):
      result1=recommend(selected_user_id)
      result2=disimilarly_recommended(selected_user_id)
      st.title('Top Predicted Ratings for Corresponding Movies')
      st.write('Movies_ID | Top Ratings',result1.head(10))
      st.title('Lowest Predicted Ratings for Corresponding Movies')
      st.write('Movies_ID | Lowest Ratings',result2.head(10))
