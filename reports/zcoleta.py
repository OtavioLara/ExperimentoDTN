#!/usr/bin/env python3
import os
def main():
	files = os.listdir("/home/gnuradio/Documents/the-one/reports/")
	router = ["EpidemicRouter", "ProphetRouter", "SprayAndWaitRouter"]
	for l in router:
		for i in range (5, 55, 5):
			for j in range(20, 160, 20):
				for k in range(25, 125, 25):
					old = "12myScenario{}{}{}{}_MessageStatsReport.txt".format(l, i, j, k)
					new = "12myScenario_{}_{}_{}_{}.txt".format(l, i, j, k)
					os.system("mv {} {}".format(old, new))
if __name__ == '__main__':
	main()
