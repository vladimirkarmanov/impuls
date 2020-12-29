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

        wcss = self._calculate_wcss(X)
        n_clusters = self._optimal_number_of_clusters(wcss)
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
        y_kmeans = kmeans.fit_predict(X)
        clusters = {c + 1: [] for c in range(max(y_kmeans) + 1)}
        for i in range(len(dataset)):
            student = {
                'name': str(dataset.iloc[i][0]),
                'academicDegree': int(dataset.iloc[i][1]),
                'academicRank': int(dataset.iloc[i][2]),
                'basicLevel': int(dataset.iloc[i][3]),
                'basicQualification': int(dataset.iloc[i][4])
            }
            clusters[y_kmeans[i] + 1].append(student)

        return clusters
