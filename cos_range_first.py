import numpy as np

users_stats = np.array(  # Наша база данных
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])  # Наш покупатель, которому нужно порекомендовать

cos_ranges = []


def cosin(a, b):
    """
    Функция считает cos расстояние, по формуле из презентации
    """
    aLength = np.linalg.norm(a)
    bLength = np.linalg.norm(b)

    return np.dot(a, b) / (aLength * bLength)


for user in users_stats:  # Сравним всех польз. из БД с нашим
    cos_ranges.append(cosin(user, next_user_stats))

print(cos_ranges)

sorted_cos_ranges = sorted(cos_ranges)[::-1]  # Отсортируем по убыванию

print(cos_ranges.index(sorted_cos_ranges[0])+1)  # найдем id пользователя, наиболее подходящего к нашему

print(cos_ranges.index(sorted_cos_ranges[1])+1)  # так как рекоммендовать было нечего, ищем второго наиболее близкого

