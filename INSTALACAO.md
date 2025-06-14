# Guia de Instalação e Configuração

## Pré-requisitos

- Conta no Google (para Google Sheets)
- Planilha no Google Sheets com os dados dos clientes
- Conhecimento básico de computador

## Passo 1: Configurar Google Sheets API

### 1.1 Criar Projeto no Google Cloud Console

1. Acesse: https://console.cloud.google.com/
2. Clique em "Criar Projeto"
3. Dê um nome ao projeto (ex: "Intranet Pedidos")
4. Clique em "Criar"

### 1.2 Ativar Google Sheets API

1. No menu lateral, vá em "APIs e Serviços" > "Biblioteca"
2. Pesquise por "Google Sheets API"
3. Clique na API e depois em "Ativar"

### 1.3 Criar Credenciais

1. Vá em "APIs e Serviços" > "Credenciais"
2. Clique em "Criar Credenciais" > "Chave de API"
3. Copie a chave gerada (você vai precisar dela)

### 1.4 Configurar Permissões da Planilha

1. Abra sua planilha no Google Sheets
2. Clique em "Compartilhar"
3. Em "Obter link", escolha "Qualquer pessoa com o link pode visualizar"
4. Copie o ID da planilha (parte da URL entre `/d/` e `/edit`)

## Passo 2: Configurar o Sistema

### 2.1 Editar o Script Python

Abra o arquivo `google_sheets_integration.py` e modifique:

```python
# Substitua estas variáveis:
SHEET_ID = "SEU_ID_DA_PLANILHA_AQUI"
API_KEY = "SUA_CHAVE_API_AQUI"
RANGE_NAME = "Sheet1!A:I"  # Ajuste conforme sua planilha
```

### 2.2 Testar a Integração

Execute o script para testar:

```bash
python3 google_sheets_integration.py
```

Se funcionar, você verá: "Arquivo de dados criado com sucesso!"

## Passo 3: Configurar Atualização Automática

### 3.1 Configurar Cron (Linux/Mac)

Para atualizar os dados a cada 5 minutos:

```bash
# Abrir editor de cron
crontab -e

# Adicionar esta linha:
*/5 * * * * /caminho/para/update_data.sh
```

### 3.2 Configurar Tarefa Agendada (Windows)

1. Abrir "Agendador de Tarefas"
2. Criar tarefa básica
3. Configurar para executar `update_data.sh` a cada 5 minutos

## Passo 4: Hospedagem

### Opção 1: GitHub Pages (Gratuito)

1. Criar conta no GitHub
2. Criar repositório público
3. Fazer upload dos arquivos
4. Ativar GitHub Pages nas configurações
5. Acessar via: `https://seuusuario.github.io/nome-repositorio`

### Opção 2: Netlify (Gratuito)

1. Criar conta no Netlify
2. Conectar com GitHub ou fazer upload direto
3. Deploy automático
4. Domínio gratuito fornecido

### Opção 3: Vercel (Gratuito)

1. Criar conta no Vercel
2. Importar projeto do GitHub
3. Deploy automático
4. Domínio gratuito fornecido

## Passo 5: Personalização

### 5.1 Alterar Cores

No arquivo `index_integrated.html`, procure por:

```css
/* Cores das etapas */
.status-inicial { background: #f8d7da; }    /* Vermelho */
.status-acabamento { background: #fff3cd; } /* Amarelo */
.status-finalizando { background: #cce7ff; } /* Azul */
.status-pronto { background: #d1ecf1; }     /* Verde */
```

### 5.2 Adicionar Logo

Adicione sua logo no cabeçalho:

```html
<div class="header">
    <img src="logo.png" alt="Logo" style="height: 50px; margin-bottom: 10px;">
    <h1>Acompanhamento de Pedidos</h1>
</div>
```

### 5.3 Personalizar Textos

Modifique os textos conforme sua necessidade:
- Título da página
- Mensagens de status
- Placeholders dos campos
- Textos explicativos

## Passo 6: Teste Final

1. Acesse o sistema hospedado
2. Teste com nomes reais da sua planilha
3. Verifique se os dados estão corretos
4. Teste a atualização de status
5. Verifique responsividade no celular

## Solução de Problemas

### Erro: "Cliente não encontrado"

- Verifique se o nome está exatamente igual na planilha
- Confirme se a integração com Google Sheets está funcionando
- Verifique se o arquivo `clients_data.json` foi criado

### Erro: "Falha ao carregar dados"

- Verifique a chave da API
- Confirme se a planilha está pública
- Teste a conexão com a internet

### Dados não atualizam

- Verifique se o script de atualização está rodando
- Confirme se o cron/tarefa agendada está ativo
- Teste manualmente o script `update_data.sh`

## Manutenção

### Backup Regular

- Faça backup do arquivo `clients_data.json`
- Mantenha cópia dos arquivos de configuração
- Documente alterações feitas

### Monitoramento

- Verifique logs de erro regularmente
- Monitore uso de API (Google tem limites gratuitos)
- Acompanhe feedback dos clientes

### Atualizações

- Mantenha o sistema atualizado
- Teste mudanças em ambiente separado
- Documente novas funcionalidades

## Suporte

Para dúvidas ou problemas:
1. Consulte esta documentação
2. Verifique os logs de erro
3. Teste cada componente separadamente
4. Documente o problema para facilitar o suporte

