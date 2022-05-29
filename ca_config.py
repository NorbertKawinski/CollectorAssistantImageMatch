
# elastic_host = "kawinski.net"
# elastic_host = "37.187.127.40"
elastic_host = "elasticsearch"
elastic_port = 9200
# It must be a tuple! (I guess array would work too?)
elastic_hosts = ({"host": elastic_host, "port": elastic_port},)

elastic_index_elements = "elements"  # Could use collection/user/etc in the future

server_debug = False
server_host = "0.0.0.0"
server_port = 5000
