(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (x) (append (cons first nil) x)) rests))

(define (zip pairs)
  'replace-this-line)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define i 0)
  (define (add-index s i)
      (cond ((= 0 (length s)) s)
        (else (cons (cons i (cons (car s) nil)) (add-index (cdr s) (+ 1 i)))))
      )
  (add-index s i)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond ((= 0 (length denoms)) nil)
        ((<= total 0) nil)
         ((< total (car denoms)) (list-change total (cdr denoms)))
         (else (cons (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms)))))
;   (map (lambda (x) () denoms)
;   (define lis '(()))
;   (define (rec-change total lis)
;       (map (lambda (x) (cons-all x lis)) (filter (lambda (x) (>= total x)) denoms)))
  
  
  )
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         'replace-this-line
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         'replace-this-line
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           'replace-this-line
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           'replace-this-line
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         'replace-this-line
         ; END PROBLEM 18
         )))