import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import plotly.express as px

# Function to load data
@st.cache_data
def load_data():
    file_path = 'data/data_cleaned.csv'  # Update the path if necessary
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['VITI'].astype(str) + '-' + data['MUAJI'].astype(str))
    return data

data = load_data()

# Sidebar for navigation
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Select a page", ["Main", "3D Visualization"])

# Main page
if page_selection == "Main":
    st.title("Fines Data Visualization - Main")

    # Sidebar filters for the main page
    selected_sectors = st.sidebar.multiselect('Choose sectors to display', data['PERSHKRIMI_SEKTORIT'].unique(), default=data['PERSHKRIMI_SEKTORIT'].unique())
    selected_municipalities = st.sidebar.multiselect('Choose municipalities to display', data['KOMUNA'].unique(), default=data['KOMUNA'].unique())
    selected_years = st.sidebar.selectbox('Choose a year to display', ['All'] + list(data['VITI'].unique()), index=0)

    # Apply filters to data
    filtered_data = data[data['PERSHKRIMI_SEKTORIT'].isin(selected_sectors) & data['KOMUNA'].isin(selected_municipalities)]
    if selected_years != 'All':
        filtered_data = filtered_data[filtered_data['VITI'] == selected_years]

    # Visualizations for the main page
    if not filtered_data.empty:
        # Heat Map
        st.subheader("Heat Map: Density of Fines in Municipalities by Sector")
        heat_map_data = filtered_data.pivot_table(index='KOMUNA', columns='PERSHKRIMI_SEKTORIT', values='VLERA', aggfunc='sum').fillna(0)
        fig_heat, ax_heat = plt.subplots(figsize=(15, 10))  # Adjusted for a larger figure
        sns.heatmap(heat_map_data, annot=False, cmap='viridis', ax=ax_heat)
        st.pyplot(fig_heat)

        # Box Plot
        st.subheader("Box Plot: Distribution of Fine Values by Sector")
        fig_box, ax_box = plt.subplots(figsize=(15, 10))  # Adjusted for a larger figure
        sns.boxplot(x='PERSHKRIMI_SEKTORIT', y='VLERA', data=filtered_data, ax=ax_box)
        plt.xticks(rotation=90)
        st.pyplot(fig_box)

        # Multi-Series Line Graph
        st.subheader("Multi-Series Line Graph: Trend of Fines Over Time by Sector")
        line_graph_data = filtered_data.groupby(['Date', 'PERSHKRIMI_SEKTORIT'])['VLERA'].sum().unstack().fillna(0)
        fig_line, ax_line = plt.subplots(figsize=(15, 10))  # Adjusted for a larger figure
        line_graph_data.plot(ax=ax_line)
        plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig_line)



elif page_selection == "3D Visualization":
    st.title("3D Scatter Plot Visualization")

    # Create 3D Scatter Plot with Plotly
    st.subheader("3D Scatter Plot: Number of Fines, Fine Amounts, and Type of Penalty")
    fig_3d = px.scatter_3d(
        data,
        x='NR_TATIMIT',
        y='NR_GJOBAVE',
        z='VLERA',
        color='PERSHKRIMI_SEKTORIT',
        title='3D Scatter Plot: Tax Registrations, Number of Jobs, and Value by Sector',
        labels={'NR_TATIMIT': 'Number of Tax Registrations', 'NR_GJOBAVE': 'Number of Jobs', 'VLERA': 'Value'},
        opacity=0.7
    )

    # Update the layout to adjust the legend position and increase its height
    fig_3d.update_layout(
        margin=dict(l=0, r=0, b=0, t=0),  # Minimize margins around the plot
        legend=dict(
            orientation="h",  # Horizontal orientation for the legend
            yanchor="top",
            y=-0.5,  # Lower the legend further down the plot
            xanchor="center",
            x=0.5,  # Center the legend horizontally
            title_font=dict(size=14),
            font=dict(size=12),
            bgcolor='rgba(255,255,255,0.9)'  # Semi-transparent background for clarity
        ),
        height=700,  # Increase the height to provide more space for the legend
        width=900,   # Set the width as necessary
    )

    # Display the plot
    st.plotly_chart(fig_3d, use_container_width=False)

