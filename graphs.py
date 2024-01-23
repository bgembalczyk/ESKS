def find_connected_subgraph(start_node, edges):
    # Find a connected subgraph starting from a given node in a graph
    result = [start_node]
    for node in result:
        for edge in edges:
            if edge[0] == node and edge[1] not in result:
                result.append(edge[1])
            if edge[1] == node and edge[0] not in result:
                result.append(edge[0])
    result.sort()
    return result

def all_nodes(edges):
    # Retrieve all unique nodes from a list of edges in a graph
    result = []
    for edge in edges:
        if edge[0] not in result:
            result.append(edge[0])
        if edge[1] not in result:
            result.append(edge[1])
    result.sort()
    return result
