```mermaid
	classDiagram

    
    class ProperInterval {
    
    }

    class TemporalEntity {
    
    }

    class Instant {
    
    }

    class GeneralDateTimeDescription {
    
    }

    class DayOfWeek {
    
    }

    class Duration {
    
    }

    class GeneralDurationDescription {
    
    }

    class TRS {
    
    }

    class TemporalDuration {
    
    }

    class TemporalPosition {
    
    }



Interval  --> Instant   :inside  

Instant  --> GeneralDateTimeDescription   :inDateTime  

n7e3c7e0bb1614bc0b6e1ae25a3f6a74db66  --> TRS   :hasTRS  

ProperInterval  --> ProperInterval   :intervalFinishedBy  

Instant  --> TemporalPosition   :inTemporalPosition  

ProperInterval  --> ProperInterval   :intervalEquals  

ProperInterval  --> ProperInterval   :intervalBefore  

ProperInterval  --> ProperInterval   :intervalStartedBy  

TemporalEntity  --> Instant   :hasEnd  

ProperInterval  --> ProperInterval   :intervalFinishes  

ProperInterval  --> ProperInterval   :intervalDisjoint  

ProperInterval  --> ProperInterval   :intervalStarts  

ProperInterval  --> ProperInterval   :intervalIn  

TemporalEntity  --> Instant   :hasBeginning  

ProperInterval  --> ProperInterval   :intervalOverlaps  

ProperInterval  --> ProperInterval   :intervalContains  

ProperInterval  --> ProperInterval   :intervalAfter  

ProperInterval  --> ProperInterval   :intervalDuring  

ProperInterval  --> ProperInterval   :intervalMetBy  

ProperInterval  --> ProperInterval   :intervalMeets  

DateTimeInterval  --> GeneralDateTimeDescription   :hasDateTimeDescription  

GeneralDateTimeDescription  --> DayOfWeek   :dayOfWeek  

GeneralDateTimeDescription  --> MonthOfYear   :monthOfYear  

TemporalEntity  --> TemporalEntity   :after  

ProperInterval  --> ProperInterval   :intervalOverlappedBy  

GeneralDateTimeDescription  --> TimeZone   :timeZone  

TemporalEntity  --> TemporalEntity   :before  

Instant  --> TimePosition   :inTimePosition  

TemporalEntity  --> TemporalDuration   :hasTemporalDuration  

```