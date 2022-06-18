import azure.functions as func
import pymongo
from config import url


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        advertisement = req.get_json()
        if not all(
            key in {"title", "city", "description", "email", "imgUrl", "price"}
            for key in advertisement.keys()
        ):
            raise ValueError
        collection = pymongo.MongoClient(url)[  # type: ignore
            "hendrikscosmosdbdatabase"
        ]["advertisements"]
        _ = collection.insert_one(advertisement)  # type: ignore
        return func.HttpResponse(status_code=201)
    except (ValueError, AttributeError):
        return func.HttpResponse(
            "Please pass advertisement in the body", status_code=400
        )
    except Exception:
        return func.HttpResponse("Could not connect to mongodb", status_code=500)
