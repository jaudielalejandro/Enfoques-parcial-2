class Boton {
    constructor(etiqueta) {
        this.etiqueta = etiqueta;
    }

    click() {
        console.log(`${this.etiqueta} clickeado`);
    }
}

const boton = new Boton("Aceptar");
boton.click();  // Evento de clic
