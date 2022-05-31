---
title : "Ongematchte bankoverschrijvingen"
meta_title: "Ongematchte bankoverschrijvingen - MultiSafepay Docs"
read_more: "."
weight: 1
url: '/bank-transfer/ongematchte-bankoverschrijvingen/'
tags: "hidden"
---

Wanneer MultiSafepay een bankoverschrijving ontvangt van een klant, matchen we die automatisch aan de bijbehorende transactie in ons systeem. We doen dit op basis van:

 - Het bedrag en betalingskenmerk, **of**
 - Het bedrag en bankrekeningnummer van de klant

Wanneer we er niet in slagen om de transacties automatisch te matchen, proberen we het handmatig.

De twee meest voorkomende redenen waarom het automatische matchen soms niet lukt, zijn als volgt:

**De betalingsgegevens missen, zijn incorrect, of verkeerd geformatteerd**

We kunnen de betaling niet matchen als de klant:

- Het verkeerde bedrag overmaakt
- Meerdere bestellingen in één overschrijving betaalt
- Het betalingskenmerk incorrect opgeeft, of er iets aan toevoegt, zoals "Betaling 5213 0452 1234 5670"
- Het ordernummer opgeeft in plaats van het betalingskenmerk

**De transactie bestaat niet in ons systeem**

De klant heeft wél een bankoverschrijving gedaan, maar heeft niet:
    
- Een bestelling bij u geplaatst, **of**
- Geklikt op **Bevestig** op de MultiSafepay betaalpagina (redirect orders). 

Beide gevallen leiden ertoe dat er geen transactie bestaat in ons systeem waarmee de overschrijving gematcht kan worden.

Om een transactie aan te maken kunt u gebruik maken van onze betaallinks ([payment links](/payment-links/)):

**Er bestaat al een betaallink**

1. Klik op de link om de betaalpagina te openen. 
2. Klik op **Bankoverschrijving**.
3. Als de klant het veld **Bankrekeningnummer** niet heeft ingevuld, vul dan het bankrekeningnummer van de klant in (indien bij u bekend).
4. Klik op **Bevestig** om de transactie aan te maken in ons systeem.

**Er bestaat nog geen betaallink**

1. [Genereer handmatig een betaallink](/payment-links/generating-links/). 
2. Voeg de naam van de klant en het ordernummer toe aan de beschrijving (voor uw eigen administratie). 
3. Klik op **Bankoverschrijving**.
4. Voeg het bankrekeningnummer van de klant toe (indien bij u bekend), zodat we de betaling gemakkelijker kunnen matchen.
5. Klik op **Bevestig** om de transactie aan te maken in ons systeem.

**Opmerking:** Iedere betaallink heeft een uniek order ID nodig.

**Ondersteuning**

Email ons Support Team via <support@multisafepay.com>