#app.py
import streamlit as st
import intakeform
import costperwatt
import scorecard_estimated

PAGES = {
    "Intake Form": intakeform,
    "Cost Per Watt": costperwatt,
    "ScoreCard Estimated": scorecard_estimated,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()