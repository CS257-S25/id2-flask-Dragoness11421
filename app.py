'''
Flask app for individual deliverable two that returns ufos of a certain shape on command
'''
from ProductionCode.processor import (
    display_results,
    get_sightings_by_shape
)
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home_screen():
    """The homescreen of the application. Tells the user viable """
    return("type in shape/<the shape of the ufos you want to look up> to look up those ufos")
@app.route('/shape/<shape>')
def display_ufo_of_shape(shape):
  """Returns a ufo of a specified shape"""
  results = get_sightings_by_shape(shape)
  return display_results(results)
if __name__ == '__main__':
  app.run()
