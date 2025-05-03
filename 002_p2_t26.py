(deftemplate temperatura
   (slot valor)
   (slot etiqueta))

(deffacts temperaturas
   (temperatura (valor 35) (etiqueta caliente)))
