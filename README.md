# IP-REST
A REST implementation of an IPv4/IPv6 subnet calculator

### Setup your environment
```
 ~/github/IP-REST > |/ master > python3 -m venv .

 ~/github/IP-REST > |/ master > source bin/activate

(IP-REST) ~/github/IP-REST > |/ master > pip3 install Flask
```

### Install any dependencies
```
(IP-REST) ~/github/IP-REST > |/ master > pip3 install Flask
Collecting Flask
  Using cached https://files.pythonhosted.org/packages/f2/28/2a03252dfb9ebf377f40fba6a7841b47083260bf8bd8e737b0c6952df83f/Flask-1.1.2-py2.py3-none-any.whl
Collecting click>=5.1 (from Flask)
  Using cached https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from Flask)
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from Flask)
  Using cached https://files.pythonhosted.org/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b318f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from Flask)
  Using cached https://files.pythonhosted.org/packages/30/9e/f663a2aa66a09d838042ae1a2c5659828bb9b41ea3a6efa20a20fd92b121/Jinja2-2.11.2-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->Flask)
  Using cached https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
Installing collected packages: click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
```

### Run local test
```
(IP-REST) ~/github/IP-REST > |/ master > python3 ./appcalc3.py
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
$ curl http://10.0.2.70:5000//appcalc3/api/v1.0/192.168.100.0/24
{"Address":"192.168.100.0","Broadcast":"192.168.100.255","CIDR":"24","Mask":"255.255.255.0","Network":"192.168.100.0"}

$ curl http://10.0.2.70:5000//appcalc3/api/v1.0/2001:db8::1000  
{"Address":"2001:db8::1000","Broadcast":"2001:db8::1000","CIDR":"128","Mask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","Network":"2001:db8::1000"}
```

### Time to make our app into a container
```
(IP-REST) ~/github/IP-REST > |/ master > docker build -t ccarmelo/appcalc3:1.0 .
Sending build context to Docker daemon  9.725MB
Step 1/8 : FROM python:3.7-alpine
...
Step 8/8 : ENTRYPOINT ["python3","./appcalc3.py"]
 ---> Running in f1eadea7fee4
Removing intermediate container f1eadea7fee4
 ---> 4fa318d23856
Successfully built 4fa318d23856
Successfully tagged ccarmelo/appcalc3:1.0
```

### Run the container the imperative way
```
(IP-REST) ~/github/IP-REST > |/ master > docker run -d -p 5000:5000 ccarmelo/appcalc3:1.0
43ae12154a8e315eaef4d201f9cf6304b874dd5c7bb012605350c7215c34019e
```
**NOTE**: the app listens on port 5000 thus it's necessary to explicitly open the port for its operation

### Run the container the declarative way (e.g. with `docker-compose.yaml`)
```
(IP-REST) ~/github/IP-REST > |/ master ●✚ > docker-compose up -d
Creating network "ip-rest_default" with the default driver
Creating ip-rest_appcalc3_1 ... done

(IP-REST) ~/github/IP-REST > |/ master ●✚ > docker-compose ps
       Name                 Command          State           Ports
---------------------------------------------------------------------------
ip-rest_appcalc3_1   python3 ./appcalc3.py   Up      0.0.0.0:5000->5000/tcp

(IP-REST) ~/github/IP-REST > |/ master ●✚ > docker-compose down
Stopping ip-rest_appcalc3_1 ... done
Removing ip-rest_appcalc3_1 ... done
Removing network ip-rest_default
```
