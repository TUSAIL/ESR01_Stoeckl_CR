def celsius_to_kelvin(celsius):
    """
    Function to return Kelvin degrees from Celsius input
    """
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    """
    Function to return fahrenheit from Celsius input
    
    
    """
    return celsius *9/5 + 32


def mean_temperature(data):
    """
    Get the mean temperature
    
    Arg:
        data(pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return sum(temperatures)/len(temperatures)