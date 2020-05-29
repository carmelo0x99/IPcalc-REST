# IP-REST
A REST implementation of an IPv4/IPv6 subnet calculator

### Setup your environment
```
 ~/github/IP-REST > python3 -m venv .

 ~/github/IP-REST > source bin/activate

(IP-REST) ~/github/IP-REST > pip3 install Flask
```

### Install any dependencies
```
(IP-REST) ~/github/IP-REST > pip3 install Flask
...
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
```

### Run local test
```
(IP-REST) ~/github/IP-REST > python3 appcalc3.py
 * Serving Flask app "appcalc3" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ...
```

#### From another tab or host...
```
$ curl http://<ip_address>:5000//appcalc3/api/v1.0/192.168.100.0/24
{"Address":"192.168.100.0","Broadcast":"192.168.100.255","CIDR":"24","Mask":"255.255.255.0","Network":"192.168.100.0"}

$ curl http://<ip_address>:5000//appcalc3/api/v1.0/2001:db8::1000  
{"Address":"2001:db8::1000","Broadcast":"2001:db8::1000","CIDR":"128","Mask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","Network":"2001:db8::1000"}
```

### Time to make our app into a container
```
(IP-REST) ~/github/IP-REST > docker build -t ccarmelo/appcalc3:1.0 .
Sending build context to Docker daemon  9.725MB
Step 1/8 : FROM python:3.7-alpine
...
Step 8/8 : ENTRYPOINT ["python3","./appcalc3.py"]
...
Successfully tagged ccarmelo/appcalc3:1.0
```

### Run the container the imperative way
```
(IP-REST) ~/github/IP-REST > docker run -d -p 5000:5000 ccarmelo/appcalc3:1.0
43ae12154a8e315eaef4d201f9cf6304b874dd5c7bb012605350c7215c34019e
```
**NOTE**: the app listens on port 5000 thus it's necessary to explicitly open the port for its operation

### Run the container the declarative way (e.g. with `docker-compose.yaml`)
```
(IP-REST) ~/github/IP-REST >  master ●✚ > docker-compose up -d
Creating network "ip-rest_default" with the default driver
Creating ip-rest_appcalc3_1 ... done

(IP-REST) ~/github/IP-REST >  master ●✚ > docker-compose ps
       Name                 Command          State           Ports
---------------------------------------------------------------------------
ip-rest_appcalc3_1   python3 ./appcalc3.py   Up      0.0.0.0:5000->5000/tcp

(IP-REST) ~/github/IP-REST >  master ●✚ > docker-compose down
Stopping ip-rest_appcalc3_1 ... done
Removing ip-rest_appcalc3_1 ... done
Removing network ip-rest_default
```
