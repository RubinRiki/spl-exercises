# HADAS DONAT 325950954
# RIKI RUBIN 326380359
#    1. הגדרות משפחה בסיסיות

/* Married(X,Y): X = male, Y = female */
male(avigdor).
male(dan).
male(yoav).
male(noam).

female(miri).
female(rachel).
female(lea).
female(aya).

married(avigdor,miri).
married(dan,rachel).

parent(avigdor,dan).
parent(miri,dan).
parent(avigdor,lea).
parent(miri,lea).
parent(dan,yoav).
parent(rachel,yoav).
parent(dan,aya).
parent(rachel,aya).

#    2. קשרי משפחה

2.1 father(X,Y) :- parent(X,Y), male(X).
2.2 mother(X,Y) :- parent(X,Y), female(X).
2.3 son(X,Y) :- parent(Y,X), male(X).
2.4 daughter(X,Y) :- parent(Y,X), female(X).
2.5 grandfather(X,Y) :- parent(X,Z), parent(Z,Y), male(X).
2.6 grandmother(X,Y) :- parent(X,Z), parent(Z,Y), female(X).
2.7 grandson(X,Y) :- parent(Y,Z), parent(Z,X), male(X).
2.8 granddaughter(X,Y) :- parent(Y,Z), parent(Z,X), female(X).

2.9 sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.

2.10 uncle(X,Y) :- brother(X,Z), parent(Z,Y).
2.11 aunt(X,Y) :- sister(X,Z), parent(Z,Y).

2.12 brother(X,Y) :- sibling(X,Y), male(X).
2.13 sister(X,Y) :- sibling(X,Y), female(X).

2.14 brother_in_law(X,Y) :- married(X,Z), sibling(Z,Y).
2.15 brother_in_law(X,Y) :- sibling(X,Z), married(Z,Y).

2.16 niece(X,Y) :- parent(Z,X), sibling(Z,Y), female(X).
2.17 nephew(X,Y) :- parent(Z,X), sibling(Z,Y), male(X).

2.18 cousin(X,Y) :- parent(A,X), parent(B,Y), sibling(A,B).

#    3. רקורסיה ורשימות

3.1 reverse([], []).
3.2 reverse([H|T], Rev) :- reverse(T, RT), append(RT,[H],Rev).

3.3 member(X,[X|_]).
3.4 member(X,[_|T]) :- member(X,T).

3.5 palindrome(L) :- reverse(L,L).

3.6 sorted([]).
3.7 sorted([_]).
3.8 sorted([X,Y|T]) :- X =< Y, sorted([Y|T]).

3.9 permutation([], []).
3.10 permutation(L, [H|T]) :- select(H,L,R), permutation(R,T).

#    4. אריתמטיקה
  

4.1 scum(1,1).
4.2 scum(N,Res) :- N > 1, N1 is N-1, scum(N1,R1), Res is R1+N.

4.3 sumDigits(0,0).
4.4 sumDigits(Num,Sum) :-
    Num > 0,
    Digit is Num mod 10,
    Rest is Num // 10,
    sumDigits(Rest,Partial),
    Sum is Partial + Digit.

4.5 split(0,[]).
4.6 split(N,[D|Rest]) :-
    N > 0,
    D is N mod 10,
    R is N // 10,
    split(R,Rest).

4.7 create(List,N) :- create(List,0,N).
4.8 create([],Acc,Acc).
4.9 create([H|T],Acc,N) :-
    NewAcc is Acc*10 + H,
    create(T,NewAcc,N).


4.10 reverse_number(N,Rev) :-
    split(N,L),
    reverse(L,LR),
    create(LR,Rev).

#    5. פעולות על רשימות


5.1 intersection([],_,[]).
5.2 intersection([H|T],L2,[H|Z]) :-
    member(H,L2),
    intersection(T,L2,Z).
5.3 intersection([_|T],L2,Z) :-
    intersection(T,L2,Z).

5.4 minus([],_,[]).
5.5 minus([H|T],L2,Z) :-
    member(H,L2),
    minus(T,L2,Z).
5.6 minus([H|T],L2,[H|Z]) :-
    \+ member(H,L2),
    minus(T,L2,Z).
