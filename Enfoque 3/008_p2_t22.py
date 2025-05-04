% En Prolog:
padre(juan, pedro).
madre(ana, pedro).

% FOIL aprendería reglas como:
padre(X, Y) :- hombre(X), progenitor(X, Y).
