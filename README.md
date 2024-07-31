# IPcalc-REST
A REST implementation of an IPv4/IPv6 subnet calculator

### Setup your environment
```
% python3 -m venv .

% source bin/activate
```

### Install any dependencies
```
% (IPcalc-REST) python3 -m pip install Flask
...
```

### Run local test
```
% (IPcalc-REST) python3 appcalc3.py
 * Serving Flask app "appcalc3" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5050/ (Press CTRL+C to quit)
 ...
```

#### From another tab or host...
```
$ curl http://<ip_address>:5050/appcalc3/api/v1.0/192.168.100.0/24
{"Address":"192.168.100.0","Broadcast":"192.168.100.255","CIDR":"24","Mask":"255.255.255.0","Network":"192.168.100.0"}

$ curl http://<ip_address>:5050/appcalc3/api/v1.0/2001:db8::1000  
{"Address":"2001:db8::1000","Broadcast":"2001:db8::1000","CIDR":"128","Mask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","Network":"2001:db8::1000"}
```

### Time to make our app into a container
```
% (IPcalc-REST) docker build -t carmelo0x99/appcalc3:1.0 .
Sending build context to Docker daemon  9.725MB
Step 1/8 : FROM python:3.7-alpine
...
Step 8/8 : ENTRYPOINT ["python3","./appcalc3.py"]
...
Successfully tagged carmelo0x99/appcalc3:1.0
```

### Run the container the imperative way
```
% (IPcalc-REST) docker run -d --rm -p 5050:5050 carmelo0x99/appcalc3:1.0
43ae12154a8e315eaef4d201f9cf6304b874dd5c7bb012605350c7215c34019e
```
**NOTE**: the app listens on port 5050 thus it's necessary to explicitly open the port for its operation

### Run the container the declarative way (e.g. with `docker-compose.yaml`)
```
% (IPcalc-REST) docker-compose up -d
Creating network "IPcalc-REST_default" with the default driver
Creating IPcalc-REST_appcalc3_1 ... done

% (IPcalc-REST) docker-compose ps
       Name                 Command          State           Ports
---------------------------------------------------------------------------
IPcalc-REST_appcalc3_1   python3 ./appcalc3.py   Up      0.0.0.0:5050->5050/tcp

% (IPcalc-REST) docker-compose down
Stopping IPcalc-REST_appcalc3_1 ... done
Removing IPcalc-REST_appcalc3_1 ... done
Removing network IPcalc-REST_default
```

