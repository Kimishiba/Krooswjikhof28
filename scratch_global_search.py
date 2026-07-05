import os

search_paths = [
    "/Users/alessandro.longoni/Library/CloudStorage",
    "/Users/alessandro.longoni/Documents/Antigravity"
]

target = "front_door_open_alert"

for path in search_paths:
    print(f"Searching in: {path}")
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        continue
    for root, dirs, files in os.walk(path):
        # skip hidden dirs or virtualenvs to speed up
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', 'venv', 'env', '__pycache__')]
        for file in files:
            if file.endswith(('.yaml', '.json', '.py', '.txt', '.md', '.conf')):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if target in content:
                            print(f"FOUND IN: {full_path}")
                except Exception:
                    pass
