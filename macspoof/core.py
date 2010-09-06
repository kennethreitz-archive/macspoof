# -*- coding: utf-8 -*-

import macspoof

__all__ = ['spoof']

def spoof(interface, mac_address=None):
	"""Spoofs mac address of given interface"""
	
	if not mac_address:
		mac_address = macspoof.generator.random_mac(pretty=True)
		
	if type(interface) is str:
		interface = macspoof.interfaces.Interface(interface)
		
	
	macspoof.log.notify(interface.spoof(mac_address))
