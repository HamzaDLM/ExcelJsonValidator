import pandas as pd
import os
import json


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def create_config_file(nodes, filename):
    path = os.path.join(__location__, filename)

    df = pd.read_excel(path, sheet_name="Sheet1", header=None)
    df = df.astype(str)

    headers_list = list(df.values)
    store = {}
    store["nodes"] = nodes

    for i in range(nodes):
        nm = str(i)
        store[nm] = headers_list[i].tolist()

    path_json = os.path.join(__location__, "config.json")

    with open(path_json, 'w') as fp:
        json.dump(store, fp, indent=4, sort_keys=True)


def compare_config_excel(json_file, excel_file):
    # Read json file----------------------------
    path_json = os.path.join(__location__, json_file)

    with open(path_json, 'r') as f:
        data = json.load(f)
    
    print(data)

    # Read excel file----------------------------
    path = os.path.join(__location__, excel_file)

    df = pd.read_excel(path, sheet_name="Sheet1", header=None)
    df = df.astype(str)

    headers_list = list(df.values)
    store = {}

    for i in range(data["nodes"]):
        nm = str(i)
        store[nm] = headers_list[i].tolist()
    
    print(store)

    # Compare ----------------------------

    del data['nodes']

    if store == data:
        print("MATCHING !")
    else:
        print("NOT MATCHING !")


create_config_file(nodes=3, filename="template.xlsx")

compare_config_excel(json_file="config.json", excel_file="template.xlsx")