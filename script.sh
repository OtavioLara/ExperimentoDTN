#!/bin/bash
#Thousands of intances
start=`date +%s`
echo 'Starting experiment'
cat base.txt>file.txt
pids=()
num_cores=7
cont=0
cont_total=0
protocols=("EpidemicRouter" "SprayAndWaitRouter" "ProphetRouter")
for protocol in "${protocols[@]}";do
	out=$(cat file.txt |  sed -r "s/(Group.router =)(.*)/\1 $protocol/g")
	printf "%s" "$out">file.txt
	for cont_alc in `seq 5 5 50`;do
		out=$(cat file.txt |  sed -r "s/(btInterface.transmitRange =)(.*)/\1 $cont_alc/g")
		printf "%s" "$out">file.txt
		for cont_escala in `seq 20 20 140`;do
			out=$(cat file.txt | sed -r "s/(Group.nrofHosts =)(.*)/\1 $cont_escala/g")
			printf "%s" "$out">file.txt
			for cont_buff in `seq 25 25 100`;do
				out=$(cat file.txt | sed -r "s/(Group.bufferSize =)(.*)/\1 ${cont_buff}M/g")
				printf "%s" "$out">file.txt
				out=$(cat file.txt | sed -r "s/(Scenario.name =)(.*)/\1 12myScenario$protocol$cont_alc$cont_escala$cont_buff/g")
				printf "%s" "$out">file.txt
				cat file.txt>"file${cont}.txt"
				./one.sh -b 1 "file${cont}.txt" > log &
				((cont_total++))
				echo "$cont_total de 840"
				((cont++))
				pids+=($!)
				if [ $cont -eq $num_cores ]; then
					echo ''
					wait $pids
					cont=0
					pids=()
				fi
			done
		done
	done
done
wait $pids
end=`date +%s`
run_time=$((end-start))
echo "CONCLUIDO COM SUCESSO TODOS OS 840 EM $run_time s"
