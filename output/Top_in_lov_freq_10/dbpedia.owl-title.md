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



Place  --> Place   :locatedInArea  

EducationalInstitution  --> Person   :alumni  

PopulatedPlace  --> Agglomeration   :agglomeration  

Settlement  --> PopulatedPlace   :frazioni  

FigureSkater  --> Person   :formerChoreographer  

Organisation  --> City   :locationCity  

Person  --> SKOSConcept   :endReign  

WrittenWork  --> Agent   :firstPublisher  

School  --> Person   :headteacher  

SoccerClub  --> Place   :ground  

Species  --> Species   :fossil  

SportsTeam  --> Person   :currentMember  

Work  --> Person   :author  

Athlete  --> SportsTeam   :coachClub  

Island  --> PopulatedPlace   :highestRegion  

Athlete  --> SportsTeam   :oldTeamCoached  

Organisation  --> City   :foundationPlace  

Settlement  --> Person   :bourgmestre  

River  --> PopulatedPlace   :mouthRegion  

MilitaryUnit  --> MeanOfTransportation   :aircraftRecon  

GrandPrix  --> Country   :secondDriverCountry  

Olympics  --> Person   :olympicOathSwornByJudge  

Restaurant  --> Person   :chef  

Place  --> PopulatedPlace   :lowestPlace  

MilitaryUnit  --> MeanOfTransportation   :aircraftPatrol  

Work  --> Person   :composer  

Road  --> PopulatedPlace   :ruralMunicipality  

PopulatedPlace  --> Language   :regionalLanguage  

ResearchProject  --> Organisation   :projectCoordinator  

Species  --> Species   :tribus  

YearInSpaceflight  --> Country   :countryWithFirstAstronaut  

Artist  --> Award   :grammyAward  

Agent  --> Artist   :artPatron  

Broadcaster  --> PopulatedPlace   :broadcastArea  

TelevisionShow  --> Person   :presenter  

Agent  --> Settlement   :hometown  

Woman  --> Person   :mother  

Sport  --> Agent   :currentWorldChampion  

GrandPrix  --> Person   :fastestDriver  

Monarch  --> Person   :heir  

ResearchProject  --> Organisation   :projectParticipant  

Actor  --> Award   :goldenRaspberryAward  

TelevisionShow  --> Person   :showJudge  

Person  --> Film   :movie  

Family  --> Person   :headOfFamily  

YearInSpaceflight  --> Country   :countryWithFirstSatelliteLaunched  

Country  --> Country   :twinCountry  

GrandPrix  --> Person   :firstDriver  

EducationalInstitution  --> Person   :rector  

Film  --> Person   :specialEffects  

River  --> PopulatedPlace   :mouthDistrict  

Organisation  --> Person   :chaplain  

Olympics  --> Person   :torchBearer  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> Province   :province  

Person  --> SKOSConcept   :britishWins  

Person  --> EducationalInstitution   :college  

GrandPrix  --> Person   :secondDriver  

Canal  --> Place   :originalStartPoint  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> Place   :livingPlace  

PopulatedPlace  --> Population   :population  

Place  --> Place   :closeTo  

Film  --> Person   :director  

Species  --> Taxon   :superFamily  

Place  --> Place   :nextEntity  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

MilitaryUnit  --> MeanOfTransportation   :aircraftFighter  

SportsEvent  --> Person   :medalist  

Rocket  --> Country   :countryOrigin  

Place  --> Area   :wholeArea  

Family  --> Person   :lastFamilyMember  

Artist  --> Award   :emmyAward  

PopulatedPlace  --> Demographics   :previousDemographics  

HistoricBuilding  --> Person   :pastor  

Scientist  --> Person   :academicAdvisor  

PoliticalParty  --> Person   :spokesperson  

Actor  --> Award   :naacpImageAward  

Place  --> PopulatedPlace   :sovereignCountry  

Race  --> Person   :recentWinner  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Person  --> SKOSConcept   :world  

River  --> Place   :sourceConfluenceRegion  

GrandPrix  --> Country   :firstDriverCountry  

Organisation  --> Person   :administrator  

Artist  --> Award   :cesarAward  

Place  --> PopulatedPlace   :nearestCity  

GrandPrix  --> Country   :fastestDriverCountry  

