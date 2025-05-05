"""Helper functions for loading and filtering UFO sightings data."""

def display_results(results):
    """Display search results."""
    if not results:
        print("No sightings found matching your query, please try again with different parameters.")
        return    
    for row in results:
        print(row)


def filter_by_shape(data, shape):
    """filter data to match the given shape."""
    results = []
    shape = shape.strip().lower()
    for row in data:
        row_shape = row['shape'].strip().lower()
        if row_shape == shape:
            results.append(row)
    return results

def get_sightings_by_shape(shape):
    """Get sightings by given shape."""
    data = [
            {'datetime': '10/10/1949 20:30', 'city': 'san marcos', 'shape': 'cylinder'},
            {'datetime': '10/10/1949 21:00', 'city': 'lackland afb', 'shape': 'light'},
            {'datetime': '10/10/1956 21:00', 'city': 'edna', 'shape': 'cylinder'}
        ]
    return filter_by_shape(data, shape)
