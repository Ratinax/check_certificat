import ssl
import socket

def check_certificate(ip_address, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((ip_address, port)) as sock:
            with context.wrap_socket(sock, server_hostname=ip_address) as ssock:
                cert = ssock.getpeercert()

        cert_valid = cert and ('issuer' in cert) and ('subject' in cert)

        if cert_valid:
            print("Certificat not valid")
        else:
            print("Certificat no valid")

    except Exception as e:
        print(f"Erreur while checking certificat validation: {e}")

check_certificate('127.0.0.1')
