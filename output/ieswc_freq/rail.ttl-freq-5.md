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



Relation  --> NetElement   :element  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

n64cb82f2c90342969fe091a8f7d8d571b24  --> NetElement   :elementPart  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

PositionedRelation  --> PositioningNetElement   :elementA  

NetElement  --> Relation   :relation  

PositionedRelation  --> PositioningNetElement   :elementB  

LinearPositioningSystem  --> LinearAnchorPoint   :anchor  

n64cb82f2c90342969fe091a8f7d8d571b27  --> PositioningNetElement   :netElement  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

IntrinsicCoordinate  --> IntrinsicCoordinate   :reaches  

n64cb82f2c90342969fe091a8f7d8d571b20  --> PositioningSystemCoordinate   :coordinate  

s  --> a   :t  

e  --> e   :l  

e  --> d   :n  

n  --> t   :e  

i  --> t   :n  

a  --> s   :s  

e  --> e   :l  

e  --> e   :l  

r  --> l   :e  

c  --> o   :o  

p  --> s   :o  

```