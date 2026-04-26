import requests

def check_security(url):
    """
    Função simples para verificar cabeçalhos de segurança HTTP.
    """
    try:
        # Adiciona https:// caso o usuário esqueça
        if not url.startswith('http'):
            url = 'https://' + url
            
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        print(f"\n--- Relatório de Segurança para: {url} ---")
        
        # Cabeçalhos cruciais para Cybersecurity
        security_headers = {
            "Strict-Transport-Security": "Protege contra interceptação (HSTS).",
            "X-Frame-Options": "Previne ataques de Clickjacking.",
            "X-Content-Type-Options": "Impede o farejamento de MIME (Sniffing).",
            "Content-Security-Policy": "Controla recursos que a página pode carregar."
        }
        
        for header, description in security_headers.items():
            if header in headers:
                print(f"[✅] {header}: Presente. {description}")
            else:
                print(f"[❌] {header}: FALTANDO! {description}")
                
    except Exception as e:
        print(f"Erro ao analisar a URL: {e}")

if __name__ == "__main__":
    # Exemplo de uso
    target = "google.com"
    check_security(target)
