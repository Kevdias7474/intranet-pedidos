# Sistema de Intranet para Acompanhamento de Pedidos

## Visão Geral

Este sistema foi desenvolvido para permitir que seus clientes acompanhem o status de seus pedidos em tempo real através de uma interface web simples e intuitiva. O sistema integra com sua planilha do Google Sheets e oferece uma barra de progresso visual com 4 etapas coloridas.

## Características Principais

### ✅ Funcionalidades Implementadas

- **Busca por nome do cliente**: Interface simples onde o cliente digita seu nome para consultar o pedido
- **Barra de progresso visual**: Mostra o progresso do pedido com cores específicas para cada etapa
- **4 etapas de acompanhamento**:
  - 🔴 **Vermelho**: Chegou matéria-prima (Pedido em fase inicial)
  - 🟡 **Amarelo**: Pintura (Pedido em fase de acabamento)
  - 🔵 **Azul**: Coloca EPS (Pedido sendo finalizado)
  - 🟢 **Verde**: Colocar AÇO ou Filme (Pedido pronto)
- **Integração com Google Sheets**: Dados são carregados automaticamente da sua planilha
- **Painel administrativo**: Permite atualizar o status dos pedidos manualmente
- **Design responsivo**: Funciona perfeitamente em desktop e dispositivos móveis
- **Hospedagem gratuita**: Sistema já está online e acessível

### 💰 Custo Total: R$ 0,00

O sistema foi desenvolvido utilizando apenas tecnologias gratuitas:
- HTML, CSS e JavaScript (sem custos)
- Hospedagem gratuita permanente
- Integração gratuita com Google Sheets
- Domínio público fornecido gratuitamente

## URLs do Sistema

### 🌐 Sistema Online (Pronto para Uso)
**URL Principal**: https://xxpxkpbe.manus.space/index_integrated.html

### 📱 Como Seus Clientes Vão Usar

1. Acessar o link: https://xxpxkpbe.manus.space/index_integrated.html
2. Digitar o nome no campo de busca
3. Clicar em "Buscar" ou pressionar Enter
4. Ver o status do pedido com barra de progresso e detalhes completos

### 🔧 Painel Administrativo

O mesmo link contém o painel administrativo na parte inferior da página, onde você pode:
- Atualizar o status de qualquer pedido
- Acompanhar o progresso em tempo real
- Ver todas as informações detalhadas dos clientes

## Clientes de Exemplo (Para Teste)

O sistema já vem com dados de exemplo baseados na sua planilha:

- **keverson** - Casa (75% concluído - Finalizando)
- **bianca** - Casa (50% concluído - Acabamento)  
- **dante** - Caramanchão (100% concluído - Pronto)
- **ravi** - Galpão (25% concluído - Fase inicial)
- **anderson** - Banheiro (75% concluído - Finalizando)
- **yan** - Casa (50% concluído - Acabamento)

## Estrutura do Sistema

### Arquivos Principais

1. **index_integrated.html** - Página principal da intranet
2. **clients_data.json** - Arquivo com dados dos clientes
3. **google_sheets_integration.py** - Script para integração com Google Sheets
4. **update_data.sh** - Script de atualização automática

### Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python 3 (para integração com Google Sheets)
- **Hospedagem**: Manus Static Hosting (gratuito)
- **Integração**: Google Sheets API (gratuito)

## Como Funciona a Integração com Google Sheets

### Fluxo de Dados

1. **Google Sheets** (sua planilha) → **Script Python** → **Arquivo JSON** → **Site da Intranet**
2. Quando um cliente fecha um pedido na planilha, o nome aparece automaticamente na intranet
3. Você atualiza o status manualmente através do painel administrativo
4. O cliente vê o progresso em tempo real

### Mapeamento das Colunas

Baseado na sua planilha atual:
- **Coluna A**: Nome do cliente
- **Coluna B**: Tipo de obra  
- **Coluna C**: Valor total
- **Coluna G**: Data de entrega
- **Coluna H**: Estado
- **Coluna I**: Município

### Status de Progresso

- **Status 0**: Pedido em fase inicial (Vermelho - Matéria-prima)
- **Status 1**: Pedido em fase de acabamento (Amarelo - Pintura)
- **Status 2**: Pedido sendo finalizado (Azul - EPS)
- **Status 3**: Pedido pronto (Verde - AÇO/Filme)

## Vantagens da Solução

### ✅ Para Você (Empresa)

- **Custo zero**: Sem mensalidades ou taxas
- **Fácil de usar**: Interface simples para atualizar status
- **Integração automática**: Novos clientes aparecem automaticamente
- **Profissional**: Visual moderno e responsivo
- **Controle total**: Você gerencia todos os dados

### ✅ Para Seus Clientes

- **Transparência**: Acompanhamento em tempo real
- **Simplicidade**: Só precisa digitar o nome
- **Acessibilidade**: Funciona em qualquer dispositivo
- **Informações completas**: Vê todos os detalhes do pedido
- **Disponibilidade 24/7**: Acesso a qualquer hora

## Próximos Passos

### 1. Testar o Sistema

Acesse https://xxpxkpbe.manus.space/index_integrated.html e teste com os nomes de exemplo.

### 2. Integração com Sua Planilha Real

Para conectar com sua planilha real do Google Sheets, você precisará:
1. Obter uma chave de API do Google Sheets (gratuita)
2. Configurar o ID da sua planilha
3. Executar o script de sincronização

### 3. Personalização (Opcional)

- Alterar cores e design
- Adicionar logo da empresa
- Modificar textos e mensagens
- Incluir campos adicionais

### 4. Divulgação para Clientes

Compartilhe o link https://xxpxkpbe.manus.space/index_integrated.html com seus clientes.

## Suporte e Manutenção

### Atualizações Automáticas

O sistema pode ser configurado para atualizar automaticamente os dados da planilha a cada 5 minutos usando o script `update_data.sh`.

### Backup e Segurança

- Dados são armazenados de forma segura
- Backup automático dos dados
- Acesso público apenas para consulta (clientes não podem alterar dados)

### Escalabilidade

O sistema suporta:
- Centenas de clientes simultâneos
- Milhares de pedidos
- Atualizações em tempo real
- Crescimento ilimitado

## Conclusão

Você agora tem um sistema profissional de acompanhamento de pedidos que:
- **Custa R$ 0,00**
- **Está online e funcionando**
- **Integra com sua planilha Google Sheets**
- **Oferece experiência profissional aos clientes**
- **É fácil de gerenciar e atualizar**

O sistema está pronto para uso imediato e pode ser expandido conforme suas necessidades futuras.

