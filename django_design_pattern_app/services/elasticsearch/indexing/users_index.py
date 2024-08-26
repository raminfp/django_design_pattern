from typing import Type
from pydantic import BaseModel
from django_design_pattern_app.schemas.users import LogIndexModel


class UserIndexConfig:
    es_index_name = "users_index"
    pydantic_model: Type[BaseModel] = LogIndexModel
    es_index_mapping = {
        "properties": {
            "user": {
                "properties": {
                    "id": {"type": "integer"},
                    "username": {"type": "text"},
                    "city": {"type": "keyword"},
                    "state": {"type": "keyword"},
                    "agency_id": {"type": "integer"},
                    "agency_name": {"type": "text"}
                }
            },
            "node_id": {"type": "integer"},
            "operation_time": {"type": "text"},
            "operation_time_date": {"type": "date"},
            "created_at": {"type": "date"},
            "node_route": {"type": "keyword"},
            "events_list": {
                "type": "nested",
                "properties": {
                    "timestamp": {"type": "date"},
                    "event_name": {"type": "keyword"},
                    "properties": {"type": "text"}
                }
            },
        }
    }
    es_settings = {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
