#!/usr/bin/env python
import requests
import json

class BitcoinWorker:
	def __init__(self):
		self.difficulty = get_difficulty()
		#self.hashrate = get_net_hashrate()
		#self.dailyelec = daily_watt_cost()
		#self.poolcosts = get_poolcosts()
		#self.exrate = get_exchangerate() 
	#static methods here for organization
	@staticmethod
	def get_difficulty():
		d = requests.get('https://blockchain.info/q/getdifficulty')
		udiff = d.text.encode('utf8')
		dj = json.loads(udiff)
		return difficulty
	@staticmethod
	def daily_watt_cost():
		usage_in_kw = get_wattage() / 1000
		daily_kwh_cost = get_wattcost() * 24
		daily_cost = float(usage_in_kw) * float(daily_kwh_cost)
		return daily_cost
	@staticmethod
	def daily_hashrate():
		d = get_difficulty()
		h = ask_hashrate()
		sec_genhash = (d * 2**32) / h 
		day_hashrate = float(84000) / float(sec_genhash)
		return day_hashrate
	@staticmethod
	def get_net_hashrate():
		h = requests.get('https://blockchain.info/q/hashrate')
		ht = h.text.encode('utf8')
		hj = json.loads(ht)
		net_hashrate = float(hj)
		return net_hashrate
	@staticmethod
	def get_exchangerate():
		rate = requests.get('https://blockchain.info/ticker')
		urate = rate.text
		j = json.loads(urate)
		us = j['USD']
		usrate = us['last']
		return usrate
	def ask_poolcosts():
		poolcosts = raw_input('Input percentage paid to pool maintainer in decimal notation ex .20 as 20%\n')
		percent = float(poolcosts) * 100
		ipercent = int(poolcosts)
		return percent
	def ask_hashrate():
		hashrate = raw_input('Input machine hash rate in GH/s\n')
		flhashrate = float(hashrate)
		return hashrate
	def ask_wattage():
		wattage = raw_input('Input machine power usage in Watts\n')
		flwattage = float(wattage)
		return flwattage
	def ask_wattcost():
		wattcosts = raw_input('Input electricty costs per kW in cents as float ex. 7.28\n')
		flwattcosts = float(wattcosts)
		return flwattcosts
