import sample
import cluster
import link
import math
from collections import OrderedDict


class AgglomerativeClustring:

    def __init__(self, link1, samples):
        self.link = link1
        self.clusters = []
        for sample in samples:
            self.clusters.append(cluster.Cluster(sample.s_id, [sample]))

    def compute_silhoeutte(self):
        silhoeutte = {}
        for cluster in self.clusters:
            for sample in cluster:
                in_xi = 0
                out_xi = 99999999
                for other_sample in cluster:
                    if sample != other_sample:
                        in_xi += sample.compute_euclidean_distance(other_sample)
                in_xi = in_xi / (len(cluster.samples) - 1)
                for other_cluster in self.clusters:
                    if cluster != other_cluster:
                        temp = sample.compute_distance_between_sample_to_cluster(sample, cluster)
                        if temp < out_xi:
                            out_xi = temp
                silhoeutte[sample] = (out_xi - in_xi) / max(in_xi, out_xi)
        return silhoeutte

    def compute_summery_silhoeutte(self):
        silhoeutte = {}

        for cluster in self.clusters:
            cluster_silhoeutte = 0
            if len(cluster.samples) != 1:
                for sample in cluster.samples:
                    in_xi = 0
                    out_xi = 99999999
                    for other_sample in cluster.samples:
                        if sample != other_sample:
                            in_xi += sample.compute_euclidean_distance(other_sample)
                    in_xi = in_xi / (len(cluster.samples) - 1)
                    for other_cluster in self.clusters:
                        if cluster != other_cluster:
                            temp = sample.compute_distance_between_sample_to_cluster(sample, cluster)
                            if temp < out_xi:
                                out_xi = temp
                    cluster_silhoeutte += (out_xi - in_xi) / max(in_xi, out_xi)
            silhoeutte[cluster.c_id] = cluster_silhoeutte
        return silhoeutte

    def compute_rand_index(self):
        pass

    def run(self, max_clusters):
        while len(self.clusters) != max_clusters:
            list_distanc_all_cluster = []
            for cluster in self.clusters:
                cluster_distances = []
                for index, other_cluster in enumerate(self.clusters):
                    if cluster != other_cluster:
                        cluster_distances.append(self.link.compute(cluster, other_cluster))
                    else:
                        cluster_distances.append(9999999999999)
                list_distanc_all_cluster.append(cluster_distances)
            min_index_distance_cluster1 = 0
            min_index_distance_cluster2 = 0
            min_value_distance = 9999999999999
            for index_list_distance_all_cluster1, cluster_distances1 in enumerate(list_distanc_all_cluster):
                temp_min = min(cluster_distances1)
                if min_value_distance > temp_min:
                    min_value_distance = temp_min
                    min_index_distance_cluster2 = cluster_distances1.index(temp_min)
                    min_index_distance_cluster1 = index_list_distance_all_cluster1

            self.clusters[min_index_distance_cluster1].merge(self.clusters[min_index_distance_cluster2])
            self.clusters.pop(min_index_distance_cluster2)


        self.link.print_type_link()
        silhouette_clusters = self.compute_summery_silhoeutte()
        for cluster in self.clusters:
            cluster.print_details(silhouette_clusters[cluster.c_id])
