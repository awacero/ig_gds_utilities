from ig_gds_utilities import ig_utilities as u
from datetime import datetime


expected_location = (45.4678, 9.1912)
expected_location_result = "a 0.14 km de Milan, Lombardy"

original_url = "http://eventos.igepn.edu.ec/eqevents/event/igepn2018jgsc/overview.html"
expected_short_url = "https://bit.ly/2rLlW6L"

def test_short_url():
    
    test_url = u.short_url(original_url)
    print(test_url)
    assert test_url == expected_short_url, "ERROR in test_short_url()"


def test_get_closest_city():
    
    test_location_result = u.get_closest_city(expected_location[0],expected_location[1])
    assert test_location_result == expected_location_result, "ERROR in test_get_closest_city()"


event_datetime = datetime.strptime("2016-04-16T23:58:00","%Y-%m-%dT%H:%M:%S")
event_id = "igepn2016hnmu"
expected_google_url = "https://bit.ly/3tdrfdF"
expected_arcgis_url = "https://bit.ly/3mTk9tD"

def test_get_survey_url():
    test_survey_url = u.get_survey_url(event_datetime,event_id)

    #if cfg.survey_type == "arcgis":
    try:
        assert expected_arcgis_url == test_survey_url, "ERROR in test_get_survey_url, arcgis"
    except :
        assert expected_google_url == test_survey_url, "ERROR in test_get_survey_url, google"


test_lat,test_lon = 4.611535, -74.074598 #Bogota
expected_message = """\nFuente oficial COLOMBIA: \nhttps://www.sgc.gov.co/sismos \nhttps://twitter.com/sgcol"""

def test_get_message_by_country():
    
    test_message = u.get_message_by_country(test_lat,test_lon)
    assert test_message == expected_message

test_lat,test_lon = 4.611535, -74.074598 #Bogota
expected_message_twitter = """\nFuente oficial COLOMBIA: https://www.sgc.gov.co/sismos"""

def test_get_message_by_country_twitter():
    
    test_message = u.get_message_by_country_twitter(test_lat,test_lon)
    assert test_message == expected_message_twitter



    

test_short_url()
test_get_closest_city()
"""

test_get_message_by_country()
test_get_survey_url()
""" 

