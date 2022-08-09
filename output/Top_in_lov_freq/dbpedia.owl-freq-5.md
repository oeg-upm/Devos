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



Person  --> Work   :debutWork  

GrandPrix  --> Person   :secondDriver  

Artist  --> Award   :filmFareAward  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

Mountain  --> Person   :firstAscentPerson  

Place  --> Place   :supply  

Place  --> Place   :endPoint  

Place  --> Place   :locatedInArea  

Race  --> Person   :firstWinner  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> SportsLeague   :leagueManager  

Artist  --> Award   :academyAward  

Work  --> Place   :releaseLocation  

Person  --> Place   :bodyDiscovered  

Band  --> Person   :bandMember  

Settlement  --> Place   :highestPoint  

Person  --> Person   :spouse  

WrittenWork  --> Person   :prefaceBy  

PoliticalParty  --> Person   :spokesperson  

Person  --> Work   :created  

RouteOfTransportation  --> Place   :routeStartLocation  

Canal  --> Place   :originalStartPoint  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Monarch  --> Person   :heir  

AdministrativeRegion  --> Person   :landeshauptmann  

Place  --> PersonFunction   :politicalLeader  

Olympics  --> Person   :officialOpenedBy  

Place  --> Place   :closeTo  

Person  --> Person   :detractor  

Person  --> Person   :relation  

Athlete  --> SportsTeam   :club  

Musical  --> Person   :musicBy  

Organisation  --> Person   :administrator  

Place  --> Area   :wholeArea  

Settlement  --> PopulatedPlace   :geolocDepartment  

SportsTeam  --> Person   :generalManager  

Person  --> Organisation   :federation  

Artist  --> Award   :afiAward  

HistoricBuilding  --> Person   :pastor  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Athlete  --> SportsTeam   :formerTeam  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

PopulatedPlace  --> Language   :officialLanguage  

Comedian  --> Award   :olivierAward  

Race  --> Person   :recentWinner  

Place  --> Place   :mainIsland  

Place  --> Province   :province  

Person  --> Place   :residence  

Person  --> EducationalInstitution   :almaMater  

Island  --> PopulatedPlace   :governmentPlace  

Work  --> Person   :coverArtist  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Place  --> Place   :westPlace  

Canal  --> Place   :originalEndPoint  

Athlete  --> SportsTeam   :oldTeamCoached  

Person  --> MilitaryService   :militaryService  

PopulatedPlace  --> Person   :leaderName  

River  --> PopulatedPlace   :mouthState  

EducationalInstitution  --> Person   :actingHeadteacher  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Person  --> Diploma   :diploma  

TelevisionShow  --> Person   :storyEditor  

Newspaper  --> Person   :associateEditor  

MusicalWork  --> PopulatedPlace   :recordedIn  

GrandPrix  --> Person   :thirdDriver  

Place  --> Place   :northPlace  

Artist  --> Award   :cesarAward  

Woman  --> Person   :sister  

Politician  --> Person   :prefect  

School  --> Person   :nobelLaureates  

Woman  --> Person   :mother  

MilitaryUnit  --> PopulatedPlace   :garrison  

Island  --> PopulatedPlace   :governmentRegion  

River  --> PopulatedPlace   :mouthDistrict  

Person  --> SKOSConcept   :mastersWins  

Person  --> Film   :movie  

LegalCase  --> Person   :attorneyGeneral  

PopulatedPlace  --> Legislature   :legislature  

PopulatedPlace  --> Agglomeration   :agglomeration  

Actor  --> Award   :naacpImageAward  

Person  --> Organisation   :employer  

MilitaryUnit  --> Person   :fourthCommander  

FigureSkater  --> Person   :choreographer  

Person  --> Person   :seiyu  

Scientist  --> Person   :doctoralStudent  

Work  --> Person   :author  

SportsTeam  --> Person   :currentMember  

Person  --> Person   :cousurper  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Island  --> PopulatedPlace   :capitalPlace  

Person  --> List   :relatedFunctions  

PopulatedPlace  --> PopulatedPlace   :principalArea  

River  --> Place   :sourceConfluenceRegion  

Work  --> Person   :writer  

PopulatedPlace  --> Demographics   :previousDemographics  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Place  --> Species   :tree  

Island  --> PopulatedPlace   :capitalDistrict  

Settlement  --> Place   :daira  

SkiResort  --> Place   :massif  

Broadcaster  --> PopulatedPlace   :broadcastArea  

PopulatedPlace  --> Place   :touristicSite  

Settlement  --> Place   :wilaya  

Man  --> Person   :father  

River  --> PopulatedPlace   :sourceConfluenceState  

