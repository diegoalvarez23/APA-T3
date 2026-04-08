# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Nom i Cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Diego Alvarez Tome
## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

(resultado_test.png)

#### Código desarrollado


```python
'''
Nom i cognoms: Diego Alvarez Tome
TASCA 3: APA CURS 2025 - 2026

Classe per a la gestió de vectors.

Tests unitaris:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])

>>> v1 * v2
Vector([4, 10, 18])

>>> v1 @ v2
32

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
'''


class Vector:
    '''
    Classe que representa un vector com una seqüència ordenada de components.
    '''

    def __init__(self, iterable):
        '''
        Constructor de la classe Vector.

        :param iterable: seqüència de nombres que formen el vector
        '''
        self.components = [element for element in iterable]

    def __repr__(self):
        '''
        Representació oficial del vector.

        :return: cadena amb format Vector([...])
        '''
        return "Vector(" + repr(self.components) + ")"

    def __str__(self):
        '''
        Representació en format cadena del vector.

        :return: cadena amb les components del vector
        '''
        return str(self.components)

    def __len__(self):
        '''
        Retorna la dimensió del vector.

        :return: nombre de components del vector
        '''
        return len(self.components)

    def __eq__(self, altre):
        '''
        Compara si dos vectors són iguals component a component.

        :param altre: altre vector
        :return: True si són iguals, False en cas contrari
        '''
        if not isinstance(altre, Vector):
            return False
        return self.components == altre.components

    def __add__(self, altre):
        '''
        Suma dos vectors component a component.

        :param altre: vector a sumar
        :return: un nou vector amb la suma
        '''
        if not isinstance(altre, Vector):
            raise TypeError("Només es poden sumar vectors.")
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa dimensió.")

        suma = []
        for a, b in zip(self.components, altre.components):
            suma.append(a + b)
        return Vector(suma)

    def __sub__(self, altre):
        '''
        Resta dos vectors component a component.

        :param altre: vector a restar
        :return: un nou vector amb la resta
        '''
        if not isinstance(altre, Vector):
            raise TypeError("Només es poden restar vectors.")
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa dimensió.")

        resta = []
        for a, b in zip(self.components, altre.components):
            resta.append(a - b)
        return Vector(resta)

    def __mul__(self, altre):
        '''
        Multiplicació de vectors o de vector per escalar.

        Casos:
        - Vector * nombre: multiplica cada component pel nombre.
        - Vector * Vector: producte de Hadamard.

        :param altre: escalar o vector
        :return: un nou vector resultat de la multiplicació
        '''
        resultat = []

        if isinstance(altre, (int, float)):
            for component in self.components:
                resultat.append(component * altre)
            return Vector(resultat)

        if isinstance(altre, Vector):
            if len(self) != len(altre):
                raise ValueError("Els vectors han de tenir la mateixa dimensió.")

            for a, b in zip(self.components, altre.components):
                resultat.append(a * b)
            return Vector(resultat)

        raise TypeError("La multiplicació només es pot fer amb un nombre o amb un altre vector.")

    def __rmul__(self, altre):
        '''
        Multiplicació d'un escalar per un vector.

        :param altre: escalar
        :return: un nou vector resultat de la multiplicació
        '''
        return self * altre

    def __matmul__(self, altre):
        '''
        Producte escalar de dos vectors.

        :param altre: vector amb el qual es fa el producte escalar
        :return: nombre resultat del producte escalar
        '''
        if not isinstance(altre, Vector):
            raise TypeError("El producte escalar només es pot fer entre vectors.")
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa dimensió.")

        total = 0
        for a, b in zip(self.components, altre.components):
            total += a * b
        return total

    def __floordiv__(self, altre):
        '''
        Retorna la component paral·lela d'un vector respecte a un altre.

        Fórmula:
            ((v1 @ v2) / (v2 @ v2)) * v2

        :param altre: vector respecte al qual es projecta
        :return: vector paral·lel
        '''
        if not isinstance(altre, Vector):
            raise TypeError("La projecció només es pot calcular respecte a un altre vector.")
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa dimensió.")

        denominador = altre @ altre
        if denominador == 0:
            raise ZeroDivisionError("No es pot projectar sobre el vector zero.")

        factor = (self @ altre) / denominador
        return factor * altre

    def __mod__(self, altre):
        '''
        Retorna la component normal o perpendicular d'un vector respecte a un altre.

        Fórmula:
            v_perpendicular = v1 - v_paralela

        :param altre: vector respecte al qual es calcula la component normal
        :return: vector perpendicular
        '''
        if not isinstance(altre, Vector):
            raise TypeError("La component normal només es pot calcular respecte a un altre vector.")
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa dimensió.")

        return self - (self // altre)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
