from datetime import datetime
from math import sqrt
from typing import List

import pandas
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class ClusterAnalysisService:
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

    def map_params(self, data: List[dict], reverse: bool) -> List[dict]:
        if not reverse:
            for record in data:
                if 'канд' in record['academicDegree'].lower():
                    record['academicDegree'] = 0
                elif 'докт' in record['academicDegree'].lower():
                    record['academicDegree'] = 1

                if 'доц' in record['academicRank'].lower():
                    record['academicRank'] = 0
                elif 'проф' in record['academicRank'].lower():
                    record['academicRank'] = 1

                if 'перв' in record['qualificationCategory'].lower():
                    record['qualificationCategory'] = 0
                elif 'высш' in record['qualificationCategory'].lower():
                    record['qualificationCategory'] = 1
        else:
            for record in data:
                if record['academicDegree'] == 0:
                    record['academicDegree'] = 'Кандидат'
                elif record['academicDegree'] == 1:
                    record['academicDegree'] = 'Доктор'

                if record['academicRank'] == 0:
                    record['academicRank'] = 'Доцент'
                elif record['academicRank'] == 1:
                    record['academicRank'] = 'Профессор'

                if record['qualificationCategory'] == 0:
                    record['qualificationCategory'] = 'Первая'
                elif record['qualificationCategory'] == 1:
                    record['qualificationCategory'] = 'Высшая'
        return data

    def cluster_analysis(self, data) -> dict:
        dataset = self._get_dataset(data)
        x = dataset.iloc[:, [1, 2, 3, 4]].values
        # normalization
        scaler = StandardScaler()
        x = scaler.fit_transform(x)

        n_clusters = 5
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=0)
        y_kmeans = kmeans.fit_predict(x)
        clusters = {c + 1: [] for c in range(max(y_kmeans) + 1)}
        for i in range(len(dataset)):
            name = str(dataset.iloc[i][0])
            academic_degree = int(dataset.iloc[i][1])
            academic_rank = int(dataset.iloc[i][2])
            qualification_category = int(dataset.iloc[i][3])
            last_training_year = int(dataset.iloc[i][4])
            group_name = ''
            year = datetime.now().year
            if year - last_training_year >= 5:
                group_name = 'Требуется повышение квалификации'
            elif year - last_training_year >= 4:
                group_name = 'Низкий уровень квалификации'
            elif year - last_training_year >= 3:
                group_name = 'Ниже среднего уровень квалификации'
            elif year - last_training_year >= 2:
                group_name = 'Средний уровень квалификации'
            elif year - last_training_year >= 0:
                group_name = 'Высокий уровень квалификации'
            student = {
                'groupName': group_name,
                'name': name,
                'academicDegree': academic_degree,
                'academicRank': academic_rank,
                'qualificationCategory': qualification_category,
                'lastTrainingYear': last_training_year
            }
            clusters[y_kmeans[i] + 1].append(self.map_params([student], reverse=True)[0])

        return clusters
