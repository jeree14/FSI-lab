# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print("Anchura")
print(search.breadth_first_graph_search(ab).path())
print("Profundidad")
print(search.depth_first_graph_search(ab).path())
print("Ramificacion y acotacion")
print(search.b_b_graph_search(ab).path())
print("Ramificacion y acotacion con subestimacion")
print(search.b_b_subestimacion_graph_search(ab).path())

# Resultados (A -> B):
# Anchura:                      8 expandidos, coste 450 (A-S-F-B)
# Profundidad:                  7 expandidos, coste 733 (A-T-L-M-D-C-P-B)
# Ramificacion y acotacion:     12 expandidos, coste 418 (A-S-R-P-B)
# B&B con subestimacion:        5 expandidos, coste 418 (A-S-R-P-B)
