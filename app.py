import streamlit as st
import altair as alt

import os
import pandas as pd


st.set_page_config(layout = 'wide')

df = pd.read_csv('./RGDP-BEA-A.csv')
print(df)

col_selected = df.columns.to_list()[1:3]






selector = alt.selection_point(
        nearest = True,
        on = 'pointerover',
        clear = 'pointerout',
        empty = False
        )



bar_selector = alt.selection_interval(encodings = ['x'])

rule = alt.Chart(df).mark_rule(color = 'grey').encode(
        x = 'Time:N',
        y2 = alt.value('height'),
        opacity = alt.condition(selector, alt.value(1), alt.value(0))
        ).add_params(selector).transform_filter(bar_selector)



lines = alt.Chart(df).transform_fold(col_selected).mark_line().encode(
        x = alt.X('Time:N').scale(zero = False),
        y = alt.Y('value:Q').scale(zero = False),
        color = 'key:N'
        ).transform_filter(bar_selector)


bar = alt.Chart(df).mark_bar(color = 'grey').encode(
        x = alt.X('Time:N'),
        y = alt.value(1),
        opacity = alt.value(0)
        ).add_params(bar_selector)




chart = alt.layer(rule, lines)
chart = (chart & bar)










st.altair_chart(chart, width = 'stretch')
