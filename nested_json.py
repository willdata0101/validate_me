nested_response = {
    "movie": {
        "title": "The Wizard of Oz",
        "year": 1939
    }
}

nested_response_2 = {
  "movies": [
    { "title": "A", "year": 2000 },
    { "title": "B", "year": "2001" }
  ]
}

json_path = "movies[0].year".split(".")

def get_json_value(path, response):
    found = True
    current = response
    for e in path:
        if "[" in e and "]" in e:
            parts = e.split("[")
            key = parts[0]
            index = int(parts[1].strip("]"))
            if not isinstance(current, dict) or key not in current:
                found = False
                break
            current = current[key]
            if not isinstance(current, list) or index < 0 or index >= len(current):
                found = False
                break
            current = current[index]
        elif isinstance(current, dict) and e in current:
            current = current[e]
        else:
            found = False
            break
            
    if found:
        return True, current
    
    return False, None
            
found, value = get_json_value(json_path, nested_response)
