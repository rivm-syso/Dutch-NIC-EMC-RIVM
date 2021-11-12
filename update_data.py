#!/usr/bin/env python#
import requests 
import itertools
import os

viruses = ['h3n2','h1n1pdm', 'vic', 'yam']
segments = ['na','ha']
year = ['2y']
types = {
    'base': {'suffix': '', 'url-parameter': ''},
    'root-sequence': {'suffix': 'root-sequence', 'url-parameter': 'root-sequence'},
    'tip-frequencies': {'suffix': 'tip-frequencies', 'url-parameter': 'tip-frequencies'},
}


base_url = 'https://nextstrain.org/charon/getDataset?prefix=flu/seasonal'
base_filename = 'auspice/Dutch-NIC-EMC-RIVM'

def build_url(virus, segment, year, file_type):
    parameter = ('&type=' + file_type) if file_type else ''
    return f"{base_url}/{virus}/{segment}/{year}{parameter}"

def build_filename(virus, segment, year, suffix):
    suffix = (f"_{suffix}" if suffix else '')
    return f"{base_filename}_{virus}-{segment}{suffix}.json"

os.makedirs(os.path.dirname(base_filename), exist_ok=True)
for request in itertools.product(viruses, segments, year, types.values()):
    url = build_url(request[0], request[1], request[2], request[3]['url-parameter'])
    filename = build_filename(request[0], request[1], request[2], request[3]['suffix'])
    # print(f"{filename:<50}: {url}")
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

