import streamlit as st
from math import log, floor
from datetime import time


def paulsLaw(seconds, old_distance, new_distance):
    return round(
        seconds + 5*log(new_distance / old_distance, 2),
        1
    )


def seconds_to_time(seconds):
    minute = int(seconds // 60)
    second = floor(seconds - 60*minute)
    microsecond = int(
        1e6 * (seconds - second - 60*minute)
    )
    return time(
        minute=minute,
        second=second,
        microsecond=microsecond
    )


def printable_time(time_obj):
    microsec = int(
        time_obj.microsecond / 1e5
    )
    return time_obj.strftime(
        f"%M:%S.{microsec}"
    )


st.header("Paul's Law Conversion")


col_type, col_distance = st.columns(2)

with col_type:
    given_type = st.radio(
        "",
        options=[
            "Split",
            "Time"
        ]
    )

with col_distance:
    distance = st.number_input(
        "Distance",
        value=1000,
        step=100
    )

input_min, input_sec = st.columns(2)

with input_min:
    minutes = st.number_input(
        "Minutes",
        min_value=1,
        value=2,
        step=1,
    )

with input_sec:
    seconds = round(
        st.number_input(
            "Seconds",
            min_value=0.0,
            max_value=59.9,
            value=30.0,
            step=0.1,
            format="%2.1f"
        ),
        1
    )


new_distance = st.number_input(
    "New Distance",
    value=1500,
    step=100
)

total_seconds = 60*minutes + seconds
if given_type == "Time":
    total_seconds *= (500/distance)


adjusted_seconds = paulsLaw(
    total_seconds,
    distance,
    new_distance
)
new_split = seconds_to_time(adjusted_seconds)

time_seconds = adjusted_seconds * (new_distance / 500)
new_time = seconds_to_time(time_seconds)

col_split, col_time = st.columns(2)

with col_split:
    st.subheader("New Split")
    st.write(
        printable_time(new_split)
    )

with col_time:
    st.subheader("New Time")
    st.write(
        printable_time(new_time)
    )

