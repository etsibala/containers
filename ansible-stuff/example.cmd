ansible all -m command -a 'uname -a'
ansible all -m command -a 'usermod --shell /bin/bash sysadmin'
ansible all -m copy -a 'content="Managed by Ansible" dest="/etc/motd"'

