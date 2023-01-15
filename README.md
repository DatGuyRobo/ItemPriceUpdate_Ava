# ItemPriceUpdate_Ava
Just a Python Script for Ava, updating prices 


Item Price:

This script is written in Python and uses the requests library to make a GraphQL API request to the Tarkov.dev API. The script prompts the user for a list of item types and validates that the input is a comma-separated list of valid item types. Then it makes a GraphQL query to the API to retrieve data for the specified item types. The data returned by the API is parsed and processed to get the items with the highest prices. The highest prices and other item details are then written to an output file called "output.txt." The script also prints the elapsed time it took to execute the script.

Custom Item List:

Same as above just diffrent format.



How:

To use this script on Windows, you will need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you will need to install the following libraries that the script uses:

json
requests
heapq
tqdm
re
You can install these libraries by running the following command in the command prompt:

pip install json requests heapq tqdm re

After installing the required libraries, you can run the script by opening the command prompt, navigating to the directory where the script is located, and running the command:

python script_name.py

Make sure to replace "script_name.py" with the actual name of the script file.

When the script runs, it will prompt you to enter a comma-separated list of valid item types. Once you have entered the item types, the script will execute and retrieve the items from the API. The script will then write the items with the highest prices to an output file named "output.txt" in the same directory as the script.

valid_item_types = {'ammo', 'ammoBox', 'any', 'armor', 'backpack', 'barter', 'container', 'glasses', 'grenade', 'gun', 'headphones', 'helmet', 'injectors', 'keys', 'markedOnly', 'meds', 'mods', 'noFlea', 'pistolGrip', 'preset', 'provisions', 'rig', 'suppressor', 'wearable'}
