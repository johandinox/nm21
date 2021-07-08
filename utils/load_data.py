import numpy as np


class Steinmetz():
    def __init__(self, alldat):
        self.alldat = alldat
        return

    def find_session(self, query_regions):
        """
        param: query_regions is a list of region names strings
        returns: dict keyed by session ids containing recordings from all query region and valued by number of neurons per query region
        """
        hits = {}
        for sess in range(len(self.alldat)):
            num_neurons = {}
            intersections = np.full(shape=self.alldat[sess]['brain_area'].shape, fill_value=True)
            for query_region in query_regions:
                intersections = np.intersect1d(intersections,
                                               self.alldat[sess]['brain_area'] == query_region)
                num_neurons[query_region] = (self.alldat[sess]['brain_area'] == query_region).sum()
            if intersections.sum() > 0:
                hits[sess] = num_neurons
        return hits
