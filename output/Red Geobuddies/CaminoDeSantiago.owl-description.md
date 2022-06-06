```mermaid
	classDiagram

    
    class EventoEducativo {
    
    }

    class ElementoBotiquin {
    
    }

    class EquipamientoParaBicicleta {
    
    }

    class ElementoBotiquinPersona {
    
    }

    class EquipamientoParaPersona {
    
    }

    class CaminoPeregrinacion {
    
    }

    class Publico {
    
    }

    class EquipamientoParaCaballo {
    
    }

    class Equipamiento {
    
    }

    class ProductoAseo {
    
    }

    class Conferencia {
    
    }

    class AlimentacionPersona {
    
    }

    class EventoSocial {
    
    }

    class AlimentacionCaballo {
    
    }

    class Exposicion {
    
    }

    class Utensilios {
    
    }

    class Ropa {
    
    }

    class Desfile {
    
    }

    class EventoReligioso {
    
    }

    class Alimentacion {
    
    }

    class EquipamientoDescanso {
    
    }

    class PaseCinematografico {
    
    }

    class ElementoBotiquinCaballo {
    
    }

    class Concierto {
    
    }

    class Libro {
    
    }

    class Peregrino {
    
    }

    class Encuentro {
    
    }

    class Calzado {
    
    }



CaminoPeregrinacion  --> Etapa   :SeComponeDe  

CaminoPeregrinacion  --> Peregrino   :caminoRecorridoPor  

CaminoPeregrinacion  --> LimiteAdministrativo   :pasaPor  

Etapa  --> CaminoPeregrinacion   :componeCamino  

Peregrino  --> CaminoPeregrinacion   :recorreCamino  

Publico  --> EventoSocial   :publicoObjetivoDe  

EventoSocial  --> Publico   :orientadoAPublico  

Equipamiento  --> MedioTransporteParaElCamino   :esParaMedioTransporte  

MedioTransporteParaElCamino  --> Equipamiento   :tieneEquipamiento  

EventoSocial  --> Event   :ocurreEn  

EventoSocial  --> Nb0fb40f9943149e28a7a095fc715db30   :tieneLugarEn  

EventoSocial  --> Ne3cf94970fe24b5084a11e82e6f9052b   :tieneOrganizador  

N40dd1d730e16489ab7279bc4c59f5bf5  --> EventoSocial   :esLugarDeEvento  

N0f85411be57a4a46bd050e85f498bf7c  --> EventoSocial   :esOrganizadorDe  

```