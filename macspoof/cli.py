# -*- coding: utf-8 -*-

import opster

import macspoof


spoof_options = [
	('a', 'airport', False, 'treat interface as airport card'),
]
	
@opster.command(usage='INTERFACE <mac>', options=spoof_options)	
def spoof(interface, mac=None, **opts):
	"""spoofs mac address of given interface
	
	"""

	if interface in macspoof.interfaces.list():
		message = macspoof.core.spoof(interface, mac)
		print message
		
	else:
		print('Please specify a valid interface.')

	
@opster.command(name='list|l|ls', usage='fukit')		
def list(**opts):
	"""lists avaiable network interfaces"""
	_interfaces = macspoof.interfaces.fetch()
	for iface in _interfaces:
		print '%s (%s)' % (iface.id, iface.mac)
	
def start():
	opster.dispatch()