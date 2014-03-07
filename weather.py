import time
import urllib
import pymetar
from display import Display

display = Display()
display.reset()

def weather():
  station = 'CYZP'

  fetcher = pymetar.ReportFetcher(station)
  report = fetcher.FetchReport()

  parser = pymetar.ReportParser()
  obs = parser.ParseReport(report)

  for x in range(0,10):
    display.write_string(station)
    time.sleep(3)

    display.write_string("%s%02i" % ( obs.getWindCompass()[:2], int(obs.getWindSpeedKnots()) ))
    time.sleep(3)

while True:
  display.write_string(time.strftime('%I%M'))

  display.colon_on()
  time.sleep(0.5)
  display.colon_off()
  time.sleep(0.5)

  if int(time.strftime('%M')) % 10 == 0:
    weather()

