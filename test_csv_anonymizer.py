#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import csv
import unittest
from csv_anonymizer import anonymize
from csv_anonymizer import target_keys


class TestCsvAnonymizer(unittest.TestCase):
    
    # def __init__(self):
        # self.test_csv_file = "paloaltologs/test_log.csv"  #TrafficLogFieldsSample
        # self.test_out_file = "paloaltologs/test_out.csv"

    def test_anonymize(self):
        # TODO:ファイル名の定義場所を検討.
        # test_csv_file = self.test_csv_file
        # test_out_file = self.test_out_file
        test_csv_file = "paloaltologs/test_log.csv"  #TrafficLogFieldsSample
        test_out_file = "paloaltologs/test_log_out.csv"

        anonymize(test_csv_file, test_out_file ,target_keys)
        csv_f = open(test_csv_file)
        csv_dicts = csv.DictReader(csv_f)
        out_f = open(test_out_file)
        out_dicts = csv.DictReader(out_f)

        for target_key in target_keys:
            for csv_dict, out_dict in zip(csv_dicts, out_dicts):
                if csv_dict.get(target_key):
                    csv_value = csv_dict.get(target_key)
                    out_value = out_dict.get(target_key)
                    self.assertNotEqual(csv_value, out_value)
        
        csv_f.close()
        out_f.close()

if __name__ == '__main__':
    unittest.main()

