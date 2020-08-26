;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
      ((> 0 x) -1)
      ((= 0 x) 0)
      ((< 0 x) 1))
  
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (if (= 0 n)
      1
      (if (= (modulo n 2) 0)
      (square (pow b (/ n 2)))
      (* (square (pow b (/ (- n 1) 2))) b)))
  
)

(define (unique s)
  'YOUR-CODE-HERE
  (define (uni x)
      (define (f item)
          (not (eq? item x)))
      f)
  (if (= 0 (length s))
      ()
      (cons (car s) (unique (filter (uni (car s)) s))))
      
)