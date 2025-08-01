---
title: Ongematchte bankoverschrijvingen
category:
  uri: Payment methods
slug: ongematchte-bankoverschrijvingen
position: 103
privacy:
  view: anyone_with_link
parent:
  uri: banking-methods
---

Wanneer MultiSafepay een bankoverschrijving ontvangt van een klant, matchen we die automatisch aan de bijbehorende transactie in ons systeem. We doen dit op basis van:

 - Het bedrag en betalingskenmerk, **of**
 - Het bedrag en bankrekeningnummer van de klant

Wanneer we er niet in slagen om de transacties automatisch te matchen, proberen we het handmatig.

De twee meest voorkomende redenen waarom het automatische matchen soms niet lukt, zijn als volgt:

## De betalingsgegevens missen, zijn incorrect, of verkeerd geformatteerd

We kunnen de betaling niet matchen als de klant:

- Het verkeerde bedrag overmaakt
- Meerdere bestellingen in één overschrijving betaalt
- Het betalingskenmerk incorrect opgeeft, of er iets aan toevoegt, zoals "Betaling 5213 0452 1234 5670"
- Het ordernummer opgeeft in plaats van het betalingskenmerk

## De transactie bestaat niet in ons systeem

De klant heeft wél een bankoverschrijving gedaan, maar heeft niet:
    
- Een bestelling bij u geplaatst, **of**
- Geklikt op **Bevestig** op de MultiSafepay betaalpagina (<<glossary:redirect>> orders). 

Beide gevallen leiden ertoe dat er geen transactie bestaat in ons systeem waarmee de overschrijving gematcht kan worden.

Om niet gematchede betalingen op te lossen, controleer of er een [transactie](/docs/payment-links/) aangemaakt is:

## Transactie aangemaakt

1. Klik op de link om de betaalpagina te openen. 
2. Klik op **Bankoverschrijving**.
3. Als de klant het veld **Bankrekeningnummer** niet heeft ingevuld, vul dan het bankrekeningnummer van de klant in (indien bij u bekend).
4. Klik op **Bevestig** om de transactie aan te maken in ons systeem.

## Transactie niet aangemaakt

1. [Genereer handmatig een betaallink](/docs/payment-links/). 
2. Voeg de naam van de klant en het ordernummer toe aan de beschrijving (voor uw eigen administratie). 
3. Klik op **Bankoverschrijving**.
4. Voeg het bankrekeningnummer van de klant toe (indien bij u bekend), zodat we de betaling gemakkelijker kunnen matchen.
5. Klik op **Bevestig** om de transactie aan te maken in ons systeem.

**Opmerking:** Iedere betaallink heeft een uniek order ID nodig.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Ondersteuning</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
