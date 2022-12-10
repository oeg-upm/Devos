```mermaid
	classDiagram

    
    class `Publication` {
    
    }

    class `List` {
    
    }

    class `Geocoded Location` {
    
    }

    class `Book` {
    
    }

    class `Journal` {
    
    }

    class `Series` {
    
    }

    class `Chapter` {
    
    }



`Chapter`  --> `Book`   :Chapter In Book  

`List`  --> `List`   :first  

`List`  --> `List`   :rest  

`Publication`  --> `Chapter`   :Publication In Chapter  

`Book`  --> `Series`   :Book In Series  

```