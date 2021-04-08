from math import sqrt
from typing import List

import pandas
from sklearn.cluster import KMeans


class ClusterAnalysis:
    def _calculate_wcss(self, data, max_clusters_count=10):
        wcss = []
        for i in range(1, max_clusters_count + 1):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
            kmeans.fit(data)
            wcss.append(kmeans.inertia_)
        return wcss

    def _optimal_number_of_clusters(self, wcss: list):
        x1, y1 = 2, wcss[0]
        x2, y2 = 10, wcss[len(wcss) - 1]

        distances = []
        for i in range(len(wcss)):
            x0 = i + 2
            y0 = wcss[i]
            numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
            denominator = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
            distances.append(numerator / denominator)
        return distances.index(max(distances)) + 3

    def _get_dataset(self, data: List[dict] = None):
        return pandas.DataFrame(data)

    def cluster_analysis(self, data) -> dict:
        dataset = self._get_dataset(data)
        X = dataset.iloc[:, [1, 2, 3, 4]].values

        n_clusters = 5
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
        y_kmeans = kmeans.fit_predict(X)
        clusters = {c + 1: [] for c in range(max(y_kmeans) + 1)}
        for i in range(len(dataset)):
            name = str(dataset.iloc[i][0])
            academic_degree = int(dataset.iloc[i][1])
            academic_rank = int(dataset.iloc[i][2])
            basic_qualification = int(dataset.iloc[i][3])
            time_without_training = int(dataset.iloc[i][4])
            group_name = 'Требуется повышение квалификации'
            if basic_qualification >= 13 and time_without_training < 40:
                group_name = 'Высоко-квалифицированные'
            elif basic_qualification >= 11 and 20 <= time_without_training <= 30:
                group_name = 'Выше среднего уровень знаний'
            elif basic_qualification >= 9 and 30 <= time_without_training <= 40:
                group_name = 'Средне-квалифицированные'
            elif time_without_training == 10 and time_without_training < 60:
                group_name = 'Высокий уровень знаний'
            elif basic_qualification <= 8 and time_without_training > 60:
                group_name = 'Низкий уровень знаний'
            student = {
                'groupName': group_name,
                'name': name,
                'academicDegree': academic_degree,
                'academicRank': academic_rank,
                'basicQualification': basic_qualification,
                'timeWithoutTraining': time_without_training
            }
            clusters[y_kmeans[i] + 1].append(student)

        return clusters