Settlement  --> PopulatedPlace   :federalState  

Species  --> Species   :superTribus  

Place  --> PersonFunction   :politicalLeader  

Aircraft  --> Organisation   :aircraftUser  

River  --> PopulatedPlace   :sourceConfluenceState  

Person  --> Person   :spouse  

Place  --> Place   :northPlace  

Person  --> Tournament   :continentalTournament  

EducationalInstitution  --> Person   :principal  

Food  --> Person   :creatorOfDish  

Place  --> Altitude   :altitude  

Place  --> PopulatedPlace   :regency  

Settlement  --> Place   :settlementAttached  

Country  --> TopLevelDomain   :topLevelDomain  

Person  --> Tournament   :worldTournament  

Restaurant  --> Person   :headChef  

Place  --> Place   :southEastPlace  

Actor  --> Award   :nationalFilmAward  

Agent  --> Event   :roleInEvent  

Settlement  --> Place   :lowestPoint  

Person  --> SpatialThing   :restingPlacePosition  

Organisation  --> Person   :ceo  

Artist  --> Award   :afiAward  

Person  --> Person   :parent  

Sport  --> Person   :footedness  

MilitaryUnit  --> MeanOfTransportation   :aircraftInterceptor  

TelevisionShow  --> Person   :coExecutiveProducer  

Place  --> Species   :bird  

MilitaryUnit  --> MeanOfTransportation   :aircraftBomber  

Place  --> Place   :supply  

FigureSkater  --> Person   :formerCoach  

Saint  --> Person   :canonizedBy  

Actor  --> Award   :goldenCalfAward  

Place  --> Place   :eastPlace  

Saint  --> PopulatedPlace   :canonizedPlace  

Place  --> Depth   :depths  

Actor  --> Award   :geminiAward  

WrittenWork  --> Person   :illustrator  

Place  --> Mountain   :lowestMountain  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Ship  --> Place   :homeport  

PopulatedPlace  --> Area   :agglomerationArea  

Person  --> SportsTeam   :teamManager  

Stream  --> Country   :sourceCountry  

Person  --> SKOSConcept   :usopenWins  

Person  --> Person   :usurper  

PopulatedPlace  --> Population   :previousPopulation  

Actor  --> Award   :arielAward  

Athlete  --> SportsTeam   :ncaaTeam  

Person  --> Person   :sibling  

Work  --> Person   :mainCharacter  

MusicalWork  --> PopulatedPlace   :recordedIn  

Saint  --> Organisation   :veneratedIn  

Place  --> River   :river  

Species  --> Species   :family  

Person  --> Person   :friend  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Film  --> Person   :setDesigner  

PopulatedPlace  --> Legislature   :legislature  

Organisation  --> Organisation   :childOrganisation  

Work  --> Agent   :publisher  

Place  --> Place   :northEastPlace  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Agent  --> Ideology   :ideology  

Work  --> Agent   :producer  

Athlete  --> SportsTeam   :managerClub  

Olympics  --> Person   :olympicOathSwornBy  

ResearchProject  --> Organisation   :fundedBy  

Settlement  --> Place   :highestPoint  

Race  --> Person   :firstWinner  

Place  --> Place   :westPlace  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

PopulatedPlace  --> City   :capital  

PopulatedPlace  --> Person   :leaderName  

SoccerClub  --> Person   :clubsRecordGoalscorer  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Canal  --> Person   :principalEngineer  

Politician  --> Person   :prefect  

Newspaper  --> Person   :managingEditor  

River  --> PopulatedPlace   :mouthState  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Man  --> Person   :uncle  

Musical  --> Person   :musicBy  

RouteOfTransportation  --> Place   :routeEndLocation  

Place  --> PopulatedPlace   :biggestCity  

Person  --> Person   :student  

PopulatedPlace  --> Saint   :saint  

Artist  --> Award   :academyAward  

Person  --> Organisation   :federation  

Place  --> Organisation   :governingBody  

Actor  --> Award   :iftaAward  

SkiResort  --> Place   :massif  

MilitaryUnit  --> Person   :fourthCommander  

PopulatedPlace  --> Language   :officialLanguage  

Olympics  --> Person   :officialOpenedBy  

LegalCase  --> Person   :solicitorGeneral  

AdministrativeRegion  --> Place   :administrativeCenter  

