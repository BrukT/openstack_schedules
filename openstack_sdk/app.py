import openstack
import pprint
import json
import time

# Connect
conn = openstack.connect()

# list images
print("Images List:")
images = [image for image in conn.compute.images()]
for image in images:
    pprint.pprint(image)

# list VMs
print("Servers List:")
servers = [server for server in conn.compute.servers()]
for server in servers:
    pprint.pprint(image)

print("Networks List:")
networks = [network for network in conn.network.networks()]
for network in networks:
    pprint.pprint(network)

print("Flavours List:") 
flavors = [flavor for flavor in conn.compute.flavors()]
for flavor in flavors:
    pprint.pprint(flavor) 

SERVER_NAME = 'mr-robot'
IMAGE_NAME = 'cirros'
FLAVOR_NAME = 'm1.tiny'
NETWORK_NAME = 'external'


image = conn.compute.find_image(IMAGE_NAME)
flavor = conn.compute.find_flavor(FLAVOR_NAME)
network = conn.network.find_network(NETWORK_NAME)

server = conn.compute.create_server( name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id, networks=[{"uuid": network.id}])
server = conn.compute.wait_for_server(server)

duration = 15
print("vm work for ", duration)
time.sleep(duration)

conn.compute.delete_server(server)