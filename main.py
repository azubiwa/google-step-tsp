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

def greedy(cities):
    return_cities = [0]
    last_city = 0
    seen = [False] * len(cities)
    seen[0] = True
    for i in range(len(cities) - 1):
        last_city = closet_city(cities, seen, last_city)
        return_cities.append(last_city)
        seen[last_city] = True
    return return_cities

def crossed_city(cities, cities_path, n, m): # n, n+1番目の辺とm, m+1番目の辺の交差判定
    if n == m or abs(n - m) == 1 or (max(n, m) == len(cities) - 1 and min(n, m) == 0):
        return False
    n_x1, n_y1 = cities[cities_path[n]]
    n_x2, n_y2 = cities[(cities_path[(n+1) % len(cities)])]
    m_x1, m_y1 = cities[cities_path[m]]
    m_x2, m_y2 = cities[(cities_path[(m+1) % len(cities)])]
    # n, mの辺の長さの2乗の合計
    nm_dist = abs(n_x1 - n_x2) * abs(n_x1 - n_x2) + abs(n_y1 - n_y2) * abs(n_y1 - n_y2) + abs(m_x1 - m_x2) * abs(m_x1 - m_x2) + abs(m_y1 - m_y2) * abs(m_y1 - m_y2)
    # n, m+1 と n+1, mの辺の長さの2乗の合計
    mixed_dist = abs(n_x1 - m_x1) * abs(n_x1 - m_x1) + abs(n_y1 - m_y1) * abs(n_y1 - m_y1) + abs(m_x2 - n_x2) * abs(m_x2 - n_x2) + abs(m_y2 - n_y2) * abs(m_y2 - n_y2)
    if nm_dist <= mixed_dist:
        return False
    else:
        return True

def two_opt(cities, cities_path):
    maybe_crossing = cities_path[:]
    while maybe_crossing: # 交差する可能性のある頂点が空になるまで
        # city = maybe_crossing[0]
        city = maybe_crossing.pop(0)
        for i in range(len(cities)):
            if cities_path[i] == city:
                city_index = i
                break
        for i in range(len(cities)):
            if crossed_city(cities, cities_path, city_index, i):
                cities_path[min(city_index, i)+1:max(city_index, i)+1] = reversed(cities_path[min(city_index, i)+1:max(city_index, i)+1])
                maybe_crossing.append(cities_path[i])
                maybe_crossing = list(set(maybe_crossing))
                break
            # if i == len(cities) - 1: # 最後まで見て交差しなかったら
                # maybe_crossing.pop(0)
            # print(city, i, maybe_crossing, cities_path)
    return cities_path

def TSP_solve(cities):
    cities_path = greedy(cities)
    cities_path = two_opt(cities, cities_path)
    return cities_path


if __name__ == "__main__":
    for i in range(7):
        file_name = "input_" + str(i) + ".csv"
        cities = read_input(file_name)
        ans = TSP_solve(cities)
        with open("output_" + str(i) + ".csv", "w") as file:
            file.write(format_tour(ans))
