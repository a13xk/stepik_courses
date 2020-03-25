import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)

nodes = parsedxml.get("osm").get("node")
nodes_with_tags = 0
nodes_without_tags = 0
for node in nodes:
    if node.get("tag"):
        nodes_with_tags += 1
    else:
        nodes_without_tags += 1
print(f"Nodes with tags: {nodes_with_tags}")
print(f"Nodes without tags: {nodes_without_tags}")
print()
print(nodes_with_tags, nodes_without_tags)
pass