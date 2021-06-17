class Cluster:

    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        """
                merge two cluster together, updating self
                param other: the cluster to be merged with
                return: None
                """
        if self.c_id > other.c_id:
            self.c_id = other.c_id
        for sample in other.samples:
            self.samples.append(sample)

        # sort samples:
        list_s_id = []
        for sample in self.samples:
            list_s_id.append(sample.s_id)

        list_s_id.sort()

        new_list_samples = []
        for s_id_value in list_s_id:
            for sample in self.samples:
                if s_id_value == sample.s_id:
                    new_list_samples.append(sample)
                    break
        self.samples = new_list_samples
        del other

    def print_details(self, silhouette):
        """
        The function of the method is to print the cluster data) from the point identifiers it contains in ascending
        order, label dominant,And silhouette index)
        param silhouette: The silhouette of the cluster
        return: none
        """
        # print cluster id
        print("Cluster ", end="")
        print(self.c_id, end=": ")
        # print list of id samples
        list_s_id = []
        for sample in self.samples:
            list_s_id.append(sample.s_id)
        list_s_id.sort()
        # find and print dominant label
        print(list_s_id, end=", dominant label = ")
        dic_label = {}
        for sample in self.samples:
            dic_label[sample.label] = 0
        for sample in self.samples:
            dic_label[sample.label] += 1
        find_max = 0
        for key in dic_label.keys():
            if dic_label[key] > find_max:
                find_max = dic_label[key]
        list_max_label = []
        for key in dic_label.keys():
            if dic_label[key] == find_max:
                list_max_label.append(key)
        list_max_label.sort()
        # print silhouette
        print(list_max_label[0], end=", silhouette = ")
        print("{0:.3f}".format(silhouette))
