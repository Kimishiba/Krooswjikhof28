import json

with open("/Users/alessandro.longoni/Documents/Antigravity/Home Assistant/ha_states.json", "r") as f:
    data = json.load(f)

search_strings = [
    "9dabbc654a9670e49876c35cdc68aaeb",
    "c2152bcb3e89a6facc609280766eea87"
]

for s in search_strings:
    print(f"Searching for: {s}")
    found = False
    for item in data:
        item_str = json.dumps(item)
        if s in item_str:
            print(f"Found in: {item.get('entity_id')}")
            found = True
    if not found:
        print("Not found in any state entity")
    print("-" * 30)
