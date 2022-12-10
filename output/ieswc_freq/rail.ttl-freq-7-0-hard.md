```mermaid
	classDiagram

    
    class `PositioningNetElement` {
    
    }

    class `IntrinsicCoordinate` {
    
    }

    class `NetElement` {
    
    }

    class `PositioningSystemCoordinate` {
    
    }

    class `AssociatedPositioningSystem` {
    
    }

    class `Relation` {
    
    }

    class `PositionedRelation` {
    
    }



`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`Relation`  --> `NetElement`   :element  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

`IntrinsicCoordinate`  --> `IntrinsicCoordinate`   :reaches  

`NetElement`  --> `Relation`   :relation  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

`NetElement`  --> `Relation`   :relation  

`NetElement`  --> `Relation`   :relation  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

```