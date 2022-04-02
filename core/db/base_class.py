from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


"""
declared_attrnormalmente se aplica como decorador a un método de nivel de clase, 
convirtiendo el atributo en una propiedad similar a un escalar que se puede invocar desde la clase sin instanciar. 
El proceso de mapeo declarativo busca estos declared_attrinvocables a medida que explora las clases y asume que cualquier 
atributo marcado con declared_attrserá un invocable que producirá un objeto específico para el mapeo declarativo o la configuración de la tabla.

declared_attrsuele aplicarse a mixins, para definir relaciones que se aplicarán a diferentes implementadores de la clase. 
También se usa para definir Columnobjetos que incluyen la ForeignKeyconstrucción, ya que estos no se pueden reutilizar 
fácilmente en diferentes asignaciones. El siguiente ejemplo ilustra ambos:
"""
"""
Esta función hace uso del registry.as_declarative_base() método, primero creando registryautomáticamente y luego invocando al decorador.
"""

@as_declarative()
class Base:
    id : Any
    __name__: str
    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()

