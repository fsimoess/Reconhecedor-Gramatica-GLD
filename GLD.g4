grammar GLD;

s : 'a' s 
  | 'b' a ;
a : EOF 
  | 'c' a ; 
