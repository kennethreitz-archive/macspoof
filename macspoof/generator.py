# -*- coding: utf-8 -*-

"""

>>> random_mac()
00163e4bb865

>>> random_mac(pretty=True)
00:16:3e:62:7a:ea

"""

import random



def random_mac(pretty=False):
	"""Returns a completely random Mac Address"""
	_mac = [
		0x00, 0x16, 0x3e, 
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff)
	]
	if pretty:
		_address = ':'.join(map(lambda x: "%02x" % x, _mac))
	else:
		_address = ''.join(map(lambda x: "%02x" % x, _mac))
	
	return _address



if __name__ == '__main__':
	 print random_mac(pretty=True)
