import seiscomp3.Logging as logging
import requests
import config_utilities as cfg


def short_url(long_url):

    endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    key = cfg.bitly_key
    group_id = cfg.bitly_group_id

    header = {  "Authorization": "%s" %key,
                "Content-Type" : "application/json",
            }
    #params = { "long_url" : long_url, "domain": "bit.ly", "group_guid": group_id } 
    params = { "long_url" : long_url} 

    try:
        response = requests.post(endpoint, headers=header,json=params)
        data = response.json()

        if not response.ok:
            logging.error("Error in utilities.short_url: %s %s" %(response, data))
        return data['link']

    except Exception as e:
        print("Error in short_url: error: %s response:%s data:%s" %(str(e),response,data))
        return "---"


def get_closest_city(latitude,longitude):
    try:
        query = '%s/get_nearest_city?lat=%s&lon=%s&token=%s'%(cfg.geolocation_service_url,latitude,longitude,cfg.geolocation_service_token)
        result = requests.get(query)
        #distance,city,province = result.text.strip('()').encode('utf-8',errors='ignore').split(',')
        distance,city,province = result.text.strip('()').split(',')
        return 'a %s km de %s, %s' %(distance,city.strip(" '"),province.strip(" '"))
    except Exception as e:
        msg_error = "##Error in get_closest_city:%s %s " %(str(e),result.text)
        print(msg_error)
        logging.error(msg_error)
        return '--'

def get_survey_url(local_time,event_id):
    
    date_event = local_time.strftime("%Y-%m-%d")
    time_event = local_time.strftime("%H:%M:%S")
    if cfg.survey_type == "arcgis":
        return short_url(cfg.arcgis_survey_url %(event_id,date_event,time_event))
    else:
        return short_url(cfg.google_survey_url %(event_id, date_event, time_event))

def get_message_by_country(latitud,longitud):
    try:
        query = '%s/get_country?lat=%s&lon=%s&token=%s'%(cfg.geolocation_service_url,latitud,longitud,cfg.geolocation_service_token)
        result = requests.get(query)
        country = result.text
        country_text = "Ecuador"

        if country == 'Ecuador':
            return country_text
        elif country == 'Colombia':
            country_text = "\nFuente oficial COLOMBIA: \nhttps://www.sgc.gov.co/sismos \nhttps://twitter.com/sgcol"
        elif country == 'Peru':
            country_text = "\nFuente oficial PERU: \nhttps://www.gob.pe/igp \nhttps://twitter.com/Sismos_Peru_IGP"
        else:
            country_text = "\nOtras fuentes que pueden consultarse:\nhttps://www.emsc-csem.org/#2\nhttps://earthquake.usgs.gov/earthquakes/map/\nhttps://geofon.gfz-potsdam.de/eqinfo/list.php"

        return country_text     

    except Exception as e: 
        msg_error = "##Error in get_country:%s" %str(e)
        print(msg_error)
        logging.error(msg_error)
        return '---'


def get_message_by_country_twitter(latitud,longitud):
    try:
        query = '%s/get_country?lat=%s&lon=%s&token=%s'%(cfg.geolocation_service_url,latitud,longitud,cfg.geolocation_service_token)
        result = requests.get(query)
        country = result.text
        country_text = "Ecuador"

        if country == 'Ecuador':
            return country_text
        elif country == 'Colombia':
            country_text = "\nFuente oficial COLOMBIA: https://www.sgc.gov.co/sismos"
        elif country == 'Peru':
            country_text = "\nFuente oficial PERU: https://www.gob.pe/igp"
        else:
            country_text = "\nFuente internacional:https://earthquake.usgs.gov/earthquakes/map/"

        return country_text  
    
    except Exception as e: 
        msg_error = "##Error in get_country:%s" %str(e)
        print(msg_error)
        logging.error(msg_error)
        return '---'
