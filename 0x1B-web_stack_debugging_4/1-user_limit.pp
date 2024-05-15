# Puppet manifest to adjust file descriptor limits for the holberton user

exec { 'adjust-file-descriptor-limit':
  command => '/bin/echo "holberton soft nofile 65536" >> /etc/security/limits.conf && /bin/echo "holberton hard nofile 65536" >> /etc/security/limits.conf',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  unless  => '/bin/grep -q "^holberton[[:space:]]soft[[:space:]]nofile[[:space:]]65536" /etc/security/limits.conf && /bin/grep -q "^holberton[[:space:]]hard[[:space:]]nofile[[:space:]]65536" /etc/security/limits.conf',
}
