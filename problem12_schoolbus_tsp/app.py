import streamlit as st
from nearest_neighbor import nearest_neighbor

st.title("School Bus Route Optimization (TSP - Heuristic)")

n = st.number_input("Number of stops", min_value=2, max_value=10)

dist_matrix = []
for i in range(n):
    row = st.text_input(f"Distances from stop {i}", "0 1 2 3 4 5 6 7 8 9")
    dist_matrix.append(list(map(int, row.split())))

if st.button("Find Route"):
    route, dist = nearest_neighbor(dist_matrix)
    st.write("Route:", route)
    st.write("Distance:", dist)
