% Si el motor no enciende y hay batería, la causa puede ser el arrancador
bateria(ok).
motor(no_enciende).
causa(arrancador) :- bateria(ok), motor(no_enciende).
