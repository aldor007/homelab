ansible cluster  -a "/sbin/poweroff"  -i inventory/hosts.ini --key-file ~/.ssh/id_rsa_ansible -u ansible  --become -vv
