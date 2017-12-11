from multiprocessing import Pool
from collections import Counter
import glob


def createhistogram(file):

    histogram = Counter()
    with open(file) as f:
        for x in f:
            histogram[x.strip()] += 1
    return histogram


def main():

    file = glob.glob("colors*.txt")

    pool = Pool(processes=3)
    histograms = pool.map(createhistogram, file)

    pool.close()
    pool.join()

    merged_hist = histograms[0]
    for h in histograms[1:]:
        merged_hist.update(h)

    for word, count in merged_hist.items():
        print("%s:  %s" % (word, count))


if __name__ == "__main__":
    main()
