#!/usr/bin/env  python2.7

import os
import json
import argparse
import requests

name_tags = [ 'Web_server' , 'DB_Server' ]

default_remote_host_vars = { "remote_user" : "deploy" }

def parse_argument(help=False):
     parser = argparse.ArgumentParser()
     parser.add_argument('--env',action='store', dest='env', default=None,
                         help='specify the env name like Prod/Dev')
     parser.add_argument('--list',action='store_true', default=False,
                         dest='list_option',help='list all hosts')
     parser.add_argument('--host',action='store',dest='host',
                         help='check host vars')
     parser.add_argument('--version', action='version', version='%(prog)s 1.0')
     if help == True:
        return parser.print_help()
     return parser.parse_args()



def get_ip(tag,env=None,eip=False):
   """return ip address of requested tag for respective environtment"""
   api_url = 'http://api.rahulinux.io/ip?host={0}&env={1}&eip={2}'
   try:
      resp = requests.get(api_url.format(tag,env,eip))
   except requests.exceptions.RequestException as e:
      return e
   if len(resp.text) >= 30:
       return resp.text.split()
   return  [ resp.text ]



if __name__ == '__main__':
  args = parse_argument()
  inventory = { "_meta" : { "hostvars": {  } }  }
  eip = os.getenv('EIP',False)
  if args.env == None:
     env = os.environ['ENV']
  else:
     env = args.env
  if args.host != None:
     print inventory
  elif args.list_option == True:
     for tag in name_tags:
        data = get_ip(tag,env,eip)
        if "error" not in str(data):
             inventory.update({
                                 "tag_Name_" + tag : {
                                     "hosts": data,
                                     "vars": default_remote_host_vars
                                     }
                               })

     print json.dumps(inventory,indent=4)
  else:
    parse_argument(help=True)
