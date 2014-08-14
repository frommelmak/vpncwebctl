from bottle import static_file, template, post, request, route, run, auth_basic
import ConfigParser
import subprocess

def check_login(username, password):
    config = ConfigParser.ConfigParser()
    config.read('server.conf')
    u = config.get('vpncweb', 'username')
    p = config.get('vpncweb', 'password')
    if ( u == username and p == password ):
        return True
    else:
        return False

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/opt/vpncwebctl/static')

@route('/initctl', method='POST')
@auth_basic(check_login)
def initctl():
    username = request.forms.get('username')
    password = request.forms.get('password')
    action = request.forms.get('initctl')
    config = ConfigParser.ConfigParser()
    config.read('server.conf')
    profile = config.get('vpnc', 'profile')
    if (action == "start"):
        p = subprocess.Popen(["vpnc-connect", profile], stdout=subprocess.PIPE)
        p_output, p_err = p.communicate()
        return template('initctl_template', action=action, output=p_output)
    elif (action == "stop"):
        p = subprocess.Popen(["vpnc-disconnect"], stdout=subprocess.PIPE)
        p_output, p_err = p.communicate()
        return template('initctl_template', action=action, output=p_output)
    else:
        return "<p>Unknown Error</p>"


@route('/')
@route('/status')
@auth_basic(check_login)
def status():
    config = ConfigParser.ConfigParser()
    config.read('server.conf')
    remote_ip = config.get('vpnc', 'remote_ip')
    p1 = subprocess.Popen(["pgrep","vpnc"], stdout=subprocess.PIPE)
    p1_output, p1_err = p1.communicate()
    p2 = subprocess.Popen(["ip","addr","show","tun0"], stdout=subprocess.PIPE) 
    p2_output, p2_err = p2.communicate()
    p3 = subprocess.Popen(["ping", "-q", "-c", "1", remote_ip], stdout=subprocess.PIPE)
    p3_output, p3_err = p3.communicate()
    if '1 received' in p3_output:
        status = "Connected"
    else:
        status = "Disconnected"

    return template('status_template', status=status, pid=p1_output, tun=p2_output, ping=p3_output)

if __name__ == '__main__':
   config = ConfigParser.ConfigParser()
   config.read('server.conf')
   port = config.get('vpncweb', 'port')
   run(host='0.0.0.0',port=port)
