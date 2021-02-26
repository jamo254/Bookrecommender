import numpy as np
import pandas  as pd
import streamlit as st
import matplotlib.pyplot as plt



#Sidebar

#Books in  our   library 
#Load the data
st.title('Books in our database')
book_data = ('goodreads.csv')
@st.cache
def load_data(nrows):
    data = pd.read_csv(book_data, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")



# if st.checkbox('Show titles'):
#     st.subheader('Book titles')
#     st.write(data['title'])

def selection(dataset_name):
 if dataset_name == 'Title':
    st.write(data['title'])
 elif  dataset_name == "Publisher":
    st.write(data['publisher'])
 elif dataset_name == 'Author' :
     st.write(data['author'])
 else:
     st.write(data)

dataset_name = selection(st.sidebar.selectbox("Select  data set", ("Title", "Publisher", "Author", "All")))

st.text_area("Input your data")




