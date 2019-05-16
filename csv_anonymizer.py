#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# palo alto log anonymization.
# IPなどをハッシュ化により匿名化する.
# [CSV format](https://docs.paloaltonetworks.com/pan-os/7-1/pan-os-admin/monitoring/syslog-field-descriptions.html)
import hashlib
import csv


# 'Traffic Log Fields', 'Threat Log Fields' に共通する項目.
# test_target_keys_b = ["Source IP", "Destination IP", "Source User", "Destination User"]
# test_target_keys = ['source_ip', 'destination_ip', 'source_user', 'destination_user']
target_keys = ["src", "dst", "srcuser", "dstuser"]


def anonymize(csv_file, output_file, hash_targets):
    is_first = True
    
    with open(output_file, 'w') as out_f:
        with open(csv_file) as csv_f:
            dict_reader = csv.DictReader(csv_f)
            if is_first:
                # print(dict_reader.fieldnames)
                csv_fields = dict_reader.fieldnames
                writer = csv.DictWriter(out_f, csv_fields)
                writer.writeheader()
            
            for csv_dict in dict_reader:
                # TODO: 内包表記でネスト浅くできる気がする.
                for target in hash_targets:
                    if csv_dict.get(target):
                        # print(csv_dict.get(target))
                        csv_dict[target] = hashlib.sha256(csv_dict[target].encode('utf-8')).hexdigest()
                writer.writerow(csv_dict)

if __name__ == '__main__':
    csv_file = "paloaltologs/test_log.csv"
    out_file = "paloaltologs/test_log_out.csv"

    anonymize(csv_file, out_file, target_keys)
