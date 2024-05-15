# Puppet manifest to change the ULIMIT parameter in /etc/default/nginx file

file { '/etc/default/nginx':
  ensure  => present,
  content => "# Note: You may want to look at the following page before setting the ULIMIT.\n#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile\n# Set the ulimit variable if you need defaults to change.\n#  Example: ULIMIT=\"-n 4096\"\nULIMIT=\"-n 15\"\n",
}

augeas { 'nginx_ulimit_parameter':
  context => '/etc/default/nginx',
  changes => "set ULIMIT '-n 500'",
}
