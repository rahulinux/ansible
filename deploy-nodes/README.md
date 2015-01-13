#Usage 

Download repo

```
git clone https://github.com/rahulinux/ansible
```
cd into it and change variables as per your requirement like version details 

```
cd ansible/deploy-nodes/
vim group_vars/all 
```
Define your remote hosts in "`ansible-hosts`"

Run Playbook 

```
ansible-playbook -i ansible-hosts site.yml
```
