import urllib.request
import json
import ssl
import time

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNjhiMmQwODJhZTQ0NzYzOTJmZGNjNDY2OTgwOThjMiIsImlhdCI6MTc4MjY3MzM4OCwiZXhwIjoyMDk4MDMzMzg4fQ.tpfps7BgZyoKiaKF9AqRdoRVEODkR9LhLCeCF1ElAlM"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

entities = [
    "binary_sensor.front_door_sensor",
    "automation.door_opens_lights_on_then_off",
    "switch.hallwaylight_sonoffhallwaylight",
    "switch.sonoff_sonoffhallwaymiddle"
]

def get_states():
    states = {}
    for ent in entities:
        url = f"https://192.168.1.41:8123/api/states/{ent}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                data = json.loads(response.read().decode('utf-8'))
                state = data.get("state")
                last_triggered = data.get("attributes", {}).get("last_triggered")
                states[ent] = (state, last_triggered)
        except Exception as e:
            states[ent] = (f"Error: {e}", None)
    return states

print("Monitoring states for 15 seconds...")
start_time = time.time()
last_states = {}
while time.time() - start_time < 15:
    current_states = get_states()
    if current_states != last_states:
        print(f"Time: {time.strftime('%H:%M:%S')}")
        for ent, (val, trig) in current_states.items():
            prev = last_states.get(ent)
            if prev is None or prev != (val, trig):
                if trig:
                    print(f"  {ent} -> State: {val}, Last Triggered: {trig}")
                else:
                    print(f"  {ent} -> State: {val}")
        last_states = current_states
    time.sleep(2.0)
print("Monitoring finished.")
