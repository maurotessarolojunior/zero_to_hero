---
O que configura um numero primo: apenas divisível por um e por ele mesmo.
Vou receber um número inteiro >  1. 
O primeiro numero a ser testado é o 2 pois por definição nem 0 nem o nº 1 são primos.
---
Num primeiro loop varro os numeros de 2 até o numero que entra na função. 
  Num loop interno avalio o resto da divisao entre o numero atual do loop externo e varios numeros inteiros começando em 2 até o (numero atual/2). 

    Se o resto for diferente de 0 em todos 0s divisores (vou precisar de uma variável de controle pra isso: check) o numero atual do loop externo é primo: primes +=1 
 
retorna primes
---