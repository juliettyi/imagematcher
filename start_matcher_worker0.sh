killall -9 python3
nohup python3 -u matcher_worker.py --id=0 --index_names=0K_10K,10K_30K,30K_50K --use_kafka=1 &
tail -f nohup.out
