# Como Integrar com Google Sheets Real

## Visão Geral

Este guia mostra como conectar o sistema com sua planilha real do Google Sheets, substituindo os dados de exemplo pelos dados reais dos seus clientes.

## Passo 1: Preparar sua Planilha

### 1.1 Estrutura Necessária

Sua planilha deve ter as seguintes colunas (pode ter outras, mas estas são obrigatórias):

| Coluna | Nome | Descrição | Exemplo |
|--------|------|-----------|---------|
| A | Nome | Nome do cliente | Keverson |
| B | Tipo de Obra | Tipo do projeto | Casa |
| C | Valor Total | Valor do pedido | R$ 12.112,24 |
| G | Data de Entrega | Data prevista | 09/06/2025 |
| H | Estado | Estado do cliente | RN - Rio Grande do Norte |
| I | Município | Cidade do cliente | Pedra Grande |

### 1.2 Exemplo de Planilha

```
A          B              C            D    E    F    G           H                    I
Nome       Tipo de obra   Valor total  ... ... ... Data entrega Estado               Município
Keverson   Casa          R$ 12.112,24  ... ... ... 09/06/2025   RN - Rio Grande do Norte  Pedra Grande
Bianca     Casa          R$ 13.715,11  ... ... ... 10/06/2025   RN - Rio Grande do Norte  Natal
```

## Passo 2: Configurar Acesso à Planilha

### 2.1 Tornar a Planilha Pública

1. Abra sua planilha no Google Sheets
2. Clique no botão "Compartilhar" (canto superior direito)
3. Em "Obter link", clique em "Alterar para qualquer pessoa com o link"
4. Certifique-se que está marcado "Visualizador"
5. Clique em "Copiar link"

### 2.2 Obter o ID da Planilha

Do link copiado, extraia o ID. Exemplo:
```
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
```

O ID é: `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`

## Passo 3: Configurar API do Google

### 3.1 Criar Projeto no Google Cloud

1. Acesse: https://console.cloud.google.com/
2. Clique em "Selecionar projeto" > "Novo projeto"
3. Nome: "Intranet Pedidos" (ou outro nome)
4. Clique em "Criar"

### 3.2 Ativar Google Sheets API

1. No menu lateral: "APIs e serviços" > "Biblioteca"
2. Pesquise: "Google Sheets API"
3. Clique na API e depois em "Ativar"

### 3.3 Criar Chave de API

1. Vá em "APIs e serviços" > "Credenciais"
2. Clique em "Criar credenciais" > "Chave de API"
3. Copie a chave gerada (guarde em local seguro)

## Passo 4: Configurar o Sistema

### 4.1 Editar o Script de Integração

Abra o arquivo `google_sheets_integration.py` e modifique:

```python
def get_google_sheets_data(sheet_id, range_name):
    # Substitua YOUR_API_KEY pela sua chave real
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}?key=SUA_CHAVE_API_AQUI"
    
    # ... resto do código permanece igual
```

### 4.2 Configurar IDs no Script Principal

No final do arquivo `google_sheets_integration.py`, substitua o exemplo:

```python
if __name__ == "__main__":
    # Substitua pelos seus dados reais
    SHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"  # Seu ID aqui
    RANGE_NAME = "Sheet1!A:I"  # Ajuste se sua aba tem nome diferente
    
    # Buscar dados reais da planilha
    clients_data = get_google_sheets_data(SHEET_ID, RANGE_NAME)
    
    if clients_data:
        create_json_data_file(clients_data, '/home/ubuntu/intranet-pedidos/clients_data.json')
        print("Dados reais carregados com sucesso!")
    else:
        print("Erro ao carregar dados da planilha")
```

## Passo 5: Testar a Integração

### 5.1 Teste Manual

Execute o script para testar:

```bash
cd /home/ubuntu/intranet-pedidos
python3 google_sheets_integration.py
```

Você deve ver: "Dados reais carregados com sucesso!"

### 5.2 Verificar Arquivo JSON

Verifique se o arquivo foi criado corretamente:

```bash
cat clients_data.json
```

Deve mostrar os dados dos seus clientes reais.

### 5.3 Testar no Site

1. Acesse o sistema: https://xxpxkpbe.manus.space/index_integrated.html
2. Digite o nome de um cliente real da sua planilha
3. Verifique se os dados aparecem corretamente

## Passo 6: Automatizar Atualizações

### 6.1 Configurar Script de Atualização

Edite o arquivo `update_data.sh`:

```bash
#!/bin/bash

# Configurações
SHEET_ID="1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"  # Seu ID
API_KEY="SUA_CHAVE_API_AQUI"  # Sua chave
PROJECT_DIR="/home/ubuntu/intranet-pedidos"

cd "$PROJECT_DIR"

# Executar script com dados reais
python3 google_sheets_integration.py

echo "Dados atualizados em $(date)"
```

### 6.2 Configurar Execução Automática

Para atualizar a cada 5 minutos:

```bash
# Editar crontab
crontab -e

# Adicionar linha:
*/5 * * * * /home/ubuntu/intranet-pedidos/update_data.sh >> /var/log/intranet-update.log 2>&1
```

## Passo 7: Gerenciar Novos Clientes

### 7.1 Fluxo Automático

Quando você adicionar um novo cliente na planilha:
1. O script de atualização vai detectar automaticamente
2. Em até 5 minutos, o cliente aparecerá na intranet
3. Status inicial será "Pedido em fase inicial"

### 7.2 Atualizar Status Manualmente

1. Acesse o sistema
2. Busque pelo cliente
3. Use o painel administrativo para atualizar o status
4. Cliente verá a atualização imediatamente

## Passo 8: Monitoramento

### 8.1 Verificar Logs

```bash
# Ver logs de atualização
tail -f /var/log/intranet-update.log

# Ver se há erros
grep -i error /var/log/intranet-update.log
```

### 8.2 Verificar Limites da API

O Google Sheets API tem limites gratuitos:
- 100 requisições por 100 segundos por usuário
- 500 requisições por 100 segundos

Para monitorar uso:
1. Acesse Google Cloud Console
2. Vá em "APIs e serviços" > "Quotas"
3. Monitore uso da Google Sheets API

## Solução de Problemas

### Erro 403: "API key not valid"

- Verifique se a chave de API está correta
- Confirme se a Google Sheets API está ativada
- Tente gerar uma nova chave de API

### Erro 404: "Spreadsheet not found"

- Verifique se o ID da planilha está correto
- Confirme se a planilha está pública
- Teste acessar a planilha pelo link

### Dados não aparecem

- Verifique se os nomes na planilha estão em minúsculas no sistema
- Confirme se não há espaços extras nos nomes
- Verifique se a estrutura da planilha está correta

### Atualizações não funcionam

- Verifique se o cron está rodando: `sudo service cron status`
- Teste o script manualmente
- Verifique permissões dos arquivos

## Backup e Segurança

### 8.1 Backup Regular

```bash
# Criar backup diário
0 2 * * * cp /home/ubuntu/intranet-pedidos/clients_data.json /backup/clients_data_$(date +\%Y\%m\%d).json
```

### 8.2 Segurança da API

- Nunca compartilhe sua chave de API
- Restrinja a chave apenas para Google Sheets API
- Monitore uso regularmente
- Regenere a chave se suspeitar de comprometimento

## Próximos Passos

Após configurar a integração real:
1. Teste com todos os clientes da planilha
2. Treine sua equipe para usar o painel administrativo
3. Compartilhe o link com os clientes
4. Configure monitoramento e alertas
5. Documente o processo para sua equipe

