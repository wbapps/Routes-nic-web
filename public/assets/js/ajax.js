
function puntosInteres_ruta(id_ruta){
    Dajaxice.app.puntosInteres(Dajax.process, {'id_ruta': id_ruta});
    Dajaxice.app.nombreRuta(Dajax.process, {'id_ruta': id_ruta});
}