#!/bin/bash

# add user 'alice' with password 'alice123'
sudo rabbitmqctl add_user alice alice123
# add virtual host 'alice_vhost'
sudo rabbitmqctl add_vhost alice_vhost
# add user tag 'alice_tag' for user 'alice'
sudo rabbitmqctl set_user_tags alice alice_tag
# set permission for user 'alice' on virtual host 'alice_vhost'
sudo rabbitmqctl set_permissions -p alice_vhost alice ".*" ".*" ".*"
