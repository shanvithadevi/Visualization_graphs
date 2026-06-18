import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Advanced Dataset Analyzer & Visualizer")

uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.write(df.head())

    st.subheader("📈 Dataset Summary")
    st.write(df.describe(include="all"))

    # Sidebar options
    st.sidebar.header("Visualization Options")
    x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)
    chart_type = st.sidebar.selectbox(
        "Choose chart type",
        [
            "Scatter", "Line", "Bar", "Histogram", "Heatmap",
            "Boxplot", "Violin", "Pairplot", "Swarmplot", "Countplot",
            "KDE Plot", "Area Plot", "Pie Chart", "Stacked Bar", "Correlation Matrix"
        ]
    )

    st.subheader("📊 Visualization")

    if chart_type == "Scatter":
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line":
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Bar":
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        sns.histplot(df[x_axis], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Boxplot":
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Violin":
        fig, ax = plt.subplots()
        sns.violinplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Pairplot":
        st.pyplot(sns.pairplot(df).fig)

    elif chart_type == "Swarmplot":
        fig, ax = plt.subplots()
        sns.swarmplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot":
        fig, ax = plt.subplots()
        sns.countplot(data=df, x=x_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "KDE Plot":
        fig, ax = plt.subplots()
        sns.kdeplot(df[x_axis], fill=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Area Plot":
        fig, ax = plt.subplots()
        df.plot.area(ax=ax)
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        df[x_axis].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Stacked Bar":
        fig, ax = plt.subplots()
        pd.crosstab(df[x_axis], df[y_axis]).plot(kind="bar", stacked=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Correlation Matrix":
        st.write(df.corr())
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="viridis", ax=ax)
        st.pyplot(fig)

else:
    st.info("👆 Upload a dataset to get started.")
