import pandas
import sample


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        """
        The method output is a list of objects of type Sample class
        return: list of objects of type Sample
        """
        new_list = []
        for index, value in enumerate(self.data["samples"]):
            new_sample = sample.Sample(0, [], "")
            for key in self.data.keys():
                if key == "samples":
                    new_sample.s_id = value
                else:
                    if key == "type":
                        new_sample.label = self.data[key][index]
                    else:
                        new_sample.genes.append(self.data[key][index])
            new_list.append(new_sample)
        return new_list
