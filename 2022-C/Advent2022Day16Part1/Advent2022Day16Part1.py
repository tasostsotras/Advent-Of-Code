from utilities import parse_multi_string, shortest_path_unweighted
from itertools import product

arr = parse_multi_string(sep=" ")

flows = {}
edges = {}
for a in arr:
    name = a[1]
    flow = int(a[4][5:-1])
    neighbours = [x.replace(",", "") for x in a[9:]]
    flows[name] = flow
    edges[name] = neighbours

# find shortest distance between AA and any valve with non-zero flow,
# and shortest distance between any 2 valves with non-zero flow
valves_to_open = [v for v, flow in flows.items() if flow > 0]
distances = {}
for v0, v1 in product(["AA"] + valves_to_open, valves_to_open):
    if v0 != v1:
        distances[v0, v1] = shortest_path_unweighted(edges, v0, v1) + 1

# represent sets of open valves by encoding as binary
valve_inds = {name: i for i, name in enumerate(valves_to_open)}
valve_to_binary = {v: 2 ** v_ind for v, v_ind in valve_inds.items()}

# For any feasible set of valves that can be opened in 30 minutes, find optimal flow
# that can be achieved by opening these valves.
# members of to_visit contain: location, time, set of valves opened, total flow
to_visit = [["AA", 0, 0, 0]]
best_flow = 0
while len(to_visit) > 0:
    curr, t, valves_opened, total_flow = to_visit.pop()
    for v in valves_to_open:
        if valves_opened & (v_bin := valve_to_binary[v]) == 0:
            d = distances[curr, v]
            if d < 30 - t:
                new_flow = total_flow + (30 - t - d) * flows[v]
                to_visit.append([v, t + d, valves_opened + v_bin, new_flow])
    else:
        best_flow = max(best_flow, total_flow)

print(best_flow)
