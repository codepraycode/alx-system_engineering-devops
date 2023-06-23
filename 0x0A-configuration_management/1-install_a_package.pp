#!/user/bin/pup
# Install flask over version 2.1.0

# Install python and pip
package { 'python3':
  ensure => installed
}

package { 'python3-pip':
  ensure => installed
}

# Install flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
