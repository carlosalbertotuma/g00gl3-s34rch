# g00gl3-s34rch

Tool para pentest e ethical hacking, a ferramenta utiliza a KEY e duas CSE do google search para fazer pesquisas em determinandos dominios que podem ser configurados em cada CSE no proprio google, como o google so permite 10 requisições no terminal foi utilizado duas CSE uma para cada dominio de pesquisa, que no caso a primeira CSE ta configurada, para pesquisar no exploit-db e a outra no packetstormsecurity.

Com um loop trago 20 primeiros resultados da pesquisa em cada dominio(CSE).

Modifique esse ponto do script com sua key e seus CSE, nao esqueça de configurar no google CSE em cada um a pesquisa que deseja no caso um com exploit-db e outro com packetstormsecurity.

SUAKEY  seucodigo
SEUCODIGOCSE 1 e 2 


api_keys_and_ids = [
    {"API_KEY": 'SUAKEY', "CSE_ID": 'SEUCODIGOCSE1'},
    {"API_KEY": 'SUAKEY', "CSE_ID": 'SEUCODIGOCSE2'}



![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/52f0a8d2-f1eb-46ef-8fd6-8bea8b2fa523)

![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/d3873a68-5188-45f7-af79-9f93c693bed3)

![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/fd6bce2a-fe44-4145-9893-5679ec9c405f)

Você pode criar as CSE no console do google, https://programmablesearchengine.google.com/controlpanel/all

![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/0bb9c92b-bb00-4a43-a276-9ecbbca132ab)


qualquer nome, voce vai precisar do codigo da CSE, onde foi configurado somente o dominio que vou pesquisar.

![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/3fd01547-1699-4a56-942c-75934354c6f5)


Vai precisar criar uma API key no console do google

![image](https://github.com/carlosalbertotuma/g00gl3-s34rch/assets/13341724/1243bcba-1387-4a34-be46-1830fada0b78)

configurar no script a mesma API key para as duas CSE criadas.

