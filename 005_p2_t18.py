padre(juan, pedro).
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).

% ¿X es abuelo de Y?
?- abuelo(juan, Y).
