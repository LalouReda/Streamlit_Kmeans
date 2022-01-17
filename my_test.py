import streamlit as st
import pandas as pd
import numpy as np
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
iris = datasets.load_iris()

#Stocker les données en tant que DataFrame Pandas
x=pd.DataFrame(iris.data)

# définir les noms de colonnes
x.columns=['Sepal_Length','Sepal_width','Petal_Length','Petal_width']

y=pd.DataFrame(iris.target)
y.columns=["Targets"]

#Cluster K-means


#adapter le modèle de données
nb=st.slider("combien tu veux de cluster ?",min_value=2,max_value=x.shape[0],value=2)


st.dataframe(x.head(nb))
nbclust=st.slider("combien tu veux de cluster ?",min_value=2,max_value=4,value=2)
model=KMeans(n_clusters=nbclust)
model.fit(x)

fig, ax=plt.subplots()

colormap=np.array(['Red','green','blue',"black"])
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[y.Targets],s=40)
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[model.labels_],s=40)
st.pyplot(fig)
st.write('hello')
