import cluster
import math


class AgglomerativeClustring:

    def __init__(self, link1, samples):
        self.link = link1
        self.clusters = []
        for sample in samples:
            self.clusters.append(cluster.Cluster(sample.s_id, [sample]))

    def comput_in_xi(self, cluster, sample):
        in_xi = 0
        for sample1 in cluster.samples:
            if sample != sample1:
                in_xi += sample.compute_euclidean_distance(sample1)
        return in_xi / (len(cluster.samples) - 1)

    def compute_out_xi(self, cluster, sample):
        out_xi = []
        for cluster1 in self.clusters:
            if cluster != cluster1:
                sum_distances = 0
                for sample1 in cluster1.samples:
                    sum_distances += sample.compute_euclidean_distance(sample1)
                out_xi.append(sum_distances / len(cluster1.samples))
        out_xi.sort()
        return out_xi[0]

    def compute_silhoeutte(self):
        silhoeutte = {}
        for cluster in self.clusters:
            for sample in cluster.samples:
                if len(cluster.samples) != 1:
                    out_xi = self.compute_out_xi(cluster, sample)
                    in_xi = self.comput_in_xi(cluster, sample)
                    silhoeutte[sample.s_id] = (out_xi - in_xi) / max(out_xi, in_xi)
                else:
                    silhoeutte[sample.s_id] = 0
        return silhoeutte

    def compute_summery_silhoeutte(self):
        silhoeutte = {}
        temp_silhoeutte = self.compute_silhoeutte()
        for cluster in self.clusters:
            silhoeutte[cluster.c_id] = 0
            if len(cluster.samples) != 1:
                for sample in cluster.samples:
                    silhoeutte[cluster.c_id] += temp_silhoeutte[sample.s_id]
                silhoeutte[cluster.c_id] /= len(cluster.samples)
            else:
                silhoeutte[cluster.c_id] = 0
        return silhoeutte

    def compute_summery_silhoeutte_all_cluster(self):
        temp_silhoeutte = self.compute_silhoeutte()
        sum_silhoeutte = 0
        sum_number_of_sample = 0
        for cluster in self.clusters:
            for sample in cluster.samples:
                sum_silhoeutte += temp_silhoeutte[sample.s_id]
                sum_number_of_sample += 1
        return sum_silhoeutte / sum_number_of_sample

    def compute_rand_index(self):
        sum_good_couples = 0
        sum_samples = 0
        for cluster1 in self.clusters:
            for sample1 in cluster1.samples:
                for cluster2 in self.clusters:
                    for sample2 in cluster2.samples:
                        if sample2 != sample1:
                            sum_samples += 1
                            if sample1.label == sample2.label and cluster1 == cluster2:
                                sum_good_couples += 1
                            if sample1.label != sample2.label and cluster1 != cluster2:
                                sum_good_couples += 1
        return sum_good_couples / sum_samples

    def run(self, max_clusters):
        # compute distance between all the clusters:
        list_distance_all_cluster = []
        for cluster in self.clusters:
            cluster_distances = []
            for index, other_cluster in enumerate(self.clusters):
                if cluster != other_cluster:
                    cluster_distances.append(self.link.compute(cluster, other_cluster))
                else:
                    cluster_distances.append(99999999)
            list_distance_all_cluster.append(cluster_distances)

        while len(self.clusters) != max_clusters:
            # find the min distance between the two close clusters
            min_index_distance_row = 0
            min_index_distance_colmun = 0
            min_value_distance = 9999999999
            for index_list_distance_all_cluster1, cluster_distances1 in enumerate(list_distance_all_cluster):
                temp_min = min(cluster_distances1)
                if min_value_distance > temp_min:
                    min_value_distance = temp_min
                    min_index_distance_colmun = cluster_distances1.index(temp_min)
                    min_index_distance_row = index_list_distance_all_cluster1

            # put the min id cluster index in "min_index_distance_row":
            if min_index_distance_colmun < min_index_distance_row:
                temp = min_index_distance_colmun
                min_index_distance_colmun = min_index_distance_row
                min_index_distance_row = temp

            # merge between the clusters and delete the unnecessery cluster:
            self.clusters[min_index_distance_row].merge(self.clusters[min_index_distance_colmun])
            self.clusters.pop(min_index_distance_colmun)

            # update the new distances between each cluster:
            if self.link.type() == "single link":
                for index_colmun, colmun in enumerate(list_distance_all_cluster[min_index_distance_row]):
                    if index_colmun != min_index_distance_row and index_colmun != min_index_distance_colmun:
                        temp_min = list_distance_all_cluster[min_index_distance_colmun][index_colmun]
                        if colmun > temp_min:
                            list_distance_all_cluster[min_index_distance_row][index_colmun] = temp_min
                            list_distance_all_cluster[index_colmun][min_index_distance_row] = temp_min
            else:
                for index_colmun, colmun in enumerate(list_distance_all_cluster[min_index_distance_row]):
                    if index_colmun != min_index_distance_row and index_colmun != min_index_distance_colmun:
                        temp_max = list_distance_all_cluster[min_index_distance_colmun][index_colmun]
                        if colmun < temp_max:
                            list_distance_all_cluster[min_index_distance_row][index_colmun] = temp_max
                            list_distance_all_cluster[index_colmun][min_index_distance_row] = temp_max

            # remove the distances of the unnecessery cluster:
            list_distance_all_cluster.pop(min_index_distance_colmun)
            for row in list_distance_all_cluster:
                row.pop(min_index_distance_colmun)

        # print the results:
        self.link.print_type_link()
        silhouette_clusters = self.compute_summery_silhoeutte()
        for cluster in self.clusters:
            cluster.print_details(silhouette_clusters[cluster.c_id])
        print("whole data: silhouette = ", end="")
        print("{0:.3f}".format(self.compute_summery_silhoeutte_all_cluster()), end=", IR = ")
        print("{0:.3f}".format(self.compute_rand_index()))
