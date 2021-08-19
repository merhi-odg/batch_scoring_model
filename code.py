# modelop.slot.0: in-use
# modleop.slot.1: in-use

import logging
import pandas

logger = logging.getLogger(__name__)


# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    
    # data provided as an array of dictionaries, such as 
    # [{"a":1, "b":2}, {"a":3, "b":4}]
    data = pandas.DataFrame(data)
    
    logger.info("BEFORE SUM: data is a dataframe of shape %s", str(data.shape))
    
    data["rown_sum"]=data["a"]+data["b"]
    
    logger.info("AFTER SUM: data is a dataframe of shape %s", str(data.shape))
    
    yield data.to_dict(orient="records")
