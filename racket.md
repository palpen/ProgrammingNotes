# Notes on Racket

## Binding variables
## Functions
* Defining functions
```racket
(lambda (x) (* x x x))  ; anonymous function for cube of x
(define cube (lambda (x) (* x x x)))
(define (cube x) (* x x x))
```
* Calling functions
```
(cube 3)
>>> 27
```
In general, `(e x)` means to evaluate the expression `e` with argument `x`. `(e)` means to evaluate the expression with zero arguments.

## Lists
* Creating lists
```racket
(define x (cons 1 (cons 2 (cons 3 null))))
(define x (cons 1 (cons 2 (cons 3 '()))))
(define x (list 1 2 3))
```