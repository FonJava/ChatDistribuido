Aplicação: Sistema de chat distribuído.

Integrantes: Anthony Guerra, Geraldo Gonçalves e Paulo Romero.

Requisitos: 

Autenticação de usuários.
Envio e recebimento de mensagens em tempo real.
Suporte a salas de chat.
Listagem de usuários online.


Módulos: 

4 Módulos em Python (usando Flask):

Módulo de Autenticação e Autorização (Backend): Implementa o login, autenticação e autorização de usuários.
Módulo de Gerenciamento de Salas (Backend): Permite criar, listar e remover salas de chat.
Módulo de Mensagens em Tempo Real (Backend): Utiliza WebSockets para comunicação em tempo real. Gerencia envio e recebimento de mensagens.
Interface Gráfica (Frontend): Desenvolve uma interface amigável para os usuários. Utiliza bibliotecas como Flask-SocketIO para interação em tempo real.


2 Módulos em Linguagens Diferentes:

Módulo de Estatísticas de Uso (Java - Spring Boot): Rastreia o uso das salas e usuários online. Fornece dados para análise.
Módulo de Notificações por E-mail (Node.js): Envia notificações por e-mail para usuários. Pode notificar sobre novas mensagens.
