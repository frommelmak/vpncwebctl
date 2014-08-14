<html>
    <head>
        <title>VPNC Web Management</title>
        <link rel="stylesheet" href="static/style.css" type="text/css">
    </head>
    <body>
        <h1>VPNC Status: {{status}}</h1>
        <h2>vpnc PID: {{pid}}</h2>
        <h2>tun0 IP</h2> <pre>{{tun}}</pre>
        <h2>Ping</h2><pre>{{ping}}</pre>
        <center>
        <form action="/initctl" method="post">
            <input name="initctl" value="start" type="submit" />
            <input name="initctl" value="stop" type="submit" />
        </form>
        </center>
    </body>
</html>
