```mermaid
	classDiagram

    
    class Asset {
    
    }

    class SKOSConcept {
    
    }

    class Identifier {
    
    }



Asset  --> SKOSConcept   :interoperabilityLevel  

Asset  --> Asset   :includedAsset  

Asset  --> Asset   :sample  

```