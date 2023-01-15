import json
import requests
import heapq
from tqdm import tqdm
import time

# Valid item types that are allowed in the input 
valid_item_types = {'ammo', 'ammoBox', 'any', 'armor', 'backpack', 'barter', 'container', 'glasses', 'grenade', 'gun', 'headphones', 'helmet', 'injectors', 'keys', 'markedOnly', 'meds', 'mods', 'noFlea', 'pistolGrip', 'preset', 'provisions', 'rig', 'suppressor', 'wearable'}

# Get user input for item types 
item_types = input("Which item types do you want to retrieve (comma-separated list)?: ")

# Ensure that the input is a comma-separated list of strings and are valid
if not all(map(lambda x: x in valid_item_types, item_types.split(","))):
    print("Invalid item types specified. valid item types :",valid_item_types)
else:
    # Make the GraphQL API request
    query = f"""
    query GetItems {{
      Items: items(types: [{item_types}]) {{
        id
        name
        avg24hPrice
        sellFor{{
            price
            source
        }}
      }}
    }}
    """
    headers = {
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "query": query
    })
    try:
        # Send request and get response
        response = requests.request("POST", "https://api.tarkov.dev/graphql", data=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else",err)
    else:
        # Get the items with highest_price
        output_list = heapq.nlargest(len(data['data']['Items']), ({"id": item['id'], "highest_price": max([i['price'] for i in item['sellFor']] + [item['avg24hPrice']])} for item in data['data']['Items']), key=lambda x: x["highest_price"])
        t0 = time.time()
        with open("output.txt", "w") as out:
            #iterate over the output_list and write the values to output file
            for item in tqdm(output_list):
                out.write(f'set_price {item["id"]} {item["highest_price"]}\n')
        print(f'elapsed time : {time.time() - t0:.4f} sec')
