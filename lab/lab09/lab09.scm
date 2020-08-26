;; Scheme ;;

(define (over-or-under x y)
  'YOUR-CODE-HERE
  (if (> x y)
    1
    (if (= x y)
      0
      -1))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst f lst)
  'YOUR-CODE-HERE
  (if (= 0 (length lst))
    ()
    (if (f (car lst))
      (cons (car lst) (filter-lst f (cdr lst)))
      (filter-lst f (cdr lst))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  'YOUR-CODE-HERE
  (define (adder x)
    (+ num x))
  adder
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  ; 'YOUR-CODE-HERE
  (cons (cons 1 ()) (cons 2 (cons (cons 3 (cons 4 ())) (cons 5 ()))))
)

(define (composed f g)
  'YOUR-CODE-HERE
  (define (comp x)
    (f (g x)))
  comp
)

(define (remove item lst)
  'YOUR-CODE-HERE
  (if (= 0 (length lst))
    ()
    (if (= item (car lst))
    (remove item (cdr lst))
    (cons (car lst) (remove item (cdr lst)))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  'YOUR-CODE-HERE
  (define (searcher item lst)
    (if (= 0 (length lst))
      #t
      (if (= item (car lst))
        #f
        (searcher item (cdr lst))
        )
      )
    
  )
  (if (= 0 (length s))
    ()
    (if (= 1 (length s))
    (cons (car s) ())
    ((if (searcher (car s) (cdr s))
        (cons (car s) (no-repeats (cdr s)))
        (no-repeats (cdr s))
      )
    )
    
  )
    )
  
)

(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (= 0 (length s))
    ()
    (if (pair? (car s))
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if (eq? old (car s))
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new))
      )
    )
  )
)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (define (searcher item lst_old lst_new)
    (if (= 0 (length lst_old))
      item
      (if (eq? item (car lst_old))
      (car lst_new)
      (searcher item (cdr lst_old) (cdr lst_new))
    ))
    
  )
  (if (= 0 (length s))
    ()
    (if (pair? (car s))
      (cons (sub-all (car s) olds news) (sub-all (cdr s) olds news))
      (cons (searcher (car s) olds news) (sub-all (cdr s) olds news))
    )
  )
)