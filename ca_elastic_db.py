import json
from typing import List

import ca_config
from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

es = Elasticsearch(ca_config.elastic_hosts)
es.indices.create(index=ca_config.elastic_index_elements, ignore=400)
ses = SignatureES(es, index=ca_config.elastic_index_elements)


def add_image(img_id: str, img_meta: dict, img_bytes: bytes) -> None:
    delete_image(img_id)
    ses.add_image(path=img_id, img=img_bytes, bytestream=True, metadata=img_meta)


def search_image(img_bytes: bytes) -> List:
    # noinspection PyTypeChecker --> Seems to be just wrong
    return ses.search_image(img_bytes, all_orientations=True, bytestream=True)


def find_ids_by_img_id(path):
    matches = es.search(index=ca_config.elastic_index_elements,
                        _source='_id',
                        q='path:' + json.dumps(path))
    return [m['_id'] for m in matches['hits']['hits']]


def delete_image(img_id: str) -> None:
    es_ids = find_ids_by_img_id(img_id)
    for es_id in es_ids:
        es.delete(index=ca_config.elastic_index_elements, id=es_id, ignore=404)
