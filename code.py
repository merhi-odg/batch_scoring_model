# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc
# modelop.recordsets.0: true

import logging
import pandas
import json


logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")

# modelop.init
def begin():

    # Unpickle any binaries if you have any in the scope of the init function
    # This is also a good place to declare any global variables
    pass


# modelop.score
def action(data):

    logger.info("BEFORE SUM: data is a dataframe of shape %s", str(data.shape))

    # Add a sum column for all rows at-once
    data["row_sum"] = data["a"] + data["b"]

    logger.info("AFTER SUM: data is a dataframe of shape %s", str(data.shape))
    
    # For CSV output, iterate through rows of dataframe, and yield dictionaries
    for _, row in data.iterrows():
        yield dict(row)
