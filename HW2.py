import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
df=sns.load_dataset("iris")
df2=sns.load_dataset("diamonds")

#plotly plots
data=[df["sepal_length"],df["sepal_width"],df["petal_length"],df["petal_width"]]
labels=['Sepal Length','Sepal Width','Petal Length','Petal Width']
fig1 = ff.create_distplot(data,labels,bin_size=[0.2,0.3,0.4,0.5])
fig2 = px.scatter_3d(df2,x="price",
                   y="carat",z="depth",
                   color='color')
fig3 = px.line_3d(df,x=df2["clarity"], y=df2["carat"],z=df2["color"],color=df2["cut"])
fig4 = px.violin(df, x="species", y="petal_width")

#Matplotlib plots
fig5, ax = plt.subplots()
ax.plot(df['species'], df['sepal_length'])
ax.plot(df['species'], df['sepal_width'])
ax.set_title('Sepal lengths and widths over species')
ax.set_xlabel('Species')
ax.set_ylabel('Sepal dimensions')
ax.set_ylim(bottom=0)
ax.legend()

st.write("""
 The Following are the some plots I have tried with plotly and Matplotlib:
 Distplot, 3D-Scatterplot, 3D-Lineplot,Violin plots,Line plots .
""")
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.pyplot(fig5)
