from graphs import *

# edges = [[1, 7], [7, 2], [7, 6], [6, 5], [6, 11], [2, 5], [5, 9], [9, 4]]
# edges = [[1, 2], [1, 3], [3, 2], [3, 4], [4, 3]]
# edges = [[1, 1], [1, 2], [1, 2], [1, 3], [1, 3], [2, 3], [4, 5], [5, 6], [5, 7], [6, 7], [6, 8], [7, 8]]
# edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 7], [6, 7], [5, 8], [6, 9]]
# edges = [[1, 2], [3, 4], [5, 6]]
# edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 6]]
# edges = [[6, 4], [4, 3], [5, 1], [5, 2], [2, 1]]

def test_all_nodes1():
    edges = [[1, 7], [7, 2], [7, 6], [6, 5], [6, 11], [2, 5], [5, 9], [9, 4]]
    assert all_nodes(edges) == [1, 2, 4, 5, 6, 7, 9, 11]

def test_all_nodes2():
    edges = [[1, 2], [1, 3], [3, 2], [3, 4], [4, 3]]
    assert all_nodes(edges) == [1, 2, 3, 4]

def test_all_nodes3():
    edges = [[1, 1], [1, 2], [1, 2], [1, 3], [1, 3], [2, 3], [4, 5], [5, 6], [5, 7], [6, 7], [6, 8], [7, 8]]
    assert all_nodes(edges) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_all_nodes4():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 7], [6, 7], [5, 8], [6, 9]]
    assert all_nodes(edges) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_all_nodes5():
    edges = [[1, 2], [3, 4], [5, 6]]
    assert all_nodes(edges) == [1, 2, 3, 4, 5, 6]

def test_all_nodes6():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 6]]
    assert all_nodes(edges) == [1, 2, 3, 4, 5, 6]

def test_all_nodes7():
    edges = [[6, 4], [4, 3], [5, 1], [5, 2], [2, 1]]
    assert all_nodes(edges) == [1, 2, 3, 4, 5, 6]

def test_find_connected_subgraph11():
    edges = [[1, 7], [7, 2], [7, 6], [6, 5], [6, 11], [2, 5], [5, 9], [9, 4]]
    assert find_connected_subgraph(1, edges) == [1, 2, 4, 5, 6, 7, 9, 11]

def test_find_connected_subgraph12():
    edges = [[1, 7], [7, 2], [7, 6], [6, 5], [6, 11], [2, 5], [5, 9], [9, 4]]
    assert find_connected_subgraph(2, edges) == [1, 2, 4, 5, 6, 7, 9, 11]

def test_find_connected_subgraph21():
    edges = [[1, 2], [1, 3], [3, 2], [3, 4], [4, 3]]
    assert find_connected_subgraph(1, edges) == [1, 2, 3, 4]

def test_find_connected_subgraph22():
    edges = [[1, 2], [1, 3], [3, 2], [3, 4], [4, 3]]
    assert find_connected_subgraph(2, edges) == [1, 2, 3, 4]

def test_find_connected_subgraph31():
    edges = [[1, 1], [1, 2], [1, 2], [1, 3], [1, 3], [2, 3], [4, 5], [5, 6], [5, 7], [6, 7], [6, 8], [7, 8]]
    assert find_connected_subgraph(1, edges) == [1, 2, 3]

def test_find_connected_subgraph32():
    edges = [[1, 1], [1, 2], [1, 2], [1, 3], [1, 3], [2, 3], [4, 5], [5, 6], [5, 7], [6, 7], [6, 8], [7, 8]]
    assert find_connected_subgraph(4, edges) == [4, 5, 6, 7, 8]

def test_find_connected_subgraph41():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 7], [6, 7], [5, 8], [6, 9]]
    assert find_connected_subgraph(1, edges) == [1, 2, 3]

def test_find_connected_subgraph42():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 7], [6, 7], [5, 8], [6, 9]]
    assert find_connected_subgraph(4, edges) == [4, 5, 6, 7, 8, 9]

def test_find_connected_subgraph51():
    edges = [[1, 2], [3, 4], [5, 6]]
    assert find_connected_subgraph(1, edges) == [1, 2]

def test_find_connected_subgraph52():
    edges = [[1, 2], [3, 4], [5, 6]]
    assert find_connected_subgraph(3, edges) == [3, 4]

def test_find_connected_subgraph53():
    edges = [[1, 2], [3, 4], [5, 6]]
    assert find_connected_subgraph(5, edges) == [5, 6]

def test_find_connected_subgraph61():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 6]]
    assert find_connected_subgraph(1, edges) == [1, 2, 3]

def test_find_connected_subgraph62():
    edges = [[1, 2], [1, 3], [2, 3], [4, 5], [4, 6], [5, 6]]
    assert find_connected_subgraph(4, edges) == [4, 5, 6]

def test_find_connected_subgraph71():
    edges = [[6, 4], [4, 3], [5, 1], [5, 2], [2, 1]]
    assert find_connected_subgraph(6, edges) == [3, 4, 6]

def test_find_connected_subgraph72():
    edges = [[6, 4], [4, 3], [5, 1], [5, 2], [2, 1]]
    assert find_connected_subgraph(5, edges) == [1, 2, 5]
