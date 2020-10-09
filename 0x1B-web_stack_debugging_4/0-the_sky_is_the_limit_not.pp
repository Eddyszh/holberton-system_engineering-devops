#Setting up the limit of max open files
exec { 'maxlimit' :
  command => 'sed -i "s/15/65536/g" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -e /etc/default/nginx',
}
