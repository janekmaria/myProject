# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
# pylint: disable=missing-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    """
    Look for a given city and disambiguate between several candidates. Return one city (or None)
    """

    response = requests.get(f'{BASE_URI}/api/location/search/?query={query}').json()

    # import ipdb; ipdb.set_trace()
    if not response:
        return None

    return response[0]

def weather_forecast(woeid):
    """
    Return a 5-element list of weather forecast for a given woeid
    """

    woeid = woeid['woeid']
    response = requests.get(f'{BASE_URI}/api/location/{woeid}/').json()
    consolidated_weather = response['consolidated_weather']

    forecast = []
    for ind in range(5):
        forecast.append(f"{consolidated_weather[ind]['applicable_date']}: {consolidated_weather[ind]['weather_state_name']} {round(float(consolidated_weather[ind]['max_temp']), 1)}°C")
    return forecast

def main():
    query = input("City?\n> ")

    print(f'Here is the weather in {query}')
    city = search_city(query)

    if not city:
        return None

    forecast = weather_forecast(city)

    for day in forecast:
        print(day)

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
