```mermaid
	classDiagram

    
    class PositioningSystemCoordinate {
    
    }

    class PositioningNetElement {
    
    }

    class NetElement {
    
    }

    class IntrinsicCoordinate {
    
    }

    class LinearAnchorPoint {
    
    }

    class OrderedAssociatedNetElement {
    
    }

    class AssociatedNetElement {
    
    }

    class AssociatedPositioningSystem {
    
    }

    class ElementPartCollection {
    
    }

    class RDFList {
    
    }



LinearPositioningSystem  --> LinearAnchorPoint   :anchor  

LinearLocation  --> OrderedAssociatedNetElement   :associatedElement  

NetElement  --> Relation   :relation  

OrderedCollection  --> RDFList   :elementPartList  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

PositionedRelation  --> PositioningNetElement   :elementB  

AreaLocation  --> AssociatedNetElement   :associatedNetElement  

n487941f7af5943ebb12a70be1d6b47ebb24  --> NetElement   :elementPart  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

n487941f7af5943ebb12a70be1d6b47ebb27  --> PositioningNetElement   :netElement  

CompositionNetElement  --> ElementPartCollection   :elementCollection  

Relation  --> NetElement   :element  

n487941f7af5943ebb12a70be1d6b47ebb20  --> PositioningSystemCoordinate   :coordinate  

IntrinsicCoordinate  --> IntrinsicCoordinate   :reaches  

PositionedRelation  --> PositioningNetElement   :elementA  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

r  --> l   :e  

e  --> e   :l  

p  --> s   :o  

a  --> s   :s  

s  --> a   :t  

c  --> o   :o  

a  --> s   :s  

i  --> t   :n  

n  --> t   :e  

e  --> d   :n  

a  --> s   :s  

e  --> e   :l  

e  --> e   :l  

```