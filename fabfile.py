from fabric.api import *

env.hosts = [ 'raspi' ]

def pack():
  local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
  dist = local('python setup.py --fullname', capture=True).strip()
  put('dist/%s.tar.gz' % dist, '/tmp/clock.tar.gz')

  with cd('/tmp'):
    run('tar xzf /tmp/clock.tar.gz')

  with cd('/tmp/%s' % dist):
    run('sudo python setup.py install')

  run('supervisorctl restart clock')
