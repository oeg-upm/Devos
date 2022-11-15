```mermaid
	classDiagram

    
    class PositioningNetElement {
    
    }

    class IntrinsicCoordinate {
    
    }

    class NetElement {
    
    }

    class PositioningSystemCoordinate {
    
    }

    class Relation {
    
    }

    class PositionedRelation {
    
    }

    class AssociatedNetElementCoordinate {
    
    }

    class AssociatedPositioningSystem {
    
    }

    class LinearPositioningSystem {
    
    }

    class LinearLocation {
    
    }



PositionedRelation  --> PositioningNetElement   :elementA  

NetElement  --> Relation   :relation  

Relation  --> NetElement   :element  

n05664515285245dd97497a2f591251f7b27  --> PositioningNetElement   :netElement  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

LinearLocation  --> OrderedAssociatedNetElement   :associatedElement  

n05664515285245dd97497a2f591251f7b20  --> PositioningSystemCoordinate   :coordinate  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

PositionedRelation  --> PositioningNetElement   :elementB  

IntrinsicCoordinate  --> IntrinsicCoordinate   :reaches  

LinearPositioningSystem  --> LinearAnchorPoint   :anchor  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

n05664515285245dd97497a2f591251f7b24  --> NetElement   :elementPart  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :end  

LinearLocation  --> OrderedAssociatedNetElement   :associatedElement  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

PositioningNetElement  --> AssociatedPositioningSystem   :associatedPositioningSystem  

PositionedRelation  --> PositioningNetElement   :elementB  

PositionedRelation  --> PositioningNetElement   :elementB  

AssociatedNetElement  --> PositioningNetElement   :netElement  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

AssociatedNetElementCoordinate  --> PositioningSystemCoordinate   :start  

AssociatedPositioningSystem  --> PositioningSystem   :positioningSystem  

LinearCoordinate  --> LinearPositioningSystem   :positioningSystem  

PositionedRelation  --> PositioningNetElement   :elementA  

PositionedRelation  --> PositioningNetElement   :elementA  

NetElement  --> Relation   :relation  

NetElement  --> Relation   :relation  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

SpotLocationCoordinate  --> PositioningSystemCoordinate   :coordinate  

AssociatedPositioningSystem  --> IntrinsicCoordinate   :intrinsicCoordinate  

UnorderedCollection  --> NetElement   :elementPart  

LinearLocationCoordinate  --> PositioningSystemCoordinate   :coordinate  

OrderedCollection  --> NetElement   :elementPart  

PositioningSystemCoordinate  --> PositioningSystem   :positioningSystem  

```