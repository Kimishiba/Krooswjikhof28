import json

path_entity = "/Users/alessandro.longoni/Library/CloudStorage/OneDrive-CM.com/CLAUDE PROJECT/antigravity/Home Automation/entity_registry.json"

with open(path_entity, "r") as f:
    ent_reg = json.load(f)

entities = ent_reg.get("data", {}).get("entities", [])
for entry in entities:
    ent_id = entry.get("entity_id")
    if "front_door" in str(ent_id) or "alert" in str(ent_id):
        print(json.dumps(entry, indent=2))
        print("-" * 30)
