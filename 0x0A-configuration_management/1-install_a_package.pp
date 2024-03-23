# install flask version (2.1.0) from pip3
package { 'flask':
  ensure   => '2.1.0', #ensure flask version 2.1.0
  provider => 'pip3', # the provider of flask is pip3
}
