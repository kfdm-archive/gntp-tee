#!/usr/bin/env python
import sys
import signal
from optparse import OptionParser
try:
	from gntp.notifier import GrowlNotifier
except ImportError:
	sys.exit('Requires http://github.com/kfdm/gntp')

APPLICATION_NAME = 'gntp-tee'
NOTIFICATION_NAME = 'Pipe'

def signal_exit(a,b): sys.exit()

class Parser(OptionParser):
	def __init__(self):
		OptionParser.__init__(self)
		self.add_option('-H','--hostname',
					help='Destination Host',
					dest='host',
					default='localhost')
		self.add_option('-p','--port',
					help='Destination Port',
					dest='port',
					default=23053)
		self.add_option('-P','--password',
					help='GNTP Password',
					dest='password',
					default=None)
		self.add_option('-A','--appname',
					help='GNTP Application Name',
					dest='app',
					default=APPLICATION_NAME)
		self.add_option('-v',dest='debug',
					help='Print Debugging to stderr',
					action='store_true',
					default=False)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_exit)
	
	parser = Parser()
	(options, args) = parser.parse_args()
	growl = GrowlNotifier(
		applicationName = options.app,
		notifications = [NOTIFICATION_NAME],
		hostname = options.host,
		password = options.password,
		port = options.port,
		debug = options.debug,
	)
	growl.register()
	while( True ):
		line = sys.stdin.readline()
		if not line: break
		sys.stdout.write(line)
		growl.notify(NOTIFICATION_NAME,NOTIFICATION_NAME,line)
