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