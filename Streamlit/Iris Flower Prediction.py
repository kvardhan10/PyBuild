import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets, neighbors

st.set_page_config(layout='wide')

st.header('IRIS FLOWER PREDICTION')

about = st.expander('About')
about.markdown("""
**This app predicts the Iris flower based on the settings adjusted by the user using the [KNN Classifier](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm. The settings are adjusted based on tweaking the sepal length, sepal width,  petal length and petal width. The target flowers may be *Iris Setosa, Iris Versicolor or Iris Virginica.* The prediction is made using the [Iris Dataset in sklearn library](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)**
""")

iris = datasets.load_iris()
X = iris.data
Y  =iris.target
st.write('Target Guide')
st.write(iris.target_names)
st.markdown('---')
knn = neighbors.KNeighborsClassifier(11, weights='uniform')
knn.fit(X, Y)
predictions = {0: 'Iris Setosa',
                1: 'Iris Versicolor',
                2: 'Iris Virginica'
                }
st.sidebar.header('Adjust your flower settings')
s_len = st.sidebar.slider('SEPAL LENGTH', 4.0, 8.0, 4.7)
s_wid = st.sidebar.slider('SEPAL WIDTH', 2.5, 4.0, 3.0)
p_len = st.sidebar.slider('PETAL LENGTH', 1.0, 6.0, 3.0)
p_wid = st.sidebar.slider('PETAL WIDTH', 0.1, 3.0, 1.7)
data = {'sepal_length': s_len,
        'sepal_width': s_wid,
        'petal_length': p_len,
        'petal_width': p_wid
        }
input = pd.DataFrame(data, index=[0])

# if st.sidebar.button('PREDICT MY FLOWER'):
st.write('PREDICTED: ' + predictions[knn.predict(input)[0]])
st.write('PREDICTION SET FOR EACH TYPE: ')
st.write(knn.predict_proba(input))
