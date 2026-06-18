from common import read_input, format_tour, print_tour

def closet_city(cities, seen, n):
    min_dist = float("INF")
    next_city = n
    a = cities[n][0]
    b = cities[n][1]
    for i, city in enumerate(cities):
        if seen[i]:
            continue
        x = city[0]
        y = city[1]
        dist = abs(a-x) * abs(a-x) + abs(b-y) * abs(b-y)
        if dist < min_dist:
            next_city = i
            min_dist = dist
    return next_city

def TSP_solve(cities):
    ans = [0]
    last_city = 0
    seen = [False] * len(cities)
    seen[0] = True
    for i in range(len(cities) - 1):
        last_city = closet_city(cities, seen, last_city)
        ans.append(last_city)
        seen[last_city] = True

    return ans


if __name__ == "__main__":
    for i in range(6):
        file_name = "input_" + str(i) + ".csv"
        cities = read_input(file_name)
        ans = TSP_solve(cities)
        with open("output_" + str(i) + ".csv", "w") as file:
            file.write(format_tour(ans))
    # cities = read_input("input_2.csv")
    # ans = TSP_solve(cities)
    # with open("output_2.csv", "w") as file:
    #     file.write(format_tour(ans))
