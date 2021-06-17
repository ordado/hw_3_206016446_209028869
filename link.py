class Link:
    """
    Interface for calculating distances between two clusters according to the two approaches: complete and single link
    """

    def compute(self, cluster1, other):
        """
        Compute the distance between the two clusters
        param: cluster1: Cluster
        param other: Cluster
        return: the Compute the distance between the two clusters

        """
        pass

    def print_type_link(self):
        """
        print the type link
        return: none
        """
        pass

    def type(self):
        """
        return: type link
        """
        pass


class SingleLink(Link):
    def compute(self, cluster1, other):
        """
                Compute the distance between the two clusters in single link method
                param: cluster1: Cluster
                param other: Cluster
                return: the Compute the distance between the two clusters

                """
        min_distance = []
        for sample1 in cluster1.samples:
            for sample2 in other.samples:
                min_distance.append(sample1.compute_euclidean_distance(sample2))
        return min(min_distance)

    def print_type_link(self):
        """
               print the type link
               return: none
               """
        print("single link:")

    def type(self):
        """
                return: the type of the link
                """
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster1, other):
        """
                Compute the distance between the two clusters in complete link method
                param: cluster1: Cluster
                param other: Cluster
                return: the Compute the distance between the two clusters

                """
        max_distance = []
        for sample1 in cluster1.samples:
            for sample2 in other.samples:
                max_distance.append(sample1.compute_euclidean_distance(sample2))
        return max(max_distance)

    def print_type_link(self):
        """
               print the type link
               return: none
               """
        print("complete link:")

    def type(self):
        """
                        return: the type of the link
                        """
        return "complete link"
