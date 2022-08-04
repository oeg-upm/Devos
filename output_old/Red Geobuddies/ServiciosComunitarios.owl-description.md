```mermaid
	classDiagram

    
    class ProveedorServicioDeTren {
    
    }

    class Restaurante {
    
    }

    class RelacionFormadoPorTipoHabitacion {
    
    }

    class ClaseTransporte {
    
    }

    class Bomberos {
    
    }

    class Mercado {
    
    }

    class GrandesAlmacenes {
    
    }

    class ServicioIngesta {
    
    }

    class Hostal {
    
    }

    class Hospital {
    
    }

    class Menu {
    
    }

    class MedioDeTransporteAereo {
    
    }

    class ProveedorServicioOcio {
    
    }

    class InformacionAdministrativa {
    
    }

    class Tienda {
    
    }

    class ServicioDeAlojamiento {
    
    }

    class Medico {
    
    }

    class Opera {
    
    }

    class CasaDeComidas {
    
    }

    class Pension {
    
    }

    class Teatro {
    
    }

    class ProveedorServicioReligioso {
    
    }

    class ExpedicionCredenciales {
    
    }

    class Espectaculo {
    
    }

    class Vcard {
    
    }

    class ProveedorServicioAlimentacion {
    
    }

    class Refugio {
    
    }

    class ProveedorServicioSanitarios {
    
    }

    class ServicioDeInformacion {
    
    }

    class Albergue {
    
    }

    class TipoHabitacion {
    
    }

    class TipoServicioAlimentacion {
    
    }

    class InformacionAlPeregrino {
    
    }

    class ServicioDeportivo {
    
    }

    class AreaDeDescanso {
    
    }

    class TiendaDeRopa {
    
    }

    class PrestamoDeBicicleta {
    
    }

    class ServicioDeExpedicionDeCredenciales {
    
    }

    class ArticuloSujetoAProcesoDeCompra {
    
    }

    class ProveedorServicioPortuario {
    
    }

    class MedioDeTransporte {
    
    }

    class ServicioCultural {
    
    }

    class TiendaDePrensa {
    
    }

    class Supermercado {
    
    }

    class Autoservicio {
    
    }

    class ProveedorServicioAlojamiento {
    
    }

    class Casino {
    
    }

    class ServicioDeSanidad {
    
    }

    class Farmacia {
    
    }

    class Discoteca {
    
    }

    class ProveedorServicioEcuestre {
    
    }

    class InformacionSeguridad {
    
    }

    class ProveedorServicio {
    
    }

    class Mercadillo {
    
    }

    class ProveedorServicioDeFerrocarril {
    
    }

    class ProveedorServicioTransporteAlquiler {
    
    }

    class AlimentacionBasica {
    
    }

    class TransporteSanitario {
    
    }

    class InformacionTuristica {
    
    }

    class ProveedorServicioInformacion {
    
    }

    class Hotel {
    
    }

    class ServicioHabitacion {
    
    }

    class ServicioDeTransporte {
    
    }

    class ServicioComidaInternacional {
    
    }

    class ServicioDeAlimentacion {
    
    }

    class AreaDeInteres {
    
    }

    class BienDeConsumoIntermedio {
    
    }

    class MedioDeTransporteAcuatico {
    
    }

    class Bar {
    
    }

    class AsociacionDeAmigosDelCaminoDeSantiago {
    
    }

    class Concierto {
    
    }

    class ProteccionCivil {
    
    }

    class Servicio {
    
    }

    class ArticuloUnitario {
    
    }

    class ProveedorServicioAeroportuario {
    
    }

    class ProveedorServicioDeAutocar {
    
    }

    class AreaDeInteresTuristico {
    
    }

    class ProveedorServicioDeTaxi {
    
    }

    class Urgencias {
    
    }

    class AreaDeInteresCultural {
    
    }

    class Musical {
    
    }

    class ProveedorServicioDeportivo {
    
    }

    class TipoDeEspacio {
    
    }

    class BienDeConsumoFinal {
    
    }

    class ProveedorServicioCultural {
    
    }

    class ProveedorServicioTransporte {
    
    }

    class ServicioDeSeguridad {
    
    }

    class PoliciaLocal {
    
    }

    class TiendaDeCalzado {
    
    }

    class ProveedorServicioDeHelipuerto {
    
    }

    class AgenciaTuristica {
    
    }

    class ArticuloEspecializado {
    
    }

    class GuardiaCivil {
    
    }

    class ProveedorServicioDeAutobus {
    
    }

    class AtencionEspecializada {
    
    }

    class ProveedorServicioSeguridad {
    
    }

    class MedioDeTransporteTerrestre {
    
    }

    class Acogida {
    
    }

    class AreaDeInteresPaisajistico {
    
    }

    class Bolera {
    
    }

    class ServicioDeOcio {
    
    }

    class ServicioReligioso {
    
    }

    class PoliciaNacional {
    
    }

    class TiendaDeAlimentacion {
    
    }

    class Producto {
    
    }



RelacionFormadoPorTipoHabitacion  --> TipoHabitacion   :deTipoHabitacion  

ProveedorServicioAlojamiento  --> RelacionFormadoPorTipoHabitacion   :formadoPorTipoHabitacion  

ProveedorServicioTransporte  --> MedioDeTransporte   :ofreceServicioDeTransporteMediante  

ProveedorServicio  --> Producto   :ofreceProducto  

ProveedorServicio  --> Servicio   :ofreceServicio  

Producto  --> ProveedorServicio   :productoOfrecidoPor  

Servicio  --> ProveedorServicio   :servicioOfrecidoPor  

```