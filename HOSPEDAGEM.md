# Guia de Hospedagem Gratuita

## Opções de Hospedagem Gratuita

Este guia apresenta as melhores opções gratuitas para hospedar seu sistema de intranet.

## Opção 1: GitHub Pages (Recomendado)

### ✅ Vantagens
- 100% gratuito
- Fácil de usar
- Atualizações automáticas
- Domínio personalizado gratuito
- SSL incluído

### 📋 Passo a Passo

#### 1.1 Criar Conta no GitHub
1. Acesse: https://github.com
2. Clique em "Sign up"
3. Crie sua conta gratuita

#### 1.2 Criar Repositório
1. Clique em "New repository"
2. Nome: `intranet-pedidos`
3. Marque "Public"
4. Marque "Add a README file"
5. Clique em "Create repository"

#### 1.3 Upload dos Arquivos
1. Clique em "uploading an existing file"
2. Arraste todos os arquivos do sistema:
   - `index_integrated.html`
   - `clients_data.json`
   - `google_sheets_integration.py`
   - `update_data.sh`
   - Arquivos de documentação
3. Commit: "Adicionar sistema de intranet"

#### 1.4 Ativar GitHub Pages
1. Vá em "Settings" do repositório
2. Role até "Pages"
3. Source: "Deploy from a branch"
4. Branch: "main"
5. Folder: "/ (root)"
6. Clique em "Save"

#### 1.5 Acessar o Site
Após alguns minutos, acesse:
`https://seuusuario.github.io/intranet-pedidos/index_integrated.html`

## Opção 2: Netlify

### ✅ Vantagens
- Deploy automático
- Domínio personalizado
- SSL gratuito
- CDN global
- Formulários gratuitos

### 📋 Passo a Passo

#### 2.1 Criar Conta
1. Acesse: https://netlify.com
2. Clique em "Sign up"
3. Use conta do GitHub (recomendado)

#### 2.2 Deploy Manual
1. Clique em "Sites"
2. Arraste a pasta do projeto para a área de upload
3. Site será publicado automaticamente

#### 2.3 Deploy Automático (GitHub)
1. Clique em "New site from Git"
2. Conecte com GitHub
3. Selecione o repositório `intranet-pedidos`
4. Deploy automático configurado

#### 2.4 Configurar Domínio
1. Vá em "Site settings"
2. "Change site name"
3. Escolha um nome: `intranet-pedidos-suaempresa`
4. Acesse: `https://intranet-pedidos-suaempresa.netlify.app`

## Opção 3: Vercel

### ✅ Vantagens
- Deploy instantâneo
- Performance otimizada
- Domínio personalizado
- SSL automático
- Analytics gratuito

### 📋 Passo a Passo

#### 3.1 Criar Conta
1. Acesse: https://vercel.com
2. Clique em "Sign up"
3. Use conta do GitHub

#### 3.2 Importar Projeto
1. Clique em "New Project"
2. Importe do GitHub
3. Selecione `intranet-pedidos`
4. Clique em "Deploy"

#### 3.3 Configurar
- Framework Preset: "Other"
- Root Directory: "./"
- Build Command: (deixe vazio)
- Output Directory: "./"

## Opção 4: Firebase Hosting

### ✅ Vantagens
- Google Cloud Platform
- SSL gratuito
- CDN global
- Integração com outros serviços Google

### 📋 Passo a Passo

#### 4.1 Instalar Firebase CLI
```bash
npm install -g firebase-tools
```

#### 4.2 Login e Inicializar
```bash
firebase login
firebase init hosting
```

#### 4.3 Configurar
- Selecione projeto existente ou crie novo
- Public directory: "."
- Single-page app: "No"
- Overwrite index.html: "No"

#### 4.4 Deploy
```bash
firebase deploy
```

## Opção 5: Surge.sh

### ✅ Vantagens
- Deploy via linha de comando
- Domínio personalizado
- SSL gratuito
- Muito simples

### 📋 Passo a Passo

#### 5.1 Instalar Surge
```bash
npm install -g surge
```

#### 5.2 Deploy
```bash
cd /caminho/para/intranet-pedidos
surge
```

#### 5.3 Configurar
- Email: seu email
- Password: criar senha
- Domain: escolher domínio (ex: intranet-pedidos.surge.sh)

## Comparação das Opções

| Serviço | Facilidade | Performance | Domínio Personalizado | SSL | CDN |
|---------|------------|-------------|----------------------|-----|-----|
| GitHub Pages | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ✅ | ❌ |
| Netlify | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ✅ |
| Vercel | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ✅ |
| Firebase | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ✅ |
| Surge | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | ❌ |

## Configuração de Domínio Personalizado

### Para GitHub Pages

1. Compre um domínio (ex: GoDaddy, Namecheap)
2. No repositório, vá em Settings > Pages
3. Custom domain: `intranet.suaempresa.com`
4. Configure DNS:
   ```
   Type: CNAME
   Name: intranet
   Value: seuusuario.github.io
   ```

### Para Netlify

1. Vá em Site settings > Domain management
2. Add custom domain: `intranet.suaempresa.com`
3. Configure DNS conforme instruções

### Para Vercel

1. Vá em Project settings > Domains
2. Add domain: `intranet.suaempresa.com`
3. Configure DNS conforme instruções

## Configuração de SSL

Todos os serviços mencionados oferecem SSL gratuito via Let's Encrypt:
- **GitHub Pages**: Automático
- **Netlify**: Automático
- **Vercel**: Automático
- **Firebase**: Automático
- **Surge**: Automático

## Atualizações Automáticas

### GitHub Pages + GitHub Actions

Crie `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Update data
      run: |
        python3 google_sheets_integration.py
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./
```

### Netlify + GitHub

- Deploy automático a cada push
- Build command: `python3 google_sheets_integration.py`
- Publish directory: `./`

## Monitoramento

### Analytics Gratuitos

1. **Google Analytics**
   - Adicione código de tracking
   - Monitore visitantes e uso

2. **Netlify Analytics**
   - Incluído gratuitamente
   - Dados de servidor

3. **Vercel Analytics**
   - Plano gratuito disponível
   - Performance insights

### Uptime Monitoring

1. **UptimeRobot** (gratuito)
   - Monitora até 50 sites
   - Alertas por email

2. **StatusCake** (gratuito)
   - Monitoramento básico
   - Alertas por email

## Backup e Recuperação

### Backup Automático

```bash
# Script de backup diário
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup/intranet-$DATE"

mkdir -p $BACKUP_DIR
cp -r /caminho/para/intranet-pedidos/* $BACKUP_DIR/

# Upload para Google Drive (opcional)
rclone copy $BACKUP_DIR gdrive:backups/intranet/
```

### Recuperação

1. **GitHub**: Histórico completo no repositório
2. **Netlify**: Deploy rollback com 1 clique
3. **Vercel**: Rollback para deploy anterior
4. **Firebase**: Versões anteriores disponíveis

## Custos e Limites

### GitHub Pages
- **Gratuito**: Repositórios públicos ilimitados
- **Limite**: 1GB de armazenamento, 100GB bandwidth/mês
- **Pago**: GitHub Pro ($4/mês) para repositórios privados

### Netlify
- **Gratuito**: 100GB bandwidth/mês, 300 build minutes/mês
- **Pago**: Pro ($19/mês) para mais recursos

### Vercel
- **Gratuito**: 100GB bandwidth/mês, 6000 build minutes/mês
- **Pago**: Pro ($20/mês) para mais recursos

### Firebase
- **Gratuito**: 1GB armazenamento, 10GB bandwidth/mês
- **Pago**: Pay-as-you-go após limites

## Recomendação Final

**Para iniciantes**: GitHub Pages
- Mais simples de configurar
- Integração direta com código
- Gratuito e confiável

**Para profissionais**: Netlify
- Melhor performance
- Mais recursos
- Deploy automático avançado

**Para alta performance**: Vercel
- Otimização automática
- CDN global
- Analytics incluído

Escolha a opção que melhor se adapta ao seu nível técnico e necessidades!

