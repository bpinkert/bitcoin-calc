#!/usr/bin/env python
import requests
import json

class BitcoinWorker:
	def __init__(self):
		self.difficulty = get_difficulty()
		self.hashrate = ""
		self.wattage = "" 
		self.wattcost = ""		
		self.dailycost = ""		
#self.exchrate = get_exchangerate()
	#ask for information first
	def ask_poolcosts(self):
		poolcosts = raw_input('Input percentage paid to pool maintainer in decimal notation ex .20 as 20%\n')
		percent = float(poolcosts) * 100
		ipercent = int(poolcosts)
		return percent
	def ask_worker_hashrate(self):
		hashrate = raw_input('Input machine hash rate in GH/s\n')
		flhashrate = float(hashrate)
		self.hashrate = flhashrate
		return flhashrate
	def ask_worker_wattage(self):
		wattage = raw_input('Input machine power usage in Watts\n')
		flwattage = float(wattage)
		self.wattage = flwattage
		return flwattage
	def ask_wattcost(self):
		wattcosts = raw_input('Input electricty costs per kW in cents as float ex. 7.28\n')
		flwattcosts = float(wattcosts)
		self.wattcost = flwattcosts
		return flwattcosts
	def daily_watt_cost(self):
		usage_in_kw = self.ask_wattage() / 1000
		daily_kwh_cost = ask_wattcost() * 24
		daily_cost = float(usage_in_kw) * float(daily_kwh_cost)
		self.dailycost = daily_cost
		return daily_cost
	def daily_hashrate(self):
		# do we need this?
		d = get_difficulty()
		h = ask_worker_hashrate()
		sec_genhash = (d * 2**32) / h 
		day_hashrate = float(84000) / float(sec_genhash)
		return day_hashrate
	#static methods here for organization
	@staticmethod
	def get_difficulty():
		d = requests.get('https://blockchain.info/q/getdifficulty')
		udiff = d.text.encode('utf8')
		dj = json.loads(udiff)
		return difficulty
	@staticmethod
	def get_net_hashrate():
		h = requests.get('https://blockchain.info/q/hashrate')
		ht = h.text.encode('utf8')
		hj = json.loads(ht)
		hashrate = float(hj)
		return hashrate
	@staticmethod
	def get_exchangerate():
		rate = requests.get('https://blockchain.info/ticker')
		urate = rate.text
		j = json.loads(urate)
		us = j['USD']
		exchrate = us['last']
		return exchrate
