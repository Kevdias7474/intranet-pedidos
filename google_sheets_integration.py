import json
import requests
from datetime import datetime

def get_google_sheets_data(sheet_id, range_name, api_key):
    """
    Função para obter dados do Google Sheets usando a API pública
    
    Args:
        sheet_id (str): ID da planilha do Google Sheets
        range_name (str): Range dos dados (ex: 'Sheet1!A:Z')
        api_key (str): Chave da API do Google
    
    Returns:
        dict: Dados formatados para a intranet
    """
    
    # URL da API do Google Sheets (modo público)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}?key={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'values' in data:
            rows = data['values']
            
            # Assumindo que a primeira linha são os cabeçalhos
            headers = rows[0] if rows else []
            
            # Processar dados dos clientes
            clients_data = {}
            
            for row in rows[1:]:  # Pular cabeçalho
                if len(row) > 0:  # Verificar se a linha não está vazia
                    client_name = row[0].lower().strip() if len(row) > 0 else ""
                    
                    if client_name:
                        clients_data[client_name] = {
                            'name': row[0] if len(row) > 0 else "",
                            'tipo_obra': row[1] if len(row) > 1 else "",
                            'valor_total': row[2] if len(row) > 2 else "",
                            'data_entrega': row[6] if len(row) > 6 else "",
                            'estado': row[7] if len(row) > 7 else "",
                            'municipio': row[8] if len(row) > 8 else "",
                            'status': 0  # Status padrão (fase inicial)
                        }
            
            return clients_data
            
    except Exception as e:
        print(f"Erro ao acessar Google Sheets: {e}")
        return {}

def create_json_data_file(clients_data, output_file):
    """
    Criar arquivo JSON com os dados dos clientes
    
    Args:
        clients_data (dict): Dados dos clientes
        output_file (str): Caminho do arquivo de saída
    """
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(clients_data, f, ensure_ascii=False, indent=2)

def update_client_status(client_name, new_status, data_file):
    """
    Atualizar status de um cliente no arquivo JSON
    
    Args:
        client_name (str): Nome do cliente
        new_status (int): Novo status (0-3)
        data_file (str): Caminho do arquivo JSON
    """
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            clients_data = json.load(f)
        
        client_key = client_name.lower().strip()
        if client_key in clients_data:
            clients_data[client_key]['status'] = new_status
            clients_data[client_key]['last_updated'] = datetime.now().isoformat()
            
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(clients_data, f, ensure_ascii=False, indent=2)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"Erro ao atualizar status: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    # Substitua estas variáveis com suas informações reais
    SHEET_ID = "1OZqcreJ0ZzE4LJ2xOK4PyaZdZzP_UhGKczAP8V6kK4o"
    API_KEY = "AIzaSyBDSYtmopOdeAyI3HpqNTKejhlxg2EJqYE"
    RANGE_NAME = "Maio!A:I"

    # Buscar dados reais da planilha
    clients_data = get_google_sheets_data(SHEET_ID, RANGE_NAME, API_KEY)
    
    if clients_data:
        create_json_data_file(clients_data, 'clients_data.json')
        print("Arquivo de dados criado com sucesso!")
    else:
        print("Erro ao carregar dados da planilha. Verifique o SHEET_ID, API_KEY e RANGE_NAME.")



