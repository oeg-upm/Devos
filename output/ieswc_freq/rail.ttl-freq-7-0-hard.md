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



`NetElement`  --> `Relation`   :relation  

`IntrinsicCoordinate`  --> `IntrinsicCoordinate`   :reaches  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`Relation`  --> `NetElement`   :element  

`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`AssociatedPositioningSystem`  --> `IntrinsicCoordinate`   :intrinsicCoordinate  

`NetElement`  --> `Relation`   :relation  

`NetElement`  --> `Relation`   :relation  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

`PositionedRelation`  --> `PositioningNetElement`   :elementB  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`PositionedRelation`  --> `PositioningNetElement`   :elementA  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

`PositioningNetElement`  --> `AssociatedPositioningSystem`   :associatedPositioningSystem  

```