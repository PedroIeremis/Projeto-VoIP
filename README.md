## Provisionamento de AGI em Python para VoIP

Para obter o repositório localmente:

```shell
git clone https://github.com/PedroIeremis/AGI-VoIP.git
```

Acesse-o:
```shell
cd AGI-VoIP
```

 E caso tenha o VsCode, use o comando abaixo para abrir a pasta direto no VsCode:
 ```shell
code .
```

---

Este projeto foi desenvolvido durante a disciplina de VoIP, na Graduação em Redes de Computadores no IFRN - Central. 

Partindo do pressuposto que você terá um servidor VoIP com Asterisk, será possível implementar este projeto, com certos ajustes de ramais e possíveis adaptações. É necessário que o SO seja __Linux__, ter __Python__ atualizado e __Docker__ para uma das funcionalidades da AGI.

---
Basicamente temos as seguintes funcionalidades provisionadas por meio da AGI:

- Buscar informações de Localização a partir de CEP
- Subir e Derrubar Serviço Web, provisionado por meio de IaC, com Docker

Para isso, serão utilizados Scripts, comandos e a própria AGI.