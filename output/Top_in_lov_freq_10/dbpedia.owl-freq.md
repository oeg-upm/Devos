```mermaid
	classDiagram

    
    class Person {
    
    }

    class PopulatedPlace {
    
    }

    class Place {
    
    }

    class SportsTeam {
    
    }

    class Award {
    
    }

    class Organisation {
    
    }

    class MeanOfTransportation {
    
    }

    class Country {
    
    }

    class Species {
    
    }

    class Agent {
    
    }



Place  --> Place   :northEastPlace  

Place  --> Place   :hasOutsidePlace  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Food  --> Person   :creatorOfDish  

River  --> Place   :sourceConfluenceRegion  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterTransport  

Person  --> Person   :sibling  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Settlement  --> PopulatedPlace   :largestMetro  

Country  --> Country   :twinCountry  

PopulatedPlace  --> PopulatedPlace   :sheading  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Musical  --> Person   :musicBy  

Athlete  --> SportsTeam   :nflTeam  

MusicalWork  --> PopulatedPlace   :recordedIn  

Settlement  --> Place   :lowestPoint  

Person  --> SKOSConcept   :startReign  

Organisation  --> Person   :superintendent  

Settlement  --> Place   :highestPoint  

Sport  --> Person   :footedness  

Organisation  --> Person   :chaplain  

Work  --> Agent   :producer  

Person  --> Place   :livingPlace  

PopulatedPlace  --> Person   :viceLeader  

PopulatedPlace  --> PopulatedPlace   :borough  

Family  --> Person   :lastFamilyMember  

TelevisionShow  --> Person   :presenter  

Country  --> Continent   :continent  

Place  --> PopulatedPlace   :district  

Species  --> Species   :fossil  

Restaurant  --> Person   :headChef  

Aircraft  --> Organisation   :aircraftUser  

Work  --> Person   :mainCharacter  

VideoGame  --> Person   :gameArtist  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

FigureSkater  --> Person   :choreographer  

Olympics  --> Person   :olympicOathSwornBy  

Film  --> Person   :director  

MilitaryUnit  --> MeanOfTransportation   :aircraftTrainer  

Person  --> Work   :created  

Person  --> SportsEvent   :competitionTitle  

Sport  --> Agent   :currentWorldChampion  

MusicalWork  --> Person   :lyrics  

Island  --> PopulatedPlace   :lowestState  

Person  --> Organisation   :employer  

Family  --> Person   :primogenitor  

Artist  --> Award   :tonyAward  

Person  --> Place   :bodyDiscovered  

EducationalInstitution  --> Person   :principal  

Actor  --> Award   :goldenCalfAward  

Person  --> Place   :residence  

Person  --> Project   :project  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

SpaceMission  --> MeanOfTransportation   :lunarRover  

Athlete  --> SportsTeam   :debutTeam  

AdministrativeRegion  --> Person   :landeshauptmann  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

Person  --> Person   :child  

Person  --> Person   :relative  

Island  --> PopulatedPlace   :capitalPlace  

Band  --> Person   :bandMember  

University  --> Person   :officerInCharge  

SportsEvent  --> Person   :medalist  

Artist  --> Award   :filmFareAward  

MilitaryUnit  --> Person   :secondCommander  

TelevisionShow  --> Person   :coExecutiveProducer  

Band  --> Person   :formerBandMember  

Scientist  --> Person   :doctoralStudent  

MeanOfTransportation  --> MeanOfTransportation   :relatedMeanOfTransportation  

Person  --> Sport   :sportDiscipline  

Saint  --> Person   :canonizedBy  

GrandPrix  --> Country   :secondDriverCountry  

Island  --> PopulatedPlace   :governmentPlace  

Animal  --> Place   :deathPlace  

TelevisionShow  --> Person   :showJudge  

Person  --> Person   :collaboration  

Place  --> River   :river  

Place  --> Place   :nextEntity  

Person  --> CareerStation   :careerStation  

Newspaper  --> Person   :associateEditor  

Country  --> TopLevelDomain   :topLevelDomain  

Olympics  --> Person   :torchBearer  

Island  --> Country   :governmentCountry  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Organisation  --> Organisation   :mergedWith  

Organisation  --> Person   :chairperson  

Film  --> Person   :specialEffects  

Athlete  --> SportsTeam   :club  

Organisation  --> PersonFunction   :leaderFunction  

Race  --> Person   :recentWinner  

Saint  --> Person   :beatifiedBy  

Woman  --> Person   :mother  

Place  --> Place   :northPlace  

PopulatedPlace  --> Demographics   :previousDemographics  

PopulatedPlace  --> Agglomeration   :agglomeration  

Artist  --> Award   :academyAward  

Artist  --> Award   :cesarAward  

Olympics  --> Person   :officialOpenedBy  

Person  --> EducationalInstitution   :college  

Person  --> RadioStation   :radio  

GrandPrix  --> Country   :firstDriverCountry  

Person  --> SKOSConcept   :world  

Athlete  --> SportsTeam   :juniorTeam  

Species  --> Species   :subTribus  

SportsTeam  --> Person   :manager  

Artist  --> Award   :goldenGlobeAward  

PopulatedPlace  --> Language   :officialLanguage  

Settlement  --> PopulatedPlace   :federalState  

PublicTransitSystem  --> MeanOfTransportation   :vehiclesInFleet  

Place  --> Place   :northWestPlace  

Person  --> SportsTeam   :teamManager  

Work  --> Place   :releaseLocation  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Saint  --> Organisation   :veneratedIn  

Person  --> Place   :announcedFrom  

SportsTeam  --> Person   :currentMember  

Place  --> Altitude   :altitude  

Person  --> SKOSConcept   :usopenWins  

YearInSpaceflight  --> Country   :countryWithFirstSatelliteLaunched  

Settlement  --> Place   :wilaya  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

WrittenWork  --> Person   :illustrator  

Athlete  --> SportsTeam   :teamCoached  

School  --> Person   :vicePrincipal  

LegalCase  --> Person   :attorneyGeneral  

River  --> PopulatedPlace   :mouthState  

Agent  --> Artist   :artPatron  

Agent  --> Event   :roleInEvent  

Place  --> Organisation   :governingBody  

Rocket  --> Country   :countryOrigin  

Film  --> Person   :editing  

Settlement  --> Person   :bourgmestre  

Person  --> MilitaryService   :militaryService  

Person  --> Person   :usurper  

Restaurant  --> Person   :chef  

Artwork  --> Person   :painter  

Place  --> Province   :province  

Woman  --> Person   :sister  

Family  --> Person   :headOfFamily  

Person  --> Person   :dubber  

Organisation  --> Person   :secretaryGeneral  

MilitaryUnit  --> Person   :notableCommander  

PopulatedPlace  --> Language   :regionalLanguage  

Athlete  --> Person   :trainer  

Place  --> Depth   :depths  

Person  --> EthnicGroup   :ethnicity  

Place  --> Place   :previousEntity  

Settlement  --> PopulatedPlace   :frazioni  

School  --> Person   :executiveHeadteacher  

Person  --> SKOSConcept   :britishWins  

Person  --> SportsTeam   :currentTeamManager  

RouteOfTransportation  --> Place   :routeEndLocation  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Organisation  --> City   :foundationPlace  

Island  --> PopulatedPlace   :highestRegion  

Place  --> Species   :tree  

MilitaryUnit  --> MeanOfTransportation   :aircraftTransport  

Species  --> Species   :tribus  

MilitaryUnit  --> MeanOfTransportation   :aircraftBomber  

Island  --> PopulatedPlace   :capitalRegion  

MilitaryUnit  --> MeanOfTransportation   :aircraftInterceptor  

Agent  --> TermOfOffice   :regionalCouncil  

YearInSpaceflight  --> Country   :countryWithFirstAstronaut  

Island  --> Place   :subdivisionName  

Place  --> Province   :provinceLink  

Place  --> Place   :southEastPlace  

Man  --> Person   :son  

Person  --> Tournament   :continentalTournament  

Athlete  --> Country   :sportCountry  

FictionalCharacter  --> Species   :enemy  

Place  --> PopulatedPlace   :nearestCity  

Work  --> Person   :author  

Person  --> Tournament   :olympicGames  

School  --> Person   :headteacher  

GrandPrix  --> Person   :fastestDriver  

Settlement  --> PopulatedPlace   :jointCommunity  

Film  --> Person   :cinematography  

Island  --> PopulatedPlace   :managementRegion  

PopulatedPlace  --> Population   :previousPopulation  

WrittenWork  --> Person   :prefaceBy  

MilitaryUnit  --> MeanOfTransportation   :aircraftRecon  

WrittenWork  --> Agent   :firstPublisher  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Person  --> Organisation   :federation  

Agent  --> TermOfOffice   :generalCouncil  

Actor  --> Award   :laurenceOlivierAward  

Canal  --> Place   :originalEndPoint  

Mountain  --> Person   :firstAscentPerson  

Actor  --> Award   :geminiAward  

Agent  --> Thing   :owns  

AdministrativeRegion  --> Place   :administrativeCenter  

River  --> PopulatedPlace   :sourceConfluenceState  

Person  --> PersonFunction   :otherOccupation  

Person  --> Person   :relation  

LegalCase  --> Person   :solicitorGeneral  

Work  --> Person   :composer  

Place  --> Altitude   :lowestAltitude  

TelevisionEpisode  --> Person   :guest  

FigureSkater  --> Person   :currentPartner  

Place  --> Place   :westPlace  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Place  --> Sea   :sea  

Actor  --> Award   :iftaAward  

TelevisionShow  --> Person   :creativeDirector  

Artist  --> Award   :emmyAward  

Race  --> Person   :firstWinner  

Settlement  --> Place   :settlementAttached  

Species  --> Species   :family  

Athlete  --> SportsTeam   :currentTeam  

Place  --> Place   :southWestPlace  

Man  --> Person   :uncle  

Organisation  --> Place   :regionServed  

HistoricBuilding  --> Person   :pastor  

Monarch  --> Person   :heir  

Road  --> PopulatedPlace   :ruralMunicipality  

Place  --> Area   :wholeArea  

Person  --> Person   :detractor  

Athlete  --> SportsTeam   :ncaaTeam  

Magazine  --> Person   :previousEditor  

Person  --> Work   :debutWork  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Place  --> PopulatedPlace   :regency  

Place  --> Species   :bird  

Language  --> PopulatedPlace   :spokenIn  

ResearchProject  --> Organisation   :projectCoordinator  

Place  --> Place   :subregion  

Organisation  --> Person   :trustee  

Place  --> Place   :eastPlace  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Athlete  --> SportsTeam   :formerTeam  

Work  --> Person   :translator  

Athlete  --> SportsTeam   :oldTeamCoached  

EducationalInstitution  --> Person   :rector  

MilitaryUnit  --> MeanOfTransportation   :aircraftPatrol  

PopulatedPlace  --> Area   :agglomerationArea  

SportsTeam  --> TeamMember   :currentTeamMember  

Settlement  --> PopulatedPlace   :geolocDepartment  

FictionalCharacter  --> Species   :entourage  

Work  --> Person   :coverArtist  

Place  --> Place   :closeTo  

Work  --> Agent   :publisher  

SportsTeam  --> Person   :generalManager  

Person  --> Country   :stateOfOrigin  

School  --> Person   :nobelLaureates  

Work  --> Person   :chiefEditor  

GrandPrix  --> Person   :firstDriver  

Newspaper  --> Person   :managingEditor  

Place  --> PopulatedPlace   :sovereignCountry  

GrandPrix  --> Person   :thirdDriver  

Comedian  --> Award   :olivierAward  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Person  --> Person   :friend  

Saint  --> PopulatedPlace   :beatifiedPlace  

Actor  --> Award   :naacpImageAward  

Settlement  --> Place   :daira  

Person  --> Person   :parent  

MilitaryUnit  --> PopulatedPlace   :garrison  

SoccerPlayer  --> SportsTeam   :trainerClub  

Person  --> Country   :nationality  

Person  --> EducationalInstitution   :almaMater  

Person  --> SKOSConcept   :endReign  

Cartoon  --> Agent   :animator  

Agent  --> Settlement   :hometown  

Athlete  --> SportsTeam   :youthClub  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Place  --> Place   :hasInsidePlace  

Place  --> Place   :mainIsland  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Olympics  --> Person   :olympicOathSwornByJudge  

Actor  --> Award   :goldenRaspberryAward  

Place  --> PersonFunction   :politicalLeader  

Man  --> Person   :brother  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

Saint  --> PopulatedPlace   :canonizedPlace  

Artist  --> Award   :grammyAward  

FigureSkater  --> Person   :formerCoach  

MilitaryUnit  --> Person   :fourthCommander  

Place  --> Place   :land  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

PoliticalParty  --> Person   :spokesperson  

PopulatedPlace  --> Population   :population  

Place  --> Place   :locatedInArea  

MilitaryUnit  --> MeanOfTransportation   :aircraftElectronic  

Agent  --> Ideology   :ideology  

Species  --> Taxon   :superFamily  

Person  --> Film   :movie  

ResearchProject  --> Organisation   :fundedBy  

River  --> PopulatedPlace   :mouthDistrict  

Scientist  --> Person   :academicAdvisor  

Species  --> Species   :superTribus  

Stream  --> Country   :sourceCountry  

ArchitecturalStructure  --> Organisation   :tenant  

ResearchProject  --> Organisation   :projectParticipant  

Animal  --> Place   :birthPlace  

Athlete  --> SportsTeam   :managerClub  

PopulatedPlace  --> Person   :leaderName  

MusicalWork  --> Agent   :artist  

Place  --> Species   :flower  

Actor  --> Award   :nationalFilmAward  

Ship  --> Place   :homeport  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Species  --> Taxon   :subFamily  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

Island  --> PopulatedPlace   :capitalDistrict  

Species  --> Species   :species  

Person  --> SpatialThing   :restingPlacePosition  

Place  --> PopulatedPlace   :lowestPlace  

Canal  --> Place   :originalStartPoint  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Island  --> PopulatedPlace   :governmentRegion  

Film  --> Person   :setDesigner  

Person  --> SKOSConcept   :mastersWins  

GrandPrix  --> Country   :fastestDriverCountry  

EducationalInstitution  --> Person   :alumni  

Person  --> Person   :colleague  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterObservation  

Person  --> Person   :student  

Department  --> PopulatedPlace   :subprefecture  

FigureSkater  --> Person   :formerChoreographer  

Athlete  --> SportsTeam   :coachClub  

PopulatedPlace  --> Place   :touristicSite  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopter  

Organisation  --> City   :locationCity  

RouteOfTransportation  --> Place   :routeStartLocation  

Person  --> Contest   :contest  

PopulatedPlace  --> Department   :department  

Scientist  --> Person   :notableStudent  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Place  --> Mountain   :lowestMountain  

Actor  --> Award   :screenActorsGuildAward  

Island  --> PopulatedPlace   :lowestRegion  

SoccerClub  --> Place   :ground  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterMultirole  

MilitaryUnit  --> MeanOfTransportation   :aircraftFighter  

Woman  --> Person   :daughter  

Canal  --> Person   :principalEngineer  

PopulatedPlace  --> Saint   :saint  

Person  --> Tournament   :worldTournament  

Artist  --> Award   :gaudiAward  

SkiResort  --> Place   :massif  

Person  --> Person   :cousurper  

TelevisionShow  --> Person   :storyEditor  

PopulatedPlace  --> Legislature   :legislature  

EducationalInstitution  --> Person   :actingHeadteacher  

River  --> Country   :sourceConfluenceCountry  

Organisation  --> Organisation   :childOrganisation  

Album  --> Person   :compiler  

Person  --> Person   :spouse  

Place  --> Place   :supply  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Artist  --> Award   :afiAward  

Comedian  --> Award   :britishComedyAwards  

River  --> PopulatedPlace   :mouthRegion  

Place  --> PopulatedPlace   :biggestCity  

Person  --> Place   :educationPlace  

Actor  --> Award   :arielAward  

Organisation  --> Person   :administrator  

Person  --> Tournament   :nationalTournament  

Person  --> Person   :opponent  

Organisation  --> Person   :ceo  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

PopulatedPlace  --> City   :capital  

Person  --> Person   :seiyu  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Man  --> Person   :father  

EducationalInstitution  --> Person   :dean  

Person  --> Person   :copilote  

Person  --> SportsLeague   :leagueManager  

Organisation  --> PopulatedPlace   :headquarter  

Place  --> RouteStop   :isRouteStop  

Scientist  --> Person   :doctoralAdvisor  

SportsEvent  --> Person   :bronzeMedalist  

GrandPrix  --> Person   :secondDriver  

Politician  --> Person   :prefect  

Place  --> SpatialThing   :lowestPosition  

Work  --> Person   :writer  

GrandPrix  --> SportsTeam   :secondTeam  

Person  --> List   :relatedFunctions  

EducationalInstitution  --> Person   :custodian  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterAttack  

Place  --> Place   :endPoint  

Film  --> Person   :makeupArtist  

Person  --> Diploma   :diploma  

```