# Puppet script that sets up your web servers for the deployment of web_static

class web_static_setup {

  # Ensure Nginx is installed
  package { 'nginx':
    ensure => 'installed',
  }

  # Create the necessary directories
  file { '/data/web_static/releases':
    ensure => 'directory',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
  }

  # Create a simple HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => "<html>
  <head>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>",
  }

  # Create a symbolic link for /data/web_static/current
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
  }

  # Ensure proper ownership for the /data directory
  file { '/data':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    recurse => true,
  }

  # Configure Nginx
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "server {
    listen 80;
    server_name makau.tech;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
",
  }

  # Test Nginx configuration
  exec { 'test_nginx_config':
    command     => '/usr/sbin/nginx -t',
    path        => ['/usr/sbin', '/usr/bin'],
    refreshonly => true,
    notify      => Service['nginx'],
  }

  # Restart Nginx if the configuration is correct
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Include the class
include web_static_setup