Person  --> Country   :stateOfOrigin  

PopulatedPlace  --> Person   :viceLeader  

Actor  --> Award   :geminiAward  

Man  --> Person   :brother  

Organisation  --> Person   :chairperson  

FigureSkater  --> Person   :formerChoreographer  

Place  --> PopulatedPlace   :district  

Family  --> Person   :lastFamilyMember  

Person  --> SportsEvent   :competitionTitle  

Actor  --> Award   :screenActorsGuildAward  

Actor  --> Award   :arielAward  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Work  --> Person   :mainCharacter  

SportsEvent  --> Person   :medalist  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

Place  --> Place   :southEastPlace  

MilitaryUnit  --> Person   :notableCommander  

Person  --> SKOSConcept   :endReign  

Film  --> Person   :editing  

River  --> PopulatedPlace   :mouthRegion  

Place  --> PopulatedPlace   :nearestCity  

Scientist  --> Person   :academicAdvisor  

Athlete  --> SportsTeam   :youthClub  

Place  --> PopulatedPlace   :biggestCity  

Athlete  --> SportsTeam   :managerClub  

Restaurant  --> Person   :headChef  

Island  --> PopulatedPlace   :capitalRegion  

PopulatedPlace  --> Department   :department  

SoccerPlayer  --> SportsTeam   :trainerClub  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

Person  --> RadioStation   :radio  

Animal  --> Place   :birthPlace  

Organisation  --> Person   :chaplain  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Artist  --> Award   :tonyAward  

Artwork  --> Person   :painter  

Language  --> PopulatedPlace   :spokenIn  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Person  --> Person   :dubber  

Actor  --> Award   :laurenceOlivierAward  

Place  --> SpatialThing   :lowestPosition  

GrandPrix  --> SportsTeam   :secondTeam  

GrandPrix  --> Person   :firstDriver  

EducationalInstitution  --> Person   :custodian  

Person  --> SKOSConcept   :britishWins  

Organisation  --> PopulatedPlace   :headquarter  

Person  --> Country   :nationality  

Work  --> Person   :composer  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Place  --> Sea   :sea  

Artist  --> Award   :gaudiAward  

Film  --> Person   :director  

Person  --> Person   :opponent  

Place  --> Place   :land  

Person  --> Tournament   :worldTournament  

Scientist  --> Person   :notableStudent  

Department  --> PopulatedPlace   :subprefecture  

PopulatedPlace  --> Population   :population  

Family  --> Person   :primogenitor  

Man  --> Person   :uncle  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

WrittenWork  --> Person   :illustrator  

Place  --> Place   :nextEntity  

Island  --> PopulatedPlace   :lowestState  

PopulatedPlace  --> Language   :regionalLanguage  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

SportsTeam  --> Person   :manager  

Place  --> Place   :northEastPlace  

University  --> Person   :officerInCharge  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Person  --> Tournament   :nationalTournament  

Band  --> Person   :formerBandMember  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

Restaurant  --> Person   :chef  

Ship  --> Place   :homeport  

MusicalWork  --> Person   :lyrics  

Person  --> EducationalInstitution   :college  

Olympics  --> Person   :torchBearer  

Place  --> PopulatedPlace   :sovereignCountry  

Place  --> Altitude   :lowestAltitude  

Woman  --> Person   :daughter  

School  --> Person   :vicePrincipal  

Person  --> Person   :colleague  

PopulatedPlace  --> Saint   :saint  

Actor  --> Award   :iftaAward  

AdministrativeRegion  --> Place   :administrativeCenter  

Person  --> Tournament   :olympicGames  

Person  --> Person   :copilote  

FigureSkater  --> Person   :formerCoach  

SportsTeam  --> TeamMember   :currentTeamMember  

Place  --> Species   :bird  

TelevisionShow  --> Person   :creativeDirector  

MilitaryUnit  --> Person   :secondCommander  

Person  --> Person   :student  

Work  --> Person   :translator  

Film  --> Person   :setDesigner  

Saint  --> PopulatedPlace   :canonizedPlace  

Road  --> PopulatedPlace   :ruralMunicipality  

Place  --> River   :river  

Person  --> PersonFunction   :otherOccupation  

EducationalInstitution  --> Person   :rector  

Place  --> Organisation   :governingBody  

Person  --> Person   :relative  

Athlete  --> Person   :trainer  

PopulatedPlace  --> PopulatedPlace   :borough  

Organisation  --> Person   :trustee  

TelevisionShow  --> Person   :showJudge  

Place  --> Altitude   :altitude  

Settlement  --> Place   :lowestPoint  

Settlement  --> PopulatedPlace   :jointCommunity  

