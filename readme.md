# FlightAware track log downloader

Just a little utility that downloads the track log files for a given aircraft (or commercial flight) from FlightAware and merges them into a single KML file that you can import into Google My Maps or Google Earth or the tool of your choice.

## Usage

```
$ export FLIGHTAWARE_USERNAME='...@example.com'
$ export FLIGHTAWARE_PASSWORD='...'
$ python -m flightaware_history N744ST
240 flights found
Fetching flight track logs... 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200 205 210 215 220 225 230 235 240 
240 flight tracks written to N744ST.kml
```