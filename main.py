import sys
import data
import link
import agglomerative_clustring


def main(argv):
    main_data = data.Data("Leukemia_sample.csv")
    single_link = link.SingleLink()
    agglomerative_clustring1 = agglomerative_clustring.AgglomerativeClustring(single_link, main_data.create_samples())
    agglomerative_clustring1.run(7)
    main_data2 = data.Data("Leukemia_sample.csv")
    complete_link = link.CompleteLink()
    print("")
    agglomerative_clustring2 = agglomerative_clustring.AgglomerativeClustring(complete_link,
                                                                              main_data2.create_samples())
    agglomerative_clustring2.run(7)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main(sys.argv)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
