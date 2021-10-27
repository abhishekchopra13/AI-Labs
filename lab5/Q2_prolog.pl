himalayan_club(a).
himalayan_club(b).
himalayan_club(c).

himalayan_club(A):-mountain_climber(A);skier(A).

like(a, snow).
like(a, rain).

dislike(b, A):-like(a, A).
dislike(a, A):-like(b, A).

skier(A):-like(A, snow).
mountain_climber(A):-dislike(A, rain).

query(D):-himalayan_club(D), mountain_climber(D), not(skier(D)),!.
