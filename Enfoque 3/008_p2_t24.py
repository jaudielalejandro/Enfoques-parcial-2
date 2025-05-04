class Boton {
    constructor(texto) {
        this.texto = texto;
    }

    click() {
        console.log(this.texto + " fue clickeado");
    }
}

let b = new Boton("Aceptar");
b.click();
