install:
    pip install -r requirements.txt

run:
    python main.py -t <target> -a <attack_type> -n <num_threads> -p proxies.txt

.PHONY: install run
