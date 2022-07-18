#!/usr/bin/env python
from daemonize import Daemonize
from urllib.request import urlopen
import json, time

pid = "/tmp/ncsgitops-agent.pid"
waitsec = 60 
# unauth requests can only do 60 per hour 
# https://developer.github.com/v3/#rate-limiting

def main():
    commit=''
    while True:
        oldcommit=commit
        commit = get_latest_commit('dentechnologies', 'nexus-container-server-gitops')        
        if oldcommit != '' and commit != oldcommit:
            print('***** NEW COMMIT ******')
        print('last commit: %s' % commit['html_url'])
        time.sleep(waitsec)

def get_latest_commit(owner, repo):
    url = 'https://api.github.com/repos/{owner}/{repo}/commits?per_page=1'.format(owner=owner, repo=repo)
    response = urlopen(url).read()
    data = json.loads(response.decode())
    return data[0]

if __name__ == '__main__':
    #daemon = Daemonize(app="cidummy", pid=pid, action=main)
    #daemon.start()
    main()