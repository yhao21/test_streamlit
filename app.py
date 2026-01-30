import streamlit as st
import altair as alt

import os
import pandas as pd


st.set_page_config(layout = 'wide')

df = pd.read_csv('./RGDP-BEA-A.csv')


base = alt.Chart(df).mark_line().encode(
        x = alt.X('Time:N'),
        y = alt.Y('Gross domestic product')
        )


chart = base



st.altair_chart(chart, width = 'stretch')