Athlete  --> SportsTeam   :youthClub  

Saint  --> PopulatedPlace   :beatifiedPlace  

Newspaper  --> Person   :associateEditor  

PopulatedPlace  --> PopulatedPlace   :borough  

Person  --> Country   :stateOfOrigin  

VideoGame  --> Person   :gameArtist  

Person  --> Person   :seiyu  

Magazine  --> Person   :previousEditor  

Organisation  --> PopulatedPlace   :headquarter  

Person  --> SKOSConcept   :mastersWins  

Language  --> PopulatedPlace   :spokenIn  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

Person  --> SportsTeam   :currentTeamManager  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterMultirole  

Organisation  --> Person   :secretaryGeneral  

Place  --> Place   :mainIsland  

Work  --> Person   :writer  

Place  --> Place   :southWestPlace  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Film  --> Person   :cinematography  

Person  --> RadioStation   :radio  

Scientist  --> Person   :notableStudent  

FigureSkater  --> Person   :choreographer  

Man  --> Person   :brother  

Person  --> CareerStation   :careerStation  

Place  --> Altitude   :lowestAltitude  

Person  --> MilitaryService   :militaryService  

ArchitecturalStructure  --> Organisation   :tenant  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Person  --> List   :relatedFunctions  

Person  --> Person   :dubber  

SportsTeam  --> Person   :generalManager  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Person  --> Person   :copilote  

Athlete  --> SportsTeam   :teamCoached  

Settlement  --> Place   :wilaya  

Athlete  --> SportsTeam   :nflTeam  

Place  --> Place   :hasInsidePlace  

MusicalWork  --> Person   :lyrics  

Athlete  --> Person   :trainer  

Person  --> Person   :opponent  

TelevisionShow  --> Person   :creativeDirector  

Organisation  --> Person   :superintendent  

FigureSkater  --> Person   :currentPartner  

Island  --> PopulatedPlace   :capitalPlace  

Island  --> PopulatedPlace   :lowestState  

Man  --> Person   :father  

Species  --> Species   :species  

Work  --> Person   :chiefEditor  

Island  --> PopulatedPlace   :governmentRegion  

Album  --> Person   :compiler  

FictionalCharacter  --> Species   :enemy  

Island  --> Place   :subdivisionName  

School  --> Person   :vicePrincipal  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterObservation  

Place  --> RouteStop   :isRouteStop  

Person  --> Place   :residence  

Person  --> Person   :relative  

Canal  --> Place   :originalEndPoint  

SoccerPlayer  --> SportsTeam   :trainerClub  

Agent  --> TermOfOffice   :regionalCouncil  

Island  --> Country   :governmentCountry  

Person  --> EducationalInstitution   :almaMater  

GrandPrix  --> Person   :thirdDriver  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopter  

Organisation  --> Organisation   :mergedWith  

MilitaryUnit  --> Person   :secondCommander  

Person  --> SKOSConcept   :startReign  

Place  --> SpatialThing   :lowestPosition  

Actor  --> Award   :laurenceOlivierAward  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Athlete  --> SportsTeam   :club  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Person  --> Person   :collaboration  

Scientist  --> Person   :doctoralStudent  

School  --> Person   :executiveHeadteacher  

Animal  --> Place   :deathPlace  

Species  --> Species   :subTribus  

FictionalCharacter  --> Species   :entourage  

Place  --> Province   :provinceLink  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Person  --> SportsEvent   :competitionTitle  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Artist  --> Award   :goldenGlobeAward  

Person  --> Person   :child  

MilitaryUnit  --> MeanOfTransportation   :aircraftTransport  

Place  --> Place   :hasOutsidePlace  

Island  --> PopulatedPlace   :lowestRegion  

Place  --> Species   :tree  

Person  --> Place   :bodyDiscovered  

Person  --> PersonFunction   :otherOccupation  

Athlete  --> SportsTeam   :currentTeam  

Place  --> PopulatedPlace   :district  

MeanOfTransportation  --> MeanOfTransportation   :relatedMeanOfTransportation  

Man  --> Person   :son  

Island  --> PopulatedPlace   :managementRegion  

Work  --> Person   :translator  

Organisation  --> PersonFunction   :leaderFunction  

Place  --> Place   :previousEntity  

