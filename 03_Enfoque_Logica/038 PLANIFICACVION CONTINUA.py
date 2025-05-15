% Hechos
animal(gato).
animal(perro).
mamifero(X) :- animal(X), tiene_sangre_caliente(X).

% Base de conocimiento = hechos + reglas
