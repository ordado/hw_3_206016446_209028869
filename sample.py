class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        """
        The role of the method is to calculate euclidean distance between the specimen, and the specimen other
        param: other: Object of class Sample
        return: distance
        """
        sum_of_square_distance = 0
        for index, value in enumerate(other.genes):
            sum_of_square_distance += ((value - self.genes[index]) ** 2)
        return sum_of_square_distance ** 0.5

    def compute_distance_sample_to_cluster(self, sample, cluster):
        """
        The role of the method is to calculate euclidean distance between the specimen and the cluster
        param sample: Object of class Sample
        param cluster: Object of class Cluster
        return:
        """
        sum_distance = 0
        for other_sample in cluster.samples:
            sum_distance += other_sample.compute_euclidean_distance(sample)
        return sum_distance / len(cluster.samples)
