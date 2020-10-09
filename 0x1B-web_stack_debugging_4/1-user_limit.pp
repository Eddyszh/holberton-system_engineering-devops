#Setting up the os max open file limit
exec { 'maxlimit' :
  command => 'sed -i "s/4/10000/g" /etc/security/limits.conf; sed -i "s/5/10000/g" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -e /etc/security/limits.conf',
}
