import sys
import data
import link
import agglomerative_clustring


def main(argv):
    main_data = data.Data("Leukemia_sample.csv")
    single_link = link.SingleLink()
    agglomerative_clustring1 = agglomerative_clustring.AgglomerativeClustring(single_link, main_data.create_samples())
    agglomerative_clustring1.run(7)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
