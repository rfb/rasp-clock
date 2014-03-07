#!/usr/bin/env python

import time
from display import Display
from circuits import Debugger, Component, Event, Timer
from circuits.app import Daemon
import pymetar

class App(Component):
  def init(self):
    self.display = Display()
    self.clock = Clock().register(self)
    self.weather = Weather().register(self)
    Daemon('edc.pid', '/home/rfb/clock/', 'stdin.log', 'stdout.log', 'stderr.log').register(self)

  def scroll_part(self, message):
    if not self.scrolling:
      message = '    ' + message """ pad the message left """

    if len(message) > 0:
      self.scrolling = True
      self.block_updates = True
      self.display.write_string('{0: <4}'.format(message[0:4]))

      Timer(1, Event.create("scroll_part", message[1:])).register(self)
    else:
      self.block_updates = False
      self.scrolling = False

  def scroll_message(self, message):
    if not self.scrolling:
      Timer(1, Event.create("scroll_part", message)).register(self)

  def update_display(self, string):
    if not self.block_updates:
      self.display.write_string(string)

  def toggle_colon(self):
    if self.block_updates:
      self.display.colon_off()
    else:
      self.display.toggle_colon()

  def started(self, component):
    self.block_updates = False
    self.scrolling = False
    Timer(0.5, Event.create("toggle_colon"), persist=True).register(self)

class Clock(Component):
  def send(self):
    self.fire(Event.create("update_display", time.strftime('%I%M')))

  def started(self, component):
    Timer(1, Event.create("send"), persist=True).register(self)

class Weather(Component):
  def fetch(self):
    self.report = self.parser.ParseReport(self.fetcher.FetchReport())

  def report(self):
    if self.report:
      message = "CYZP %s%02i" % (self.report.getWindCompass(), self.report.getWindSpeedKnots())
      self.fire(Event.create("scroll_message", message))

  def started(self, component):
    self.fetcher = pymetar.ReportFetcher('CYZP')
    self.parser  = pymetar.ReportParser()

    self.fire(Event.create("fetch"))

    Timer(60*30, Event.create("fetch"), persist=True).register(self)
    Timer(60, Event.create("report"), persist=True).register(self)

App().run()
#(App() + Debugger()).run()

