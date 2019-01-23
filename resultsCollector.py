#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot  as plt
import os
begin = "/home/otavio/Documents/the-one/reports/12myScenario_"
protocols = ["EpidemicRouter", "ProphetRouter", "SprayAndWaitRouter"]
protocols_name = ["Epidemic", "Prophet", "Spray and Wait"]

def gera_grafico(cur_range, line, xlabel, ylabel, fixed="range", buff=50, nodes=60, rang=25):
	map_oh = {}
	cont = 0
	for protocol in protocols:
		map_oh[protocol] = []
		for value in cur_range:
			if fixed == 'Tamanho do Buffer':
				file_name = "{}{}_{}_{}_{}.txt".format(begin, protocol, rang, nodes, value )
			elif fixed == 'Número de Nós':
				file_name = "{}{}_{}_{}_{}.txt".format(begin, protocol, rang, value, buff )	
			elif fixed == 'Alcance de Transmissão':
				file_name = "{}{}_{}_{}_{}.txt".format(begin, protocol, value, nodes, buff )
			fp = open(file_name, 'r')
			lines = fp.readlines()
			fp.close()
			map_oh[protocol].append(float(lines[line].split(':')[1]))
		plt.plot(cur_range, map_oh[protocol], **{'marker' : 'o'}, label=protocols_name[cont])
		cont+=1
	plt.grid()
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	title = xlabel+ " X "+ylabel
	plt.title(title)
	plt.legend()
	try:
		os.mkdir("resultsImgs")
	except:
		pass	
	plt.savefig("resultsImgs/"+title+".png")
	plt.cla()

def main(args):
	results = [("Taxa de entrega", 9), ("Latencia Média", 12), ("Overhead", 11), ("Buffer time", 16)]
	parameters = [("Alcance de Transmissão", range(5, 55, 5)), ("Número de Nós", range(20, 160, 20)), ("Tamanho do Buffer", range(25, 120, 25))] 
	for result in results:
		for parameter in parameters:
			gera_grafico(parameter[1], result[1], parameter[0], result[0], fixed=parameter[0], buff=100, nodes=140, rang=50)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

