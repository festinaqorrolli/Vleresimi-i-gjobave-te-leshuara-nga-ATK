import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import plotly.express as px


# Funksioni per me load data
@st.cache_data
def load_data():
    file_path = 'data/data_cleaned.csv'  # Update path-in
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['VITI'].astype(str) + '-' + data['MUAJI'].astype(str))
    return data


data = load_data()

# Sidebar per navigation
st.sidebar.title("Navigimi")
page_selection = st.sidebar.radio("Selektoni faqen", ["Main", "3D Vizualizimi"])
# Main page
if page_selection == "Main":
    st.title("Vizualizimi i të dhënave të gjobave - Kryesor")

    # Filtrat e shiritit anësor për faqen kryesore
    selected_sectors = st.sidebar.multiselect('Zgjidhni sektorët për të shfaqur', data['PERSHKRIMI_SEKTORIT'].unique(),
                                              default=data['PERSHKRIMI_SEKTORIT'].unique())
    selected_municipalities = st.sidebar.multiselect('Zgjidhni bashkitë për tu shfaqur', data['KOMUNA'].unique(), default=data['KOMUNA'].unique())
    selected_years = st.sidebar.selectbox('Zgjidhni një vit për të shfaqur', ['All'] + list(data['VITI'].unique()),
                                          index=0)

    # Aplikoni filtra në të dhëna
    filtered_data = data[
        data['PERSHKRIMI_SEKTORIT'].isin(selected_sectors) & data['KOMUNA'].isin(selected_municipalities)]
    if selected_years != 'All':
        filtered_data = filtered_data[filtered_data['VITI'] == selected_years]


    # Vizualizime për faqen kryesore
    if not filtered_data.empty:
    # Heat Map
        st.subheader("Heat Map: Dendësia e gjobave në komuna sipas sektorëve")
    heat_map_data = filtered_data.pivot_table(index='KOMUNA', columns='PERSHKRIMI_SEKTORIT', values='VLERA',
                                              aggfunc='sum').fillna(0)
    fig_heat, ax_heat = plt.subplots(figsize=(15, 10))
    sns.heatmap(heat_map_data, annot=False, cmap='viridis', ax=ax_heat)
    st.pyplot(fig_heat)

    # Box Plot
    st.subheader("Komploti i kutisë: Shpërndarja e vlerave të bukura sipas sektorëve")
    fig_box, ax_box = plt.subplots(figsize=(15, 10))
    sns.boxplot(x='PERSHKRIMI_SEKTORIT', y='VLERA', data=filtered_data, ax=ax_box)
    plt.xticks(rotation=90)
    st.pyplot(fig_box)

    # Multi-Series Line Graph
    st.subheader("Grafiku i linjës me shumë seri: Trendi i gjobave me kalimin e kohës sipas sektorëve")
    line_graph_data = filtered_data.groupby(['Date', 'PERSHKRIMI_SEKTORIT'])['VLERA'].sum().unstack().fillna(0)
    fig_line, ax_line = plt.subplots(figsize=(15, 10))
    line_graph_data.plot(ax=ax_line)
    plt.legend(title='Sektor', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig_line)

    elif page_selection == "3D Vizualizimi":
    st.title("3D Scatter Plot Vizualizimi")

    # Krijo 3D Scatter Plot me Plotly
    st.subheader("3D Scatter Plot: Numri i gjobave, shumat e gjobave dhe lloji i dënimit")
    fig_3d = px.scatter_3d(
        data,
        x='NR_TATIMIT',
        y='NR_GJOBAVE',
        z='VLERA',
        color='PERSHKRIMI_SEKTORIT',
        title='3D Scatter Plot: Regjistrimet tatimore, numri i vendeve të punës dhe vlera sipas sektorëve',
        labels={'NR_TATIMIT': 'Numri i Regjistrimeve Tatimore', 'NR_GJOBAVE': 'Numri i Gjobave', 'VLERA': 'Value'},
        opacity=0.7
    )

    # Përditësoni paraqitjen për të rregulluar pozicionin e legjendës dhe për të rritur lartësinë e saj
    fig_3d.update_layout(
        margin=dict(l=0, r=0, b=0, t=0),  # Minimizoni kufijtë rreth komplotit
        legend=dict(
            orientation="h",  # Orientimi horizontal për legjendën
            yanchor="top",
            y=-0.5,  # Uleni legjendën më poshtë në komplot
            xanchor="center",
            x=0.5,  # Përqendroni legjendën horizontalisht
            title_font=dict(size=14),
            font=dict(size=12),
            bgcolor='rgba(255,255,255,0.9)'  # Sfondi gjysmë transparent për qartësi
        ),
        height=700,  # Rritni lartësinë për të siguruar më shumë hapësirë për legjendën
        width=900,  # Vendosni gjerësinë sipas nevojës
    )

    # Display plot
    st.plotly_chart(fig_3d, use_container_width=False)
