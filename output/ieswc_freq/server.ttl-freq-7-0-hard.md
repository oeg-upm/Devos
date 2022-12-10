```mermaid
	classDiagram

    
    class `VirtualServer` {
    
    }

    class `Physical Server` {
    
    }

    class `Server` {
    
    }

    class `Account` {
    
    }

    class `Data Center` {
    
    }

    class `Network Card` {
    
    }

    class `n89965ea65ed643b08a81f7932b462f4fb1` {
    
    }



`Physical Server`  --> `VirtualServer`   :hosts  

`Account`  --> `Server`   :is Account Of  

`VirtualServer`  --> `Physical Server`   :hosted In  

`Server`  --> `n89965ea65ed643b08a81f7932b462f4fb1`   :assignment Status  

`Server`  --> `Account`   :has account  

`Physical Server`  --> `Network Card`   :networkCard  

`Server`  --> `Account`   :has account  

`Server`  --> `Account`   :has account  

`Physical Server`  --> `Network Card`   :networkCard  

```