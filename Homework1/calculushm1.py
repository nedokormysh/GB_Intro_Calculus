# -*- coding: utf-8 -*-
"""CalculusHM1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8XpRCasKoTssHVqhCORZOgP9TuPAtgc

__1.__ Представьте в виде __несократимой__ рациональной дроби:

### $$а)\,\,\, 0.(216);$$

### $$б)\,\,\, 1.0(01).$$

a)
$$a=0.(216)$$
$$1000a=216.(216)$$
$$1000a=216+0.(216)$$
$$1000a=216+a$$
$$999a=216$$
$$a=\frac{216}{999}=\frac{24}{111}$$
$$0.(216)=\frac{24}{111}$$
$$0.(216)=\frac{8}{37}$$
"""

print (8/37)

"""
б)
$$a=0.(01)$$
$$100a=01.(01)$$
$$100a=1+0.(01)$$
$$100a=1+a$$
$$99a=1$$
$$a=\frac{1}{99}$$
$$b=1.0(01)$$
$$10b=10.(01)$$
$$10b=10+0.(01)$$
$$10b=10+\frac{1}{99}$$
$$10b=\frac{991}{99}$$
$$b=\frac{991}{990}$$"""

print(991/990)

"""__2*.__ Пусть $x =\frac{2}{21}$. Известно, что для некоторого натурального $k$ число $x$ записывается в $k$ - ичной системе счисления как $0.(13)_k = 0, 131313..._k$. Найдите $k$.

$$x=\frac{2}{21}$$
$$x=0.(13)_k$$


$$k^2x=13.(13)_k$$
$$k^2x=13_k+0.(13)_k$$
$$k^2x=13_k+x$$
$$k^2x-x=13_k$$
$$(k^2-1)x=13_k$$
$$x=\frac{13_k}{k^2-1}$$
$$x=\frac{1\cdot k^1+3\cdot k^0}{k^2-1}$$
$$x=\frac{k+3}{k^2-1}$$
$$\frac{2}{21}=\frac{k+3}{k^2-1}$$
$$2k^2-2=21k+63$$
$$2k^2-21k-65=0$$
$$k_1=-2.5$$
$$k_2=13$$

Ответ: k = 13

__3.__ Проверьте любым способ, является ли данные логические формулы тавтологией:

### $$a)\,\,\, (A \vee B) \rightarrow (B \vee\overline A)$$
### $$б)\,\,\, A \rightarrow (A \vee (\overline B \wedge A))$$

### $$a)\,\,\, (A \vee B) \rightarrow (B \vee\overline A)$$

<table>
<thead>
<tr><th>$A$</th><th>$B$</th><th>$(A \vee B)$</th><th>$\overline A$</th><th>$B \vee\overline A$</th><th>$(A \vee B) \rightarrow (B \vee\overline A)$</th></tr>
</thead>
<tbody>
    <tr><td>$0$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr>
    <tr><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr>
    <tr><td>$1$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr>
    <tr><td>$1$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1$</td></tr>
</tbody>
</table>


Не тавтология


### $$б)\,\,\, A \rightarrow (A \vee (\overline B \wedge A))$$

$$\ A\rightarrow (A \vee (\overline B \wedge A))=$$
$$\ A\rightarrow (A \vee \overline B) \wedge (A \vee A)=$$
$$\ A\rightarrow (A \vee \overline B) \wedge A=$$
$$\ A\rightarrow A \wedge (A \vee \overline B)=$$
$$\ A\rightarrow A$$

Тавтология

__4.__ Сформулируйте словесно высказывания:
### $$a)\,\,\, (\overline A \vee B) \rightarrow \overline C$$
### $$б)\,\,\, C \rightarrow (A \vee \overline B)$$

- $A:\,\,\,$ сегодня светит солнце; 
- $B:\,\,\,$ сегодня сыро; 
- $C:\,\,\,$ я поеду на дачу.

### $$a)\,\,\, (\overline A \vee B) \rightarrow \overline C$$

$ \overline A $ =  сегодня не светит солнце; 
$ \overline C $ = я не поеду на дачу

Если сегодня не светит солнце или сегодня сыро, то я не поеду на дачу

### $$б)\,\,\, C \rightarrow (A \vee \overline B)$$

$ \overline B $ = сегодня сухо

Если я поеду на дачу, то сегодня светит солнце или сегодня сухо

5. Пользуясь правилом построения противоположного высказывания, запишите утверждения, противоположные следующим:

a) На любом курсе каждого факультета есть студенты, сдающие все экзамены на «отлично».

б) В любом самолете на рейсе Вашингтон-Москва присутствует хотя бы один сотрудник силовых органов, в каждой пуговице одежды которого вмонтирован микрофон.

a) На любом курсе каждого факультета есть студенты, сдающие все экзамены на «отлично».


$\forall$ курсе $\forall$ факультета $\exists$ студенты, сдающие $\forall$ экзамены на «отлично».

$\exists$ курс $\exists$ факультет, на котором $\forall$ студенты, не сдающие экзамены на "отлично".


Существуют курсы на каких-либо факультетах, на которых любой студент не сдаёт экзамен на "отлично".


б) В любом самолете на рейсе Вашингтон-Москва присутствует хотя бы один сотрудник силовых органов, в каждой пуговице одежды которого вмонтирован микрофон.


$\forall$ самолете на рейсе Вашингтон-Москва $\exists$ сотрудник силовых органов, в $\forall$ пуговице одежды которого вмонтирован микрофон.

$\exists$ самолёт на рейсе Вашингтон-Москва, где у $\forall$ сотрудника силовых органов, присутствующего на этом рейсе, $\exists$ пуговицы на одежде, в которые не вмонтирован микрофон.

Существует самолёт на рейсе Вашингтон-Москва, где у любого сотрудника силовых органов, присутствующего на этом рейсе, существуют пуговицы на одежде, в которые не вмонтирован микрофон.

__6*.__ Прочитайте высказывания, установите их истинность и постройте противоположное высказывание:

### $$a)\,\,\, \forall x\in\mathbb{R}\,\,\,\exists X\in\mathbb{R}:\,\,\, X>x;$$
### $$б)\,\,\, \forall y\in\Bigl[0; \frac{\pi}{2}\Bigr]\,\,\,\exists \varepsilon>0:\,\,\, \sin y<\sin(y+\varepsilon);$$
### $$в)\,\,\, \forall y\in\Bigl[0; \pi\Bigr)\,\,\,\exists \varepsilon>0:\,\,\, \cos y>\cos(y+\varepsilon).$$

### $$a)\,\,\, \forall x\in\mathbb{R}\,\,\,\exists X\in\mathbb{R}:\,\,\, X>x;$$

Для любого вещественного x сущесвует вещественное число X большое, такое что, X большое больше x.
Истинно.

Противоположное: $$\exists x\in\mathbb{R}\,\,\,\forall X\in\mathbb{R}:\,\,\, X<x;$$

### $$б)\,\,\, \forall y\in\Bigl[0; \frac{\pi}{2}\Bigr]\,\,\,\exists \varepsilon>0:\,\,\, \sin y<\sin(y+\varepsilon);$$

Для любых y, принадлежащих диапазону от нуля до Pi пополам, включая обе границы, существует эпсилон больше нуля, так что sin(y) меньше sin(y + e). Ложно, т.к. включена граница Pi/2. sin(pi/2) = 1, следовательно высказывание ложно.

Противоположное:$$\exists y\in\Bigl[0; \frac{\pi}{2}\Bigr]\,\,\,\forall \varepsilon>0:\,\,\, \sin y>\sin(y+\varepsilon)$$

### $$в)\,\,\, \forall y\in\Bigl[0; \pi\Bigr)\,\,\,\exists \varepsilon>0:\,\,\, \cos y>\cos(y+\varepsilon).$$

Для любого y, принадлежащего диапазону от нуля включительно до Pi(не включая), существует эпсилон больше нуля, такое что cos(y) больше cos(y + e). Истинно.

Противоположное:$$\exists y\in\Bigl[0; \pi\Bigr)\,\,\,\forall \varepsilon>0:\,\,\, \cos y<\cos(y+\varepsilon).$$
"""