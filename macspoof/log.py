from logbook import Logger
from logbook.notifiers import GrowlHandler


app_name = Logger(u'MacSpoof')
handler = GrowlHandler()



def notify(msg):
	with handler:
		app_name.notice(msg)
		print msg