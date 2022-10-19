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



AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

PositionedRelation  --> PositioningNetElement   :elementA  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

AreaLocation  --> AssociatedNetElement   :associatedNetElement  

CompositionNetElement  --> ElementPartCollection   :elementCollection  

Relation  --> NetElement   :element  

OrderedCollection  --> RDFList   :elementPartList  

nb3326e55e1944b9d8965c2af15ea47d5b20  --> PositioningSystemCoordinate   :coordinate  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

PositionedRelation  --> PositioningNetElement   :elementB  

nb3326e55e1944b9d8965c2af15ea47d5b24  --> NetElement   :elementPart  

nb3326e55e1944b9d8965c2af15ea47d5b27  --> PositioningNetElement   :netElement  

LinearLocation  --> OrderedAssociatedNetElement   :associatedElement  

IntrinsicCoordinate  --> IntrinsicCoordinate   :reaches  

LinearPositioningSystem  --> LinearAnchorPoint   :anchor  

NetElement  --> Relation   :relation  

e  --> e   :l  

n  --> t   :e  

a  --> s   :s  

c  --> o   :o  

e  --> e   :l  

a  --> s   :s  

e  --> e   :l  

a  --> s   :s  

s  --> a   :t  

i  --> t   :n  

e  --> d   :n  

p  --> s   :o  

r  --> l   :e  

```