Person  --> Tournament   :continentalTournament  

Athlete  --> SportsTeam   :debutTeam  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Island  --> PopulatedPlace   :highestRegion  

Organisation  --> Person   :secretaryGeneral  

Actor  --> Award   :goldenRaspberryAward  

Athlete  --> SportsTeam   :teamCoached  

Person  --> Place   :educationPlace  

Scientist  --> Person   :doctoralAdvisor  

Place  --> Place   :southWestPlace  

Artist  --> Award   :emmyAward  

Animal  --> Place   :deathPlace  

EducationalInstitution  --> Person   :alumni  

Organisation  --> Person   :ceo  

Settlement  --> PopulatedPlace   :largestMetro  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Food  --> Person   :creatorOfDish  

Album  --> Person   :compiler  

Family  --> Person   :headOfFamily  

GrandPrix  --> Person   :fastestDriver  

Person  --> Person   :collaboration  

School  --> Person   :executiveHeadteacher  

Person  --> Place   :livingPlace  

Island  --> PopulatedPlace   :managementRegion  

Saint  --> Person   :beatifiedBy  

Person  --> SKOSConcept   :world  

Place  --> Place   :hasOutsidePlace  

Olympics  --> Person   :olympicOathSwornBy  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Film  --> Person   :cinematography  

Person  --> Person   :friend  

Place  --> Place   :northWestPlace  

Place  --> PopulatedPlace   :regency  

Person  --> CareerStation   :careerStation  

Place  --> Place   :hasInsidePlace  

Canal  --> Person   :principalEngineer  

FigureSkater  --> Person   :currentPartner  

Settlement  --> PopulatedPlace   :frazioni  

Settlement  --> Place   :settlementAttached  

Film  --> Person   :makeupArtist  

Place  --> Species   :flower  

Island  --> Place   :subdivisionName  

Person  --> SportsTeam   :teamManager  

Olympics  --> Person   :olympicOathSwornByJudge  

Place  --> Province   :provinceLink  

Artist  --> Award   :goldenGlobeAward  

EducationalInstitution  --> Person   :principal  

Athlete  --> SportsTeam   :juniorTeam  

Settlement  --> PopulatedPlace   :federalState  

Person  --> Sport   :sportDiscipline  

Person  --> SKOSConcept   :startReign  

Person  --> Person   :child  

TelevisionEpisode  --> Person   :guest  

SoccerClub  --> Place   :ground  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Organisation  --> Person   :superintendent  

Magazine  --> Person   :previousEditor  

Person  --> SKOSConcept   :usopenWins  

LegalCase  --> Person   :solicitorGeneral  

EducationalInstitution  --> Person   :dean  

Place  --> Place   :previousEntity  

Person  --> SportsTeam   :currentTeamManager  

Place  --> Place   :subregion  

Athlete  --> SportsTeam   :coachClub  

VideoGame  --> Person   :gameArtist  

Organisation  --> Place   :regionServed  

TermOfOffice  --> Person   :presidentGeneralCouncil  

PopulatedPlace  --> Area   :agglomerationArea  

Person  --> EthnicGroup   :ethnicity  

TelevisionShow  --> Person   :coExecutiveProducer  

PopulatedPlace  --> Population   :previousPopulation  

Athlete  --> SportsTeam   :currentTeam  

Person  --> Place   :announcedFrom  

Place  --> Depth   :depths  

Place  --> Place   :eastPlace  

Man  --> Person   :son  

PopulatedPlace  --> City   :capital  

Place  --> RouteStop   :isRouteStop  

Island  --> PopulatedPlace   :lowestRegion  

Athlete  --> SportsTeam   :nflTeam  

Actor  --> Award   :goldenCalfAward  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Person  --> Person   :parent  

Settlement  --> Person   :bourgmestre  

TelevisionShow  --> Person   :presenter  

Saint  --> Person   :canonizedBy  

RouteOfTransportation  --> Place   :routeEndLocation  

Saint  --> PopulatedPlace   :beatifiedPlace  

Actor  --> Award   :nationalFilmAward  

Newspaper  --> Person   :managingEditor  

Work  --> Person   :chiefEditor  

Person  --> Person   :sibling  

Person  --> SpatialThing   :restingPlacePosition  

Place  --> Mountain   :lowestMountain  

School  --> Person   :headteacher  

Comedian  --> Award   :britishComedyAwards  

Person  --> Contest   :contest  

Sport  --> Person   :footedness  

SportsEvent  --> Person   :bronzeMedalist  

Artist  --> Award   :grammyAward  

Athlete  --> SportsTeam   :ncaaTeam  

Person  --> Project   :project  

Film  --> Person   :specialEffects  

```