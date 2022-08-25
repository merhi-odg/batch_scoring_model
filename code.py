# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc
# modelop.recordsets.0: true
# modelop.recordsets.1: true

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
        
    logger.info("BEFORE SUM: data is a dataframe of shape %s", str(data.shape))
    
    # Add a sum column for all rows at-once
    data["rown_sum"] = data["a"] + data["b"]
    
    logger.info("AFTER SUM: data is a dataframe of shape %s", str(data.shape))
    
    # Yield one JSON-serializable object, such as a dict, or an array of dicts, etc.
    yield data
    
