Para rodar o programa siga estes passos:

1. Baixe o docker pelo site [docker](https://www.docker.com/)
2. Abra o aplicativo do docker
3. Copie este repositório
4. Entre na pasta "ecormecce"
5. Para gerar uma imagem de cada pasta, entre nas pastas e siga estes passos
```bash
docker build -t <nome-da-minha-imagem> .

```
5.1. No seu terminal, entre na pasta catalogoCompra ou nas outras e rode o comando acima. Substitua <nome-da-minha-imagem> por um nome do seu agrado para a imagem
5.2. Repita isso para as outras pastas
5.3. Para saber se a imagem foi  gerada execute o comando 
```bash
docker images
```
No seu terminal deve aparecer isto:
<img width="770" height="213" alt="image" src="https://github.com/user-attachments/assets/3eeaf0af-3f8f-4f16-b276-32fa89b9ec7d" />

6. Agora devemos criar uma rede para o serviço
6.1. Execute este comando:
```bash
docker network create <nome-da-rede>
```
**observação**:Não precisa estar em uma dessas pastas para executar este comando, ele pode ser feito fora das pastas
6.2. Para ver sua rede execute: 
```bash 
  docker network ls
```

7. Para executar as imagens e formar um container e rodar, execute estes passos
7.1. Para criar o container de cada imagem, execute estes comandos mudando apenas o nome da imagem de cada pasta
```bash
docker run -d -p <numero da porta, por exemplo 5001:5001> --network nome-da-rede --name nome-do-conteiner
nome-da-minha-imagem
```

exemplo:
<img width="753" height="52" alt="image" src="https://github.com/user-attachments/assets/785a1eae-b537-48cb-a035-70a02d26bc74" />

Feito isso para cada imagem
vá o link
[Local host](http://localhost:5000/comprar/Proteina/user1)
