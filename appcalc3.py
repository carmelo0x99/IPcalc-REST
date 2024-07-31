#!/usr/bin/env python3
import ipaddress
from flask import Flask, abort, jsonify, make_response

app = Flask(__name__)
PORT = 5050

@app.errorhandler(400)
def not_an_ip(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.route('/appcalc3/api/v1.0/<path:subnet>', methods=['GET'])
def ipdecode(subnet):
    try:
        ipif = ipaddress.ip_interface(subnet)
    except:
        abort(400)

    return jsonify(
        Address = str(ipif.ip),
        Mask = str(ipif.netmask),
        CIDR = str(ipif.network).split('/')[1],
        Network = str(ipif.network).split('/')[0],
        Broadcast = str(ipif.network.broadcast_address)
)

if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug = True)
    app.run(host='0.0.0.0', port = PORT)

