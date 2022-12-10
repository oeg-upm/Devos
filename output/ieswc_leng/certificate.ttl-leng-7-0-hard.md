```mermaid
	classDiagram

    
    class `Certificate Signing Request` {
    
    }

    class `SSL Certificate` {
    
    }

    class `Digital Certificate` {
    
    }

    class `CFCA (China Financial Certification Authority) Certificate` {
    
    }

    class `Digital Certificate Deployment` {
    
    }

    class `Digital Certificate Bundle` {
    
    }

    class `Datatype` {
    
    }



`Digital Certificate`  --> `Certificate Signing Request`   :has certificate signing request  

`Digital Certificate`  --> `Digital Certificate Deployment`   :has certificate deployment  

`Digital Certificate Bundle`  --> `Digital Certificate`   :contains certificate  

`Digital Certificate`  --> `Certificate Signing Request`   :has certificate signing request  

`Digital Certificate Bundle`  --> `Digital Certificate`   :contains certificate  

`Digital Certificate`  --> `Certificate Signing Request`   :has certificate signing request  

`Digital Certificate Bundle`  --> `Digital Certificate`   :contains certificate  

```