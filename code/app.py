import streamlit as st
import joblib
import pickle
import pandas as pd

model = joblib.load(open('model.pkl','rb'))
books_data = joblib.load(open('final_ratings.pkl','rb'))
# # book_sparse = pickle.load(open('book_sparse.pkl','rb'))

books = pd.DataFrame(books_data)


st.title('Books Recommender System')

book_pivot = books.pivot_table(columns='user_id',index='title',values='book_rating')
book_pivot.fillna(0,inplace=True)

# st.write(book_pivot.shape)




selected_book_name = st.selectbox(
    'which book recommendations you want to check?',
    (book_pivot.index))

st.write(selected_book_name)

# Get the Selected movie index in books data
book_index=0
if selected_book_name in book_pivot.index:
    book_index = book_pivot.index.get_loc(selected_book_name)





# book_index = books[books['title'] == selected_book_name].index[0]

# st.write(book_index)
distances , suggestions = model.kneighbors(book_pivot.iloc[book_index,:].values.reshape(1,-1),n_neighbors=6)

if st.button('Recommend'):
    for i in suggestions[0][1:6]:
        st.write(book_pivot.index[i])



