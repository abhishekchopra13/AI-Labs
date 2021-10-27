himalayan_club(a).
himalayan_club(b).
himalayan_club(c).

% If notmc and notsk, then fail
himalayan_club(X):-notmc(X),notsk(X),!, fail.
himalayan_club(_).

like(a,rain).
like(a,snow).

like(a,X) :- dislike(b,X).
like(b,X) :- like(a,X),!,fail.
like(b,_).

mc(X):-like(X,rain),!,fail.
mc(_).

notsk(X):- dislike(X,snow).

notmc(X):- mc(X),!,fail.
notmc(_).

% If P likes Q, then fail
dislike(P,Q):- like(P,Q),!,fail.
dislike(_,__).

query(X):-himalayan_club(X),mc(X),notsk(X),!.