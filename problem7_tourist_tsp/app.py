import streamlit as st
from brute_force_tsp import brute_force_tsp

st.title("Tourist Travel Planner (TSP - Brute Force)")

n = st.number_input("Number of cities", min_value=2, max_value=6)

dist_matrix = []
for i in range(n):
    row = st.text_input(f"Distances from city {i}", "0 1 2 3 4 5")
    dist_matrix.append(list(map(int, row.split())))

if st.button("Find Optimal Route"):
    route, dist = brute_force_tsp(dist_matrix)
    st.write("Route:", route)
    st.write("Distance:", dist)
