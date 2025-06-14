#!/bin/bash

# Script para atualizar dados da intranet a partir do Google Sheets
# Este script deve ser executado periodicamente (ex: a cada 5 minutos)

echo "Iniciando atualização dos dados da intranet..."

# Diretório do projeto
PROJECT_DIR="/home/ubuntu/intranet-pedidos"

# Navegar para o diretório do projeto
cd "$PROJECT_DIR"

# Executar o script Python para buscar dados atualizados
python3 google_sheets_integration.py

# Verificar se o arquivo foi criado com sucesso
if [ -f "clients_data.json" ]; then
    echo "Dados atualizados com sucesso em $(date)"
    
    # Opcional: fazer backup do arquivo anterior
    if [ -f "clients_data_backup.json" ]; then
        rm clients_data_backup.json
    fi
    
    # Criar backup
    cp clients_data.json clients_data_backup.json
    
    echo "Backup criado: clients_data_backup.json"
else
    echo "Erro: Arquivo de dados não foi criado"
    exit 1
fi

echo "Atualização concluída!"

