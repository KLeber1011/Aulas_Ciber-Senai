import requests

def verificar_site_online(url):
    try:
        # Envia uma solicitação HTTP GET para o site
        response = requests.get(url)
        
        # Verifica o código de status da resposta
        if response.status_code == 200:
            print(f"O site {url} está online!")
        else:
            print(f"O site {url} está offline. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro ao tentar acessar o site {url}: {e}")

# URL do site a ser verificado
url = 'https://www.exemplo.com'

# Chama a função para verificar se o site está online
verificar_site_online(url)
