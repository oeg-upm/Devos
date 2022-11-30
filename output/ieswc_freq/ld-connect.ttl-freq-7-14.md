```mermaid
	classDiagram

    
    class Publication {
    
    }

    class List {
    
    }

    class Geocoded Location {
    
    }

    class Book {
    
    }

    class Journal {
    
    }

    class Series {
    
    }

    class Chapter {
    
    }



List  --> List   :first  

Publication  --> Chapter   :Publication In Chapter  

List  --> List   :rest  

Book  --> Series   :Book In Series  

Chapter  --> Book   :Chapter In Book  

Publication  --> string   :Source File  

Volume  --> Journal   :Volume In Journal  

Series  --> Category   :Category  

Organization  --> Geocoded Location   :Geocoding Output  

Journal  --> Category   :Category  

Geocoded Location  --> Geometry   :Geometry  

```