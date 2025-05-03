(deftemplate clima (slot cielo))
(defrule no_hay_sol
   (clima (cielo nublado))
   =>
   (assert (lluvia si)))
