import ssl
import socket

def check_certificate(ip_address, port, cafile=None):
	try:
		context = ssl.create_default_context(cafile=cafile)
		with socket.create_connection((ip_address, port)) as sock:
			with context.wrap_socket(sock, server_hostname=ip_address) as ssock:
				cert = ssock.getpeercert()
		cert_valid = cert and ('issuer' in cert) and ('subject' in cert)
		if cert_valid:
			return True
		else:
			return False
	except Exception as e:
		return False

print(check_certificate('127.0.0.1', 8080, 'cert.pem'))