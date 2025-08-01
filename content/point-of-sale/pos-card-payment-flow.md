---
title: 'POS card payment flow'
category: 6477597e0e2961004638cd5d
order: 3
hidden: true
slug: 'pos-card-payment-flow'

---
POS payments can done be with or without verification. This depends on various parties, including the acquirer's host configuration.

Without verification > Issuer may accept or soft decline it

## Soft declined

For some card transactions without verfication, inserting the PIN can be requested by the issuer.

by different parties: the terminal, the card, or the issuer. Example: the issuer can block the original transaction due to an elevated amount.

### Transaction history

When payment is soft declined, typically in the case of contactless, you will see two transactions reflected in your Merchant Dashboard:

* the original transaction: in status *declined* with error code 65, 71.
* the "step up" transaction: in status *completed* or *cancelled*, depending on the outcome.

### Display on terminal

The customer does not see any declined message on the terminal for the inital payment attempt; only the PIN requirement is displayed on the device. The process stays frictionless.

### Notifications

If you are using our Event Notifications, you should receive three types of notifications:

* Status *declined* for the original transaction;
* status *initialized* for the next transaction,
* and then status *completed* once the payment was successful.

In this case, *declined* is not the final status. After a Declined notification, you should always receive either the Completed or Cancelled final notifications for that payment.

Note: if you use the event notification system (eventstreamURL), do not stop listening to the updates after the *Declined* status, as this at times is not the final status per order ID.