Ambiente virtual

```
> conda create -n "nome_que_voce_quiser" python=3.12
> conda activate "nome_que_voce_escolheu"
> pip install django
> django admin startproject "nome_desejado" .(O ponto e para ele soltar os arquivos dentro da pasta que voce esta)

-Ambiente criado
```
Configurar o git
```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

#configure o gitignore
git init
git add .
git commit -m 'Mensagens'
git remote add origin https://github.com/NatanCristhoffe/agenda-project.git

uma vez que voce tiver dado o comando anterior add origin com a sua url_do_git voce nao precisa utilizalo mais, caso altere algum arquivo e so fazer os seguinter comandos:
git add .
git commit -m 'nome do commit'
git log ou git log --oneline
git push origin main -u(Esse comando que manda os seus arquivos para o repositorio do GitHub)
a primeira vez utilizamos o comando com um -U no final para o git setar o origin main como padrao e entao so precisamos dar um git push da proxima vez
```