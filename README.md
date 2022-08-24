# Teste_InPeace

<p>PASSO A PASSO</p>

1º - Para iniciar o projeto foi necesssário realizar a integração do Python com o MySql . Para isso eu criei um novo banco de dados chamado "teste" com as tabelas "info_igreja" e "info_membro" com as informações pedidas. Para a conexão ser realizada eu passei como parâmetro o "host", "user", "password" e "database" para relacionar o Python com o que foi criado com o MySql. Para executar os comandos da minha conexão foi criado a variável "cursor". 

2º - Para inserir um conteúdo no banco de dados foi criada a variável "comando" que armazena nas tabelas as informações passadas pelo usuário (input) e logo depois o cursor executa esse comando passando as informações para o banco de dados.

3º - Para listar os membros cadastrados eu utilizei um comando que seleciona todo o conteudo da tabela e guardei as informações em uma variável chamada "visualizador". O conteudo vem atráves de uma lista de tupla, então eu percorri essa lista e printei as informações.

4º - Para editar eu utilizei a mesma variável citada acima. Em Python não é possível modificar um tupla, então eu criei uma lista vazia e armazenei todo o conteudo através de uma lista de lista. Com essa nova lista eu fiz comparações verificando se o CPF digitado pelo usuário existe dentro do banco de dados para que a edição possa ser realizada. Se o CPF digitado existir eu busco o id e faço um update em todas as informações contidas ali.

5º - Para deletar eu também verifico se o CPF digitado existe e se ele existir eu verifico a qual id essa informação está contida e através do cursor eu deleto todas o conteudo pertencente a esse CPF.  

<p>OBSERVAÇÃO</p>

Muito dos requisitos pedidos eu não pude cumprir, pois como foi dito na entrevista eu nunca tive contato com FrontEnd nem banco de dados, Então tudo que eu executei com MySql eu aprendi no período em que o teste esteve aberto. Também nunca realizei um projeto utilizando uma framework. Mas caso a empresa decida me contratar, eu estou totalmente aberto a aprender todos  os conhecimentos necessários para ajudar a equipe. Agradeço a Oportunidade!!!!
