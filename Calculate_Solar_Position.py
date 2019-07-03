def solar_angle(date, latitude, zenith):
    '''
        The zenith  --> is an imaginary point directly "above" a particular location, on the imaginary celestial sphere.
                "Above" means in the vertical direction opposite to the apparent gravitational force at that location
                The zenith is the "highest" point on the celestial sphere.
        The azimuth --> is an angular measurement in a spherical coordinate system. The vector from an observer (origin)
                to a point of interest is projected perpendicularly onto a reference plane; the angle between the projected
                vector and a reference vector on the reference plane is called the azimuth. 
     Input :       
        - date        : TimeStamp np.array
        - latitude    : float representing the latitude of the observer's place
        - longitude   : float representing the longitude of the observer's place
        
    Output : a tuple containing
        - zenith      : float np.array
        - azimuth     : float np.array
    
    Note : The zenith and azimuth are computed using the 'pvlib' module named 'solarposition'.
           For more information, check out here : https://pvlib-python.readthedocs.io/en/stable/api.html#solar-position
    '''
    
    from pvlib import solarposition as spos
    
    if(len(date) > 1):
        dayOfYear = date.map(lambda d: d.dayofyear)

    else:
        dayOfYear = date[0].dayofyear
        
    ###### Ajout solar position ########    
    equationOfTime = spos.equation_of_time_pvcdrom(dayOfYear)
    declination = spos.declination_cooper69(dayOfYear)

    times = pd.DatetimeIndex(date)
    hourAngle = spos.hour_angle(times, longitude, equationOfTime)

    zenith = spos.solar_zenith_analytical(latitude,hourAngle,declination)

    azimuth = spos.solar_azimuth_analytical(latitude, hourAngle, declination, zenith)
    
    return zenith, azimuth
