# modelop.slot.0: in-use
# modleop.slot.1: in-use

import logging
import pandas
from typing import List, Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")

# modelop.init
def begin():
    pass


# modelop.score
def action(data):

    if isinstance(data, List):
        # data provided as an array of dictionaries, such as [{"a":1, "b":2}, {"a":3, "b":4}]
        data = pandas.DataFrame(data)

    elif isinstance(data, Dict):
        # Data is provided as a dictionary, such as {"a":1, "b":2}
        data = pandas.DataFrame([data])

    else:
        logger.error(
            "Input data must be either a record(dictionary) or an array of records!"
        )

    logger.info("BEFORE SUM: data is a dataframe of shape %s", str(data.shape))

    # Add a sum column for all rows at-once
    data["rown_sum"] = data["a"] + data["b"]

    logger.info("AFTER SUM: data is a dataframe of shape %s", str(data.shape))

    yield data.to_dict(orient="records")