SportsEvent  --> Person   :bronzeMedalist  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterTransport  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

Person  --> EthnicGroup   :ethnicity  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

EducationalInstitution  --> Person   :dean  

Person  --> Work   :debutWork  

Artwork  --> Person   :painter  

Athlete  --> Country   :sportCountry  

Work  --> Person   :coverArtist  

MilitaryUnit  --> Person   :notableCommander  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterAttack  

Person  --> Place   :educationPlace  

EducationalInstitution  --> Person   :custodian  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Animal  --> Place   :birthPlace  

Artist  --> Award   :filmFareAward  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

River  --> Country   :sourceConfluenceCountry  

PopulatedPlace  --> Department   :department  

Person  --> Person   :cousurper  

Work  --> Place   :releaseLocation  

Settlement  --> PopulatedPlace   :jointCommunity  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Actor  --> Award   :screenActorsGuildAward  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

Film  --> Person   :makeupArtist  

MilitaryUnit  --> MeanOfTransportation   :aircraftTrainer  

TelevisionEpisode  --> Person   :guest  

Person  --> Place   :announcedFrom  

Agent  --> Thing   :owns  

MusicalWork  --> Agent   :artist  

Woman  --> Person   :sister  

Species  --> Taxon   :subFamily  

Place  --> Place   :land  

University  --> Person   :officerInCharge  

Country  --> Continent   :continent  

LegalCase  --> Person   :attorneyGeneral  

TelevisionShow  --> Person   :storyEditor  

Athlete  --> SportsTeam   :formerTeam  

Artist  --> Award   :gaudiAward  

Island  --> PopulatedPlace   :capitalDistrict  

Place  --> Place   :northWestPlace  

Comedian  --> Award   :olivierAward  

Person  --> Country   :nationality  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Agent  --> TermOfOffice   :generalCouncil  

Mountain  --> Person   :firstAscentPerson  

Cartoon  --> Agent   :animator  

EducationalInstitution  --> Person   :actingHeadteacher  

Place  --> Place   :subregion  

Person  --> Organisation   :employer  

Comedian  --> Award   :britishComedyAwards  

Athlete  --> SportsTeam   :debutTeam  

PopulatedPlace  --> Person   :viceLeader  

Person  --> Contest   :contest  

Family  --> Person   :primogenitor  

AdministrativeRegion  --> Person   :landeshauptmann  

Department  --> PopulatedPlace   :subprefecture  

Person  --> Person   :detractor  

SpaceMission  --> MeanOfTransportation   :lunarRover  

PopulatedPlace  --> Place   :touristicSite  

Person  --> SportsLeague   :leagueManager  

Person  --> Tournament   :olympicGames  

Person  --> Work   :created  

Scientist  --> Person   :doctoralAdvisor  

Island  --> PopulatedPlace   :governmentPlace  

Place  --> Species   :flower  

Woman  --> Person   :daughter  

Place  --> Sea   :sea  

Athlete  --> SportsTeam   :juniorTeam  

SportsTeam  --> Person   :manager  

Person  --> Project   :project  

Organisation  --> Person   :chairperson  

Person  --> Person   :colleague  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Organisation  --> Place   :regionServed  

Place  --> Place   :endPoint  

Band  --> Person   :formerBandMember  

Person  --> Person   :relation  

Settlement  --> Place   :daira  

SportsTeam  --> TeamMember   :currentTeamMember  

Film  --> Person   :editing  

Artist  --> Award   :tonyAward  

GrandPrix  --> SportsTeam   :secondTeam  

RouteOfTransportation  --> Place   :routeStartLocation  

Band  --> Person   :bandMember  

MilitaryUnit  --> MeanOfTransportation   :aircraftElectronic  

Person  --> Sport   :sportDiscipline  

Settlement  --> PopulatedPlace   :largestMetro  

Island  --> PopulatedPlace   :capitalRegion  

PublicTransitSystem  --> MeanOfTransportation   :vehiclesInFleet  

MilitaryUnit  --> PopulatedPlace   :garrison  

Person  --> Tournament   :nationalTournament  

Organisation  --> Person   :trustee  

WrittenWork  --> Person   :prefaceBy  

Person  --> Diploma   :diploma  

Saint  --> Person   :beatifiedBy  

School  --> Person   :nobelLaureates  

```