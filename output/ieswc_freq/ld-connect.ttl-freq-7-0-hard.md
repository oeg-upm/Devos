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



`List`  --> `List`   :rest  

`Publication`  --> `Chapter`   :Publication In Chapter  

`List`  --> `List`   :first  

`Chapter`  --> `Book`   :Chapter In Book  

`Book`  --> `Series`   :Book In Series  

```