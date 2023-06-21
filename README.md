Aqui está um script de exemplo em Python 3 que demonstra um ataque de XSS refletido protegido pela política de segurança de conteúdo (CSP) 
com um ataque de tag pendente:

Neste script, definimos a variável target_url para a URL do aplicativo vulnerável. Definimos dois payloads: payload para o ataque XSS refletido
 e dangling_tag para o ataque dangling tag. 
Em seguida, definimos os cabeçalhos necessários para contornar a proteção CSP usando o dicionário de cabeçalhos.

Em seguida, construímos os dados de carga útil combinando a carga XSS e o ataque de tag pendente. 
Enviamos uma solicitação POST para a URL de destino com os dados de carga útil e os cabeçalhos personalizados. 
Por fim, verificamos a resposta para determinar se o ataque foi bem-sucedido.

AVISO IMPORTANTE:
Observe que a realização de tais ataques é ilegal e antiética, a menos que você tenha permissão explícita do alvo
e o esteja usando para fins educacionais ou de teste de segurança. 
Certifique-se sempre de cumprir as diretrizes legais e éticas ao testar vulnerabilidades.
