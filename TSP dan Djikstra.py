import networkx as nx
import time

def tsp_shortest_path(graph, start, end):
    start_time = time.time()
    shortest_path = nx.approximation.traveling_salesman_problem(graph, weight='weight', cycle=True)
    end_time = time.time()
    return shortest_path, end_time - start_time

def dijkstra_shortest_path(graph, start, end):
    start_time = time.time()
    shortest_path = nx.dijkstra_path(graph, start, end, weight='weight')
    end_time = time.time()
    return shortest_path, end_time - start_time

def print_iterations(iterations):
    print("Iterasi:")
    for i, path in enumerate(iterations):
        print(f"Iterasi {i + 1}: {path}")

def print_execution_time(time_taken):
    print(f"Waktu komputasi: {time_taken:.6f} detik")

def print_shortest_path(path):
    print("Hasil akhir (Shortest Path):")
    print(path)

def analyze_algorithm():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=10)
    graph.add_edge('A', 'G', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('D', 'E', weight=11)
    graph.add_edge('D', 'F', weight=10)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('E', 'G', weight=7)
    graph.add_edge('F', 'G', weight=9)

    print("Graf:")
    print(graph.edges())
    print("\nAlgoritma yang tersedia:")
    print("1. TSP")
    print("2. Dijkstra")

    choice = input("Pilih algoritma (1/2): ")

    if choice == "1":
        shortest_path, time_taken = tsp_shortest_path(graph, 'A', 'G')
        print("\nHasil TSP:")
        print("-------------")
        print_iterations(shortest_path)
        print_execution_time(time_taken)
        print_shortest_path(shortest_path)
    elif choice == "2":
        shortest_path, time_taken = dijkstra_shortest_path(graph, 'A', 'G')
        print("\nHasil Dijkstra:")
        print("-----------------")
        print_iterations([shortest_path])
        print_execution_time(time_taken)
        print_shortest_path(shortest_path)
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

if __name__ == '__main__':
    analyze_algorithm()