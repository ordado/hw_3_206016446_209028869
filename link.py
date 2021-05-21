import sample
import cluster


class Link:

    def compute(self, cluster1, other):
        pass

    def print_type_link(self):
        pass


class SingleLink(Link):
    def compute(self, cluster2, other):
        min_distance = cluster2.samples[0].compute_euclidean_distance(other.samples[0])
        for sample1 in cluster2.samples:
            for sample2 in other.samples:
                temp_distance = sample1.compute_euclidean_distance(sample2)
                if min_distance > temp_distance:
                    min_distance = temp_distance
        return min_distance

    def print_type_link(self):
        print("single link:")


class CompleteLink(Link):
    def compute(self, cluster3, other):
        list_max_distance = []
        for sample1 in cluster3.samples:
            max_distance = cluster3.samples[0].compute_euclidean_distance(other.sample[0])
            for sample2 in other.sample:
                temp_distance = sample1.compute_euclidean_distance(sample2)
                if max_distance > temp_distance:
                    max_distance = temp_distance
                list_max_distance.append(max_distance)
        list_max_distance.sort()
        return list_max_distance[0]

    def print_type_link(self):
        print("complete link:")
