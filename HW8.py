import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)  # перетворюємо список у heap

    total_cost = 0

    while len(cable_lengths) > 1:
        # беремо два найменші кабелі
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        # обчислюємо вартість з'єднання і додаємо її до загальної вартості
        connection_cost = cable1 + cable2
        total_cost += connection_cost

        # додаємо новий кабель до heap з вартістю з'єднання
        heapq.heappush(cable_lengths, connection_cost)

    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cable_lengths)
print("Мінімальна вартість для з'єднання кабелів:", min_cost)