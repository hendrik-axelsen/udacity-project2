import azure.functions as func
import pymongo
from bson.json_util import dumps
from config import url


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        collection = pymongo.MongoClient(url)[  # type: ignore
            "hendrikscosmosdbdatabase"
        ]["posts"]
        query = {}
        result = collection.find(query)  # type: ignore
        result = dumps(result)
        return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
    except Exception:
        return func.HttpResponse("Could not connect to mongodb", status_code=500)
