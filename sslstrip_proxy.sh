#!/bin/sh
echo "Make sure you already run sslstrip ..."
echo "Redirecting all web request to SSL Strip Proxy Port"
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000