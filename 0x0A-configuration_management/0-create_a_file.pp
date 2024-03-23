#a script that creates a file in /tmp

file {'/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
  mode    => '0744',
}
