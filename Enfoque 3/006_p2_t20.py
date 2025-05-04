% Prolog
vuela(X) :- ave(X), not(excepcion(X)).
excepcion(pinguino).
ave(pinguino).
