#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# anonymize palo alto log .
# IPなどをハッシュ化により匿名化する.
# [CSV format](https://docs.paloaltonetworks.com/pan-os/7-1/pan-os-admin/monitoring/syslog-field-descriptions.html)

import hashlib
import csv


# 'Traffic Log Fields', 'Threat Log Fields' に共通する項目.
# test_target_keys_b = ["Source IP", "Destination IP", "Source User", "Destination User"]
# test_target_keys = ['source_ip', 'destination_ip', 'source_user', 'destination_user']
INDEX_TYPE = 3
TRAFFIC = "TRAFFIC"
INDEX_SRC_IP = 7
INDEX_DST_IP = 8
INDEX_SRC_USER = 12
INDEX_DST_USER = 13
TARGET_INDEXES = [INDEX_SRC_IP, INDEX_DST_IP, INDEX_SRC_USER, INDEX_DST_USER]


def anonymize_traffic_log(logs):
    if logs[INDEX_TYPE] != TRAFFIC:
        print("[Error] Not TRAFFIC log.")
        return None
    for index in TARGET_INDEXES:
        if logs[index]:
            # print("[encode before]", logs[_index])
            logs[index] = hashlib.sha256(logs[index].encode('utf-8')).hexdigest()
            # print("[encode after]", logs[_index])

    return logs


def anonymize(target_csv_file, output_file):
    with open(target_csv_file, 'r') as csv_f:
        with open(output_file, 'w') as out_f:
            reader = csv.reader(csv_f)
            writer = csv.writer(out_f)

            for fields_str in reader:
                # print(fields_str)
                fields = anonymize_traffic_log(fields_str)
                writer.writerow(fields)


if __name__ == '__main__':
    csv_file = "paloaltologs/log.csv"
    out_file = "paloaltologs/log_out.csv"

    anonymize(csv_file, out_file)
