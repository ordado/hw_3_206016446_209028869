import sample
import cluster


class Link:

    def compute(self, cluster1, other):
        pass

    def print_type_link(self):
        pass

    def type(self):
        pass


class SingleLink(Link):
    def compute(self, cluster1, other):
        min_distance = []
        for sample1 in cluster1.samples:
            for sample2 in other.samples:
                min_distance.append(sample1.compute_euclidean_distance(sample2))
        return min(min_distance)

    def print_type_link(self):
        print("single link:")

    def type(self):
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster1, other):
        max_distance = []
        for sample1 in cluster1.samples:
            for sample2 in other.samples:
                max_distance.append(sample1.compute_euclidean_distance(sample2))
        return max(max_distance)

    def print_type_link(self):
        print("complete link:")

    def type(self):
        return "complete link"