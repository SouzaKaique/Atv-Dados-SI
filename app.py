import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Mental Health Dashboard',
    layout='wide'
)

st.title('Mental Health Dashboard')

st.markdown(
    'Dashboard interativa sobre saude mental, burnout e ambiente de trabalho.'
)

df = pd.read_csv('mental_health_workplace.csv')

df = df.rename(columns={
    'country': 'Pais',
    'gender': 'Genero',
    'stress_level': 'Nivel_Estresse',
    'burnout_risk_score': 'Risco_Burnout',
    'sleep_hours_per_night': 'Horas_Sono_Noite',
    'work_model': 'Modelo_Trabalho',
    'intention_to_leave': 'Intencao_Sair',
    'employer_support_level': 'Suporte_Empresa',
    'job_satisfaction_score': 'Satisfacao',
    'productivity_score': 'Produtividade',
    'age_group': 'Faixa_Etaria'
})

df['Genero'] = df['Genero'].replace({
    'Male': 'Masculino',
    'Female': 'Feminino',
    'Non-binary': 'Nao Binario',
    'Prefer not to say': 'Prefiro nao informar'
})

df['Nivel_Estresse'] = df['Nivel_Estresse'].replace({
    'Low': 'Baixo',
    'Moderate': 'Moderado',
    'High': 'Alto',
    'Very Low': 'Muito Baixo',
    'Very Severe': 'Muito Severo'
})

df['Modelo_Trabalho'] = df['Modelo_Trabalho'].replace({
    'Remote': 'Remoto',
    'Hybrid': 'Hibrido',
    'On-site': 'Presencial'
})

df['Intencao_Sair'] = df['Intencao_Sair'].replace({
    'Very Likely': 'Muito Provavel',
    'Likely': 'Provavel',
    'Neutral': 'Neutro',
    'Unlikely': 'Improvavel',
    'Very Unlikely': 'Muito Improvavel'
})

df['Suporte_Empresa'] = df['Suporte_Empresa'].replace({
    'Poor': 'Ruim',
    'Average': 'Medio',
    'Good': 'Bom',
    'Excellent': 'Excelente'
})

df['Faixa_Etaria'] = df['Faixa_Etaria'].replace({
    '18-24': '18 a 24',
    '25-34': '25 a 34',
    '35-44': '35 a 44',
    '45-54': '45 a 54',
    '55+': '55 ou mais'
})

st.sidebar.header('Filtros')

st.sidebar.markdown('---')

filtro_genero = st.sidebar.multiselect(
    'Genero',
    options=df['Genero'].unique()
)

filtro_pais = st.sidebar.multiselect(
    'Pais',
    options=df['Pais'].unique()
)

filtro_estresse = st.sidebar.multiselect(
    'Nivel de Estresse',
    options=df['Nivel_Estresse'].unique()
)

filtro_modelo = st.sidebar.multiselect(
    'Modelo de Trabalho',
    options=df['Modelo_Trabalho'].unique()
)

filtro_saida = st.sidebar.multiselect(
    'Intencao de Sair',
    options=df['Intencao_Sair'].unique()
)

st.sidebar.markdown('---')

st.sidebar.caption(
    'Filtros interativos do dashboard'
)

df_filtrado = df.copy()

if filtro_genero:
    df_filtrado = df_filtrado[
        df_filtrado['Genero'].isin(filtro_genero)
    ]

if filtro_pais:
    df_filtrado = df_filtrado[
        df_filtrado['Pais'].isin(filtro_pais)
    ]

if filtro_estresse:
    df_filtrado = df_filtrado[
        df_filtrado['Nivel_Estresse'].isin(filtro_estresse)
    ]

if filtro_modelo:
    df_filtrado = df_filtrado[
        df_filtrado['Modelo_Trabalho'].isin(filtro_modelo)
    ]

if filtro_saida:
    df_filtrado = df_filtrado[
        df_filtrado['Intencao_Sair'].isin(filtro_saida)
    ]

st.subheader('Indicadores Gerais')

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric(
    'Registros',
    len(df_filtrado)
)

kpi2.metric(
    'Media Burnout',
    round(df_filtrado['Risco_Burnout'].mean(), 2)
)

kpi3.metric(
    'Media Sono',
    round(df_filtrado['Horas_Sono_Noite'].mean(), 2)
)

kpi4.metric(
    'Produtividade',
    round(df_filtrado['Produtividade'].mean(), 2)
)

kpi5.metric(
    'Satisfacao',
    round(df_filtrado['Satisfacao'].mean(), 2)
)

col1, col2 = st.columns(2)

with col1:

    st.subheader('Nivel de Estresse')

    fig1, ax1 = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df_filtrado,
        x='Nivel_Estresse',
        hue='Nivel_Estresse',
        palette='Purples',
        legend=False,
        ax=ax1
    )

    plt.xticks(rotation=20)

    st.pyplot(fig1)

with col2:

    st.subheader('Modelo de Trabalho')

    fig2 = px.histogram(
        df_filtrado,
        x='Modelo_Trabalho',
        color='Modelo_Trabalho',
        color_discrete_sequence=px.colors.sequential.Purples
    )

    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:

    st.subheader('Sono x Burnout')

    fig3 = px.scatter(
        df_filtrado,
        x='Horas_Sono_Noite',
        y='Risco_Burnout',
        color='Nivel_Estresse',
        color_discrete_sequence=px.colors.sequential.Purples
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    st.subheader('Intencao de Sair')

    fig4 = px.pie(
        df_filtrado,
        names='Intencao_Sair',
        color_discrete_sequence=px.colors.sequential.Purples
    )

    st.plotly_chart(fig4, use_container_width=True)

col5, col6 = st.columns(2)

with col5:

    st.subheader('Suporte da Empresa')

    fig5 = px.histogram(
        df_filtrado,
        x='Suporte_Empresa',
        color='Suporte_Empresa',
        color_discrete_sequence=px.colors.sequential.Purples
    )

    st.plotly_chart(fig5, use_container_width=True)

with col6:

    st.subheader('Burnout por Pais')

    df_paises = df_filtrado.groupby('Pais')['Risco_Burnout'] \
                           .mean() \
                           .reset_index()

    fig6 = px.choropleth(
        df_paises,
        locations='Pais',
        locationmode='country names',
        color='Risco_Burnout',
        hover_name='Pais',
        color_continuous_scale='Purples'
    )

    st.plotly_chart(fig6, use_container_width=True)

st.subheader('Correlacao Entre Variaveis')

correlacao = df_filtrado.select_dtypes(
    include='number'
).corr()

fig7, ax7 = plt.subplots(figsize=(14,8))

sns.heatmap(
    correlacao,
    cmap='Purples',
    ax=ax7
)

st.pyplot(fig7)

