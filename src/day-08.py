import itertools
import math

import networkx as nx

def euc_dist(cord_a, cord_b):
    s = [(x - y) ** 2 for x, y in zip(cord_a, cord_b)]
    return math.sqrt(sum(s))

def part1(data: str):
    lines = list(map(lambda line: tuple(map(int, line.split(','))), data.splitlines()))
    distances = []
    for combination in itertools.combinations(lines, 2):
        distances.append([euc_dist(*combination), combination])
    shortest = sorted(distances, key=lambda x: x[0])[:10]

    connections = []
    for el in shortest:
        connections.append(el[1])

    G = nx.Graph()
    G.add_edges_from(connections)

    components = list(nx.connected_components(G))
    s = sorted(components, key=len, reverse=True)[:3]

    return math.prod(len(x) for x in s)


def part2(data: str):
    lines = list(map(lambda line: tuple(map(int, line.split(','))), data.splitlines()))
    distances = []
    for combination in itertools.combinations(lines, 2):
        distances.append([euc_dist(*combination), combination])
    shortest = sorted(distances, key=lambda x: x[0])

    cnt = 10
    result = 0
    visited = set()
    while True:
        connections = []
        for i in range(0, cnt):
            connections.append(shortest[i][1])
            visited.add(shortest[i][1][0])
            visited.add(shortest[i][1][1])

        if len(visited) < len(lines):
            cnt += 1
            continue

        G = nx.Graph()
        G.add_edges_from(connections)

        if nx.is_connected(G):
            result = connections[-1][0][0] * connections[-1][1][0]
            break
        cnt += 1

    return result
