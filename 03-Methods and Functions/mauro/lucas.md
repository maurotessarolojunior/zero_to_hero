







Talvez, para incluir o 7, e qualquer número entre 6 e 9, você possa iniciar um while loop dentro do for loop ao esbarrar no 6, e só sair quando esbarrar no 9

---

Tudo depende de como vai ser aplicado: 

Se criar um while, ele vai ignorar o for e ficar iterando no while isolado. 

Então teu for loop não pode ser dos ITENS da lista, mas do 

for i in range(len(list))

que ai enquanto o while rodar, vc incrementa manualmente o "i" pra quando ele escapar do while

o for vai ler o que vai vir depois do 9, e não o valor errado

Com o break teu while tá funcionando como um if:

Ele entra no loop e quebra a cada iteração, aí escapa e volta pro for loop. Se usar o while com o continue dentro, tem que atualizar o  round dentro dele tbm