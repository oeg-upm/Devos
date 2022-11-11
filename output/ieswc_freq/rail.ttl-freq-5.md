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



PositionedRelation  --> PositioningNetElement   :elementB  

LinearPositioningSystem  --> LinearAnchorPoint   :anchor  

nfe502903a72a4958a72cae6a2d7ed2f2b20  --> PositioningSystemCoordinate   :coordinate  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

Relation  --> NetElement   :element  

nfe502903a72a4958a72cae6a2d7ed2f2b24  --> NetElement   :elementPart  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

PositionedRelation  --> PositioningNetElement   :elementA  

IntrinsicCoordinate  --> IntrinsicCoordinate   :reaches  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

nfe502903a72a4958a72cae6a2d7ed2f2b27  --> PositioningNetElement   :netElement  

NetElement  --> Relation   :relation  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

n  --> t   :e  

r  --> l   :e  

a  --> s   :s  

e  --> e   :l  

s  --> a   :t  

p  --> s   :o  

c  --> o   :o  

i  --> t   :n  

e  --> d   :n  

e  --> e   :l  

e  --> e   :l  

```