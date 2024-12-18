import time

routes = [
    ("A", "B", 10),
    ("A", "C", 15),
    ("B", "D", 20),
    ("C", "D", 30),
    ("B", "E", 25),
    ("D", "E", 5)
]

def merge_sort_routes(routes):
    if len(routes) <= 1:
        return routes

    mid = len(routes) // 2
    left = merge_sort_routes(routes[:mid])
    right = merge_sort_routes(routes[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def greedy_route_selection(routes):
    # Urutkan rute menggunakan Merge Sort
    sorted_routes = merge_sort_routes(routes)
    selected_routes = []
    visited = set()

    for route in sorted_routes:
        asal, tujuan, biaya = route
        if asal not in visited or tujuan not in visited:
            selected_routes.append(route)
            visited.add(asal)
            visited.add(tujuan)

    return selected_routes

print("Rute awal:", routes)

start_time = time.perf_counter()
greedy_result = greedy_route_selection(routes)
end_time = time.perf_counter()

print("\nHasil Greedy dengan Merge Sort:")
for r in greedy_result:
    print(f"{r[0]} -> {r[1]} dengan biaya {r[2]}")

print(f"\nWaktu eksekusi: {end_time - start_time:.6f} detik")
