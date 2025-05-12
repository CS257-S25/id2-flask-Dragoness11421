from ProductionCode.processor import (
    display_results,
    filter_by_shape,
    get_sightings_by_shape
)
import cl
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_screen()
    print("type in shape:/<the shape of the ufos you want to look up> to look up those ufos")


@app.route('shape:/<shape>')
def display_ufo_of_shape()
  results = get_sightings_by_shape(shape)
  return display_results(results)






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
