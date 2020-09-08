# vxtel_backend

## __Estrutura__
O projeto é baseado na framework de aplicação na web Django e segue sua estrutura e configurações padrão. Ou seja, o projeto e dividido no programa principal __Vxtel__, na aplicação __FaleMais__ e no gerenciador __manage.py__.

### __Vxtel__
Esse diretorio guarda as configurações principais que mantem a integridade do Django. Sendo assim, apenas o arquivo urls.py foi modificado para corresponder à views da aplicação __FaleMais__

### __FaleMais__
Esse diretorio comports toda a estrutura da apicação propriamente dita, sendo dividida em:
 * models.py: comporta os modelos de armazenamento de informacoes como Ligacao e Tarifa que são utilizados nas operações lógicas
 * form.py: armazena os formularios utilizados para coletar informação provida pelo usuario.
 * views.py: funcoes chamadas por urls na web que apresentam os templates em html e fazem o processamento lógico mais raso.
 * tests.py: comportam classes de testes, no caso utilizando unittest do django e lib selenium, que são lançados através de comandos ao __manage.py__.
 * admin.py: registra models utilizados para armazenamento fixo de dados.
Os outros arquivos e pastas servem como armazenamento de arquivos como templates ou foram setandos automaticamento pelo django.

### __manage.py__
Gerenciador de atividades que são acessadas pelo terminal:
 * python ./manage.py test FaleMais.tests.TestUser.test_method: acessa a classe TestUser e realiza o método de teste indicado
 * python ./manage.py makemigrations: computa as mudanças feitas na estrutura do programa(models por exemplo)
 * python ./manage.py migrate: aplica as mudanças computadas
 * python ./manage.py runserver: lança o server na web
 
## Considerações
  Dentro do arquivos tests em __FaleMais__, nao realize os testes através de Run direto na IDE, as configurações foram feitas para só funcionarem utilizando o __manage.py__. Assim o servidor é lançado automaticamente na rede e desligado após os testes.

  Alguns testes em relação ao preenchimento incorreto de formularios nao foram realizados devido à impedimentos automaticos realizados pelo Django ao defini-los.
  * Inserir letras no espaço de tempo: models.FloatField impede inserir caracteres não numéricos.
  * Inserir DDDs com mais, menos números ou indisponiveis: models.CharField com widget de escolhas.
  * Inserir um tempo muito grande: delimitado pelo models.FloatField.

