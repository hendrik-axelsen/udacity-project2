import logging

import azure.functions as func
import pymongo
from bson.errors import InvalidId
from bson.json_util import dumps
from bson.objectid import ObjectId
from config import url


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        id = req.params["id"]
        advertisement = req.get_json()
        if not all(
            key in {"title", "city", "description", "email", "imgUrl", "price"}
            for key in advertisement.keys()
        ):
            raise ValueError
        collection = pymongo.MongoClient(url)[  # type: ignore
            "hendrikscosmosdbdatabase"
        ]["advertisements"]
        filter_query = {"_id": ObjectId(id)}
        update_query = {"$set": advertisement}
        collection.update_one(filter_query, update_query)  # type: ignore
        return func.HttpResponse(status_code=201)
    except (KeyError, InvalidId, TypeError, ValueError, AttributeError):
        return func.HttpResponse(
            "Please pass id in query string and advertisement in body", status_code=400
        )
    except Exception as err:
        logging.warn(err)
        return func.HttpResponse("Could not connect to mongodb", status_code=500)
