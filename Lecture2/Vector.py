class Vector:

    def __init__(self, n=2):
        self._coords = [0] * n;

    def __str__(self):
        result = '< '
        result += ", ".join([ str(x) for x in self._coords])
        result = result + ' >'
        return result

    def __getitem__(self, k):
        return self._coords[k]

    def __setitem__(self, k, v):
        self._coords[k] = v

    def __len__(self):
        return len(self._coords)
    
    def __add__(self, other):
        if len(other) == len(self):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] + other[i]
            return result
        else:
            raise ValueError('dimensions must agree')

    def __mul__(self, other):
        if isinstance( other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = other * self._coords[i]
            return result
        else:
            if len(other) == len(self):
                result = 0.0
                for i in range(len(self)):
                    result += self[i] * other[i]
                return result
            else:
                raise ValueError('dimensions must agree')
        

v1 = Vector(3)
v1[0] = 1
v1[1] = -2
v1[2] = 3

v2 = Vector(3)
v2[0] = 3
v2[1] = -0.5
v2[2] = 7
    
