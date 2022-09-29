# modelop.slot.0: in-use
# modelop.slot.1: in-use

import logging
import pandas
from typing import List, Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")

# modelop.init
def begin():
    
    # Unpickle any binaries if you have any in the scoe of the init function
    # This is also a good place to declare any global variables
    pass


# modelop.score
def action(data):
    
    # MOC can accomodate different formats/types of input data.
    
    if isinstance(data, List):
        # Data is provided as an array of dictionaries, such as [{"a":1, "b":2}, {"a":3, "b":4}]
        # All records will be processed at-once
        data = pandas.DataFrame(data)

    elif isinstance(data, Dict):
        # Data is provided as a dictionary, such as {"a":1, "b":2}. The input data could consist of one-line JSON records such as
        """
        {"a":1, "b":2}
        {"a":3, "b":4}
        """
        # The scoring function will run once for every record/line (processing one record at-a-time)
        data = pandas.DataFrame([data])
        
    else:
        logger.error(
            "Input data must be either a record(dictionary) or an array of records!"
        )
        
    logger.info("BEFORE SUM: data is a dataframe of shape %s", str(data.shape))
    
    # Add a sum column for all rows at-once
    data["rown_sum"] = data["a"] + data["b"]
    
    logger.info("AFTER SUM: data is a dataframe of shape %s", str(data.shape))
    
    # return one JSON-serializable object, such as a dict, or an array of dicts, etc.
    yield data.to_dict(orient="records")
    
