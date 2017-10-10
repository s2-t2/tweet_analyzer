#!/bin/bash
#start rabbitmq-server
password = password
sudo rabbitmq-server &

for number in {1..10}
do 
	sudo rabbitmqctl add_user user$number password
	sudo rabbitmqctl add_vhost "user""$number""_vhost"
	sudo rabbitmqctl set_user_tags "user""$number" "user""$number""_tag"
	sudo rabbitmqctl set_permissions -p "user""$number""_vhost" "user""$number" ".*" ".*" ".*"

done
exit 0
