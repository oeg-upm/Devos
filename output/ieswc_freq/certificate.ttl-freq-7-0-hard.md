```mermaid
	classDiagram

    
    class `Digital Certificate` {
    
    }

    class `Digital Certificate Bundle` {
    
    }

    class `Digital Certificate Deployment` {
    
    }

    class `Certificate Signing Request` {
    
    }



`Digital Certificate`  --> `Digital Certificate Deployment`   :has certificate deployment  

`Digital Certificate`  --> `Certificate Signing Request`   :has certificate signing request  

`Digital Certificate Bundle`  --> `Digital Certificate`   :contains certificate  

```