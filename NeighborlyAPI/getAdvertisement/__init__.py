import azure.functions as func
import pymongo
from bson.errors import InvalidId
from bson.json_util import dumps
from bson.objectid import ObjectId
from config import url


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        id = req.params["id"]
        collection = pymongo.MongoClient(url)[  # type: ignore
            "hendrikscosmosdbdatabase"
        ]["advertisements"]
        query = {"_id": ObjectId(id)}
        result = collection.find_one(query)  # type: ignore
        if result is None:
            return func.HttpResponse(status_code=404)
        result = dumps(result)
        return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
    except (KeyError, InvalidId, TypeError):
        return func.HttpResponse("Please pass id in query string", status_code=400)
    except Exception:
        return func.HttpResponse("Could not connect to mongodb", status_code=500)
