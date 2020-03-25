import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
nodes = parsedxml.get("osm").get("node")
relations = parsedxml.get("osm").get("relation")
ways = parsedxml.get("osm").get("way")

node_gas_stations = 0

for node in nodes:
    tags = node.get("tag")
    if isinstance(tags, list):
        for tag in tags:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                node_gas_stations += 1
    else:
        tag = node.get("tag")
        if tag:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                node_gas_stations += 1

way_gas_stations = 0

for way in ways:
    tags = way.get("tag")
    if isinstance(tags, list):
        for tag in tags:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                way_gas_stations += 1
    else:
        tag = way.get("tag")
        if tag:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                way_gas_stations += 1

relation_gas_stations = 0

for relation in relations:
    tags = relation.get("tag")
    if isinstance(tags, list):
        for tag in tags:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                way_gas_stations += 1
    else:
        tag = relation.get("tag")
        if tag:
            if tag.get("@k") == "amenity" and tag.get("@v") == "fuel":
                way_gas_stations += 1

print(f"Gas stations found as nodes: {node_gas_stations}")
print(f"Gas stations found as ways: {way_gas_stations}")
print(f"Gas stations found as relations: {relation_gas_stations}")
