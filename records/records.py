#!/usr/bin/env python

"""
Record class that gets records from GBIF.
"""

import requests
import pandas as pd


class Records:
    def __init__(self, genusKey=None, year=None, genusName=None):
        """
        Parameters
        ----------
        genusKey (int, optional):
            Genus key number. Defaults to None.
        year (str, optional):
            Year range separated by a comma. Defaults to None.
        """
        # store input params
        self.genusName = genusName
        self.genusKey = genusKey
        self.year = year

        # will be used to store output results
        self.df = None
        self.json = None

    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        p = {
                "year": self.year,
                "offset": offset,
                "limit": limit,
                "hasCoordinate": "true",
                "country": "US",
            }
        if self.genusKey:
            p["genusKey"] = self.genusKey
        elif self.genusName:
            p["q"] = self.genusName
            p["rank"] = "GENUS"
        res = requests.get(
            url="https://api.gbif.org/v1/occurrence/search/",
            params=p
        )
        return res.json()

    def get_all_records(self):
        "stores result for all records to self.json and self.df"
        # for storing results
        alldata = []

        # continue until we call 'break'
        offset = 0
        while 1:

            # get JSON data for a batch
            jdata = self.get_single_batch(offset=offset, limit=300)

            # increment counter by 300 (the max limit)
            offset += 300

            # add this batch of data to the growing list
            alldata.extend(jdata["results"])
            # stop when end of record is reached
            if jdata["endOfRecords"]:
                print(f'Done. Found {len(alldata)} records')
                break

            # print a dot on each rep to show progress
            print('.', end='')
        self.json = alldata
        self.df = pd.json_normalize(alldata)
