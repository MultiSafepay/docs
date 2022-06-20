---
title: 'Verbinden von unzugeordneten Banküberweisungen'
category: 6298bd782d1cf4006032e765
order: 104
hidden: true
parentDoc: 62a728d48b97080046c1d220
slug: 'unzugeordneten-banküberweisungen'
---

Wenn MultiSafepay eine Banküberweisung von Kund:innen erhält, verbinden wir diese aufgrund der angegebenen Zahlungsdetails automatisch mit der entsprechenden Transaktion in unserem System. 

Falls die automatische Zuordnung nicht funktioniert, verbinden wir die Zahlung manuell basierend auf:

- Betrag und Zahlungsreferenz, **oder**
- Betrag und Kontonummer des Kunden/der Kundin

Die häufigsten Ursachen für eine nicht geglückte Zuordnung sind: 

## Zahlungsdetails inkorrekt, fehlend, oder inkorrekt formatiert

Wir können eine Zahlung nicht zuordnen, wenn ein Kunde/eine Kundin:

- den falschen Betrag überweist
- verschiedene Bestellungen in einer Zahlung zusammenfasst
- die Zahlungsreferenz falsch eingibt oder Wörter hinzufügt, z.B. “Zahlungs-ID 5213 0452 1234 5670”
- anstatt der Zahlungsreferenz die Bestellnummer angibt 

Manchmal fügt die Bank des Kunden/der Kundin Kommentare zur Überweisung hinzu.

## Transaktion nicht generiert

Der Kunde/die Kundin hat eine Überweisung getätigt, jedoch nicht:

- die Bestellung in Ihrem Onlinehandel aufgegeben, **oder**
- **Bestätigen** auf der MultiSafepay Zahlungsseite geklickt (redirect orders).

Dies bedeutet, dass die Transaktion nicht erfolgreich in unserem System generiert werden konnte.

Um die Transaktion erneut zu erstellen, überprüfen Sie, ob ein [Zahlungslink](/account/payment-links/) generiert wurde: 

## Zahlungslink wurde generiert

1. Klicken Sie auf den Link, um die Zahlungsseite zu öffnen. 
2. Klicken Sie auf **Banküberweisung**.
3. Falls der Kunde/die Kundin das Feld **Kontonummer** nicht ausgefüllt hat, füllen Sie es aus (soweit bekannt), um uns dabei zu helfen, die Transaktion zuzuordnen. 
4. Klicken Sie auf **Bestätigen**, um die Transaktion in unserem System zu generieren. 

## Zahlungslink wurde nicht generiert

1. [Erstellen Sie einen Zahlungslink manuell](/account/payment-links/#generating-payment-links).
2. Nennen Sie den Kundennamen und die Bestellnummer in der Beschreibung
3. Klicken Sie auf **Banküberweisung**.
4. Füllen Sie die Kontonummer des Kunden/der Kundin ein (soweit bekannt), um uns dabei zu helfen, die Transaktion zuzuordnen.
5. Klicken Sie auf **Bestätigen**, um die Transaktion in unserem System zu generieren. 

**Bitte beachten:** Die Bestellnummer muss für jeden Zahlungslink einzigartig sein.

> 💬  Support
> Schicken Sie eine E-mail an unser Support-Team an <support@multisafepay.com>
