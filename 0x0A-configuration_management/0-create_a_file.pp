file {'name':
  ensure  => file,
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
  mode    => '0744',
}
