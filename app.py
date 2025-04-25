'''Replace me with your flask app'''
from ProductionCode.processor import (
    display_results,
    filter_by_shape,
    get_sightings_by_shape
)
import cl
from flask import Flask
app = Flask(__name__)

@app.route('shape:/<shape>')
  results = get_sightings_by_shape(shape)
  return display_results(results)






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
