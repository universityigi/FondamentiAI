% ___ Esercizio 1 ____________

% a ** Fibonacci **
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :- N > 1, N1 is N-1, N2 is N-2, fibonacci(N1, F1), fibonacci(N2, F2), F is F1+F2.

% b ** Prime **

div(X,Y) :- 0 is X mod Y.
div(X,Y) :- X > Y+1, div(X, Y+1).

prime(2).
prime(3).
prime(N) :- integer(N), N > 3, N mod 2 =\= 0, \+div(N, 3).

% ___ Esercizio 2 ____________

% a ** Prodotto Scalare ** 
cdot([], [], 0).
cdot([H1|T1], [H2|T2], X) :- cdot(T1, T2, Y), X is H1*H2 + Y.

% b ** Steep **
steep([]).
steep([_]).
steep([H|T]) :- steep(T, H).

steep([], _).
steep([H|T], X) :- H >= X, SUM is H+X, steep(T, SUM).

% c ** Seg **
seg(S, L) :- append(_, SubList, L), append(S, _, SubList).


% d ** Insertion Sort **
isort(X, [], [X]).
isort(X, [H|T], [X,H|T]) :- X =< H.
isort(X, [H|T], [H|T1]) :- X > H, isort(X, T, T1).


% ___ Esercizio 3 ____________

% ** Depth First **

dfv(R, N) :- dfv_aux(R, N, []).

dfv_aux(R, R, Visited) :- \+ member(R, Visited).
dfv_aux(R, N, Visited) :-
    \+ member(R, Visited),
    arc(R, M),
    dfv_aux(M, N, [R|Visited]).

% knowledge base per l'es 3
arc(a,b).
arc(a,c).
arc(b,d).
arc(b,e).
arc(c,b).
arc(e,c).