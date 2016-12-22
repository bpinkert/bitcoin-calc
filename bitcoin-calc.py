#!/usr/bin/env python
import requests
import json

class BitcoinWorker:
	def __init__():
		self.difficulty = get_difficulty()
		self.hashrate = get_hashrate()
		self.dailyelec = daily_watt_cost()
		self.poolcosts = get_poolcosts()
		self.exrate = get_exchangerate() 
	def get_difficulty():
		d = requests.get('https://blockchain.info/q/getdifficulty')
		udiff = d.text.encode('utf-8')
		dj = json.loads(udiff)
		difficulty = float(dj)
		return difficulty
	def get_hashrate():
		hashrate = raw_input('Input machine hash rate in GH/s\n')
		flhashrate = float(hashrate)
		return hashrate
	def get_wattage():
		wattage = raw_input('Input machine power usage in Watts\n')
		flwattage = float(wattage)
		return flwattage
	def get_wattcost():
		wattcosts = raw_input('Input electricty costs per kW in cents as float ex. 7.28\n')
		flwattcosts = float(wattcosts)
		return flwattcosts
	def daily_watt_cost():
		usage_in_kw = get_wattage() / 1000
		daily_kwh_cost = get_wattcost() * 24
		daily_cost = float(usage_in_kw) * float(daily_kwh_cost)
		return daily_cost
	def daily_hashrate():
		d = get_difficulty()
		h = get_hashrate()
		sec_genhash = (d * 2**32) / h 
		day_hashrate = float(84,000) / float(sec_genhash)
		return day_hashrate
	def get_net_hashrate():
		h = requests.get('https://blockchain.info/q/hashrate')
		ht = h.text.encode('utf-8')
		hj = json.loads(ht)
		net_hashrate = float(hj)
		return net_hashrate
	def get_poolcosts():
		poolcosts = raw_input('Input percentage paid to pool maintainer in decimal notation ex .20 as 20%\n')
		percent = float(poolcosts)
		return percent
	def get_exchangerate():
		rate = requests.get('https://blockchain.info/ticker')
		urate = rate.text.encode('utf-8')
		j = json.loads(urate)
		us = j['USD']
		usrate = us['last']
		return usrate

