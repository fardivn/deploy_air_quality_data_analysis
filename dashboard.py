import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
import streamlit as st

all_data = pd.read_csv('data.csv')

st.header("Air Quality Data Analysis", divider="rainbow")
st.subheader("Temperatur")

tab_temp_monthly, tab_temp_yearly = st.tabs(["Monthly", "Yearly"])
 
with tab_temp_monthly:
    st.markdown("**Rata-Rata Temperatur Per Bulan**")
    trend_temp_monthly = all_data.groupby(["year", "month"])["TEMP"].mean().round(2)
    ax = trend_temp_monthly.plot(
        marker=".", 
        title=f"Rata-Rata Temperatur Per Bulan (\N{DEGREE SIGN}C)",
        figsize=(13,5),
        xticks=range(len(trend_temp_monthly)),
        colormap="Set3"
    )
    ax.set_xticklabels(trend_temp_monthly.index, rotation=90)
    plt.xlabel("Tahun, Bulan")
    fig = ax.figure
    st.pyplot(fig)
    
with tab_temp_yearly:
    st.markdown("**Rata-Rata Temperatur Per Tahun**")
    trend_temp_yearly = all_data.groupby("year")["TEMP"].mean().round(2)
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.plot(trend_temp_yearly, marker=".")
    ax.set_title(f"Rata-Rata Temperatur Per Tahun (\N{DEGREE SIGN}C)")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Tahun")
    st.pyplot(fig)

st.divider()
st.markdown("### Rata-Rata Temperatur di Setiap Station")

with st.container():
    fig, ax = plt.subplots(figsize=(10, 5))

    temp_station = all_data.groupby("station").mean(numeric_only=True).round(2)
    sns.barplot(
        y="station", 
        x="TEMP",
        data=temp_station.sort_values(by="TEMP"),
        ax=ax
    )
    ax.set_title(f"Rata-Rata Temperatur Berdasarkan Station (\N{DEGREE SIGN}C)")
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    st.pyplot(fig)

st.subheader("", divider="rainbow")
st.subheader("Tingkat Polusi")

tab_pm, tab_so2, tab_no2, tab_co, tab_o3 = st.tabs(["PM", "SO2", "NO2", "CO", "O3"])
trend_pm = all_data.groupby(["year", "month"]).mean(numeric_only=True).round(2)


with tab_pm:
    st.markdown("**Rata-Rata Konsentrasi Particulate Matter Per Bulan**")
    ax = trend_pm.plot(y=["PM2.5", "PM10"], marker=".")
    plt.title(f"Rata-Rata Konsentrasi Particulate Matter Per Bulan (\u03BCg/m\u00b3)")
    plt.xlabel(xlabel="Tahun, Bulan")
    plt.gcf().set_size_inches(13, 5)
    ax.set_xticks(range(len(trend_pm)))
    ax.set_xticklabels(trend_pm.index, rotation=90)
    fig = ax.figure
    st.pyplot(fig)

with tab_so2:
    st.markdown("**Rata-Rata Konsentrasi SO2 Per Bulan**")
    ax = trend_pm.plot(y="SO2", marker=".")
    plt.title("Rata-Rata Konsentrasi SO2 Per Bulan")
    plt.xlabel(xlabel="Tahun, Bulan")
    plt.gcf().set_size_inches(13, 5)
    ax.set_xticks(range(len(trend_pm)))
    ax.set_xticklabels(trend_pm.index, rotation=90)
    fig = ax.figure
    st.pyplot(fig)

with tab_no2:
    st.markdown("**Rata-Rata Konsentrasi NO2 Per Bulan**")
    ax = trend_pm.plot(y="NO2", marker=".")
    plt.title("Rata-Rata Konsentrasi NO2 Per Bulan")
    plt.xlabel(xlabel="Tahun, Bulan")
    plt.gcf().set_size_inches(13, 5)
    ax.set_xticks(range(len(trend_pm)))
    ax.set_xticklabels(trend_pm.index, rotation=90)
    fig = ax.figure
    st.pyplot(fig)

with tab_co:
    st.markdown("**Rata-Rata Konsentrasi CO Per Bulan**")
    ax = trend_pm.plot(y="CO", marker=".")
    plt.title("Rata-Rata Konsentrasi CO Per Bulan")
    plt.xlabel(xlabel="Tahun, Bulan")
    plt.gcf().set_size_inches(13, 5)
    ax.set_xticks(range(len(trend_pm)))
    ax.set_xticklabels(trend_pm.index, rotation=90)
    fig = ax.figure
    st.pyplot(fig)

with tab_o3:
    st.markdown("**Rata-Rata Konsentrasi O3 Per Bulan**")
    ax = trend_pm.plot(y="O3", marker=".")
    plt.title("Rata-Rata Konsentrasi O3 Per Bulan")
    plt.xlabel(xlabel="Tahun, Bulan")
    plt.gcf().set_size_inches(13, 5)
    ax.set_xticks(range(len(trend_pm)))
    ax.set_xticklabels(trend_pm.index, rotation=90)
    fig = ax.figure
    st.pyplot(fig)