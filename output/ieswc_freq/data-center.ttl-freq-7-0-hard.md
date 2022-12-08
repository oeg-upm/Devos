```mermaid
	classDiagram

    
    class `Data Center` {
    
    }

    class `Data Center Connection` {
    
    }

    class `n4ee2ba98808a436b9ea85c2049cbd8beb1` {
    
    }

    class `n4ee2ba98808a436b9ea85c2049cbd8beb5` {
    
    }

    class `n4ee2ba98808a436b9ea85c2049cbd8beb9` {
    
    }

    class `Location` {
    
    }

    class `Site` {
    
    }



`Data Center Connection`  --> `n4ee2ba98808a436b9ea85c2049cbd8beb1`   :connection type  

`Data Center`  --> `n4ee2ba98808a436b9ea85c2049cbd8beb5`   :data center type  

`Data Center`  --> `Data Center Connection`   :allows connection via  

`Data Center`  --> `Site`   :located in site  

`Data Center`  --> `n4ee2ba98808a436b9ea85c2049cbd8beb9`   :hosts  

`Data Center`  --> `Location`   :located In  

`Data Center Connection`  --> `Data Center`   :startInternetDataCenter  

`Data Center Connection`  --> `Data Center`   :startInternetDataCenter  

`Data Center Connection`  --> `Data Center`   :endInternetDataCenter  

`Data Center Connection`  --> `Data Center`   :endInternetDataCenter  

`Data Center`  --> `Data Center Connection`   :allows connection via  

`Data Center`  --> `Data Center Connection`   :allows connection via  

`Data Center`  --> `Site`   :located in site  

`Data Center`  --> `Location`   :located In  

`Data Center`  --> `Site`   :located in site  

`Data Center`  --> `Location`   :located In  

```