import json

with open('configs/public-config.json') as config:
    public = json.load(config)

with open('configs/private-config.json') as config:
    private = json.load(config)