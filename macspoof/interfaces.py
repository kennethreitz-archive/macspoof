import netifaces
import os

BLACK_ID = ('lo0', 'gif0')
BLACK_MAC = ('', '::1')

class Interface(object):
	"""Network Interface Object"""
	
	def __init__(self, id):
		super(Interface, self).__init__()
		self.id = id
		
		_meta = netifaces.ifaddresses(self.id)
		self.mac = _meta[18][0]['addr']
		
		try:
			self.broadcase = _meta[2][0]['broadcast']
			self.netmask = _meta[2][0]['netmask']
			self.addr = _meta[2][0]['addr']
		except KeyError, e:
			pass
			
		try:
			self.ip6_netmask = _meta[30][0]['netmask']
			self.ip6_addr = _meta[30][0]['addr']
		except KeyError, e:
			pass		
	
	
	def __repr__(self):
		return ('<interface: %s>' % self.id)
	
	
	def __str__(self):
		return self.id
	
	
	def spoof(self, mac, air=False):
		"""Spoofs given MAC address"""
		
		if air:
			os.system(
				'sudo '
				'/System/Library/PrivateFrameworks'
				'/Apple80211.framework/Versions'
				'/Current/Resources/airport -z'
			)
		
		_status = os.system('sudo ifconfig %s ether %s' % (self.id, mac))
		
		print 'Interface %s (%s) => (%s)' % (self.id, self.mac, mac)
		


def fetch():
	"""Returns a list of interfaces objects."""
	
	_interfaces = [Interface(iface) for iface in netifaces.interfaces()]
	
	for iface in _interfaces: 
		if (iface.id in BLACK_ID) or (iface.mac in BLACK_MAC) or (len(iface.mac) < 5):
			_interfaces.remove(iface)
			
	return _interfaces
	

def list():
	"""Lists available interface names."""

	return netifaces.interfaces()
