#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygeoip
gi = pygeoip.GeoIP('/Users/luis.urbina/Desktop/GeoIP/Geo.dat')


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[+] '+str(city)+', '+str(region)+', '+str(country)
    print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)


tgt = '73.181.113.194'
printRecord(tgt)
