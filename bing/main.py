import os
import urllib.request
import json


def parse_keys(keys: str) -> list[str]:
    result = []
    part = ""
    inside_quotes = False

    for char in keys:
        if char == '"' and not inside_quotes:
            inside_quotes = True
        elif char == '"' and inside_quotes:
            inside_quotes = False
            result.append(part)
            part = ""
        elif char == "." and not inside_quotes:
            if part:
                result.append(part)
                part = ""
        else:
            part += char

    if part:
        result.append(part)

    return result


def json_get(data: dict | list, keys: str):
    result = data
    try:
        for key in parse_keys(keys):
            if key.startswith("[") and key.endswith("]"):
                key = int(key[1:-1])
            result = result[key]
        return result
    except:
        raise KeyError from None


def main():
    url = "https://www.bing.com/hp/api/model"
    headers = {
        "User-Agent": os.environ.get("USER_AGENT"),
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)

    # with urllib.request.urlopen(req) as res:
    with open("a.json") as res:
        data = json.load(res)
        keypath = "MediaContents"
        print(json_get(data, keypath))


if __name__ == "__main__":
    main()
