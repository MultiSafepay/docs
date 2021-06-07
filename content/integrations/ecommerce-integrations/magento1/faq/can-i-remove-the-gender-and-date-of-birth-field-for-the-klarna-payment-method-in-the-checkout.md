---
title : "Can I remove the Klarna fields \"Gender\" and \"Date of birth\" in my checkout?"
meta_title: "Magento 1 plugin remove Klarna fields - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: [/integrations/magento1/faq/can-i-remove-the-gender-and-date-of-birth-field-for-the-klarna-payment-method-in-the-checkout/]
---

Klarna needs the gender and date of birth of the customer. By default, the customer fills in this information in the Magento checkout in the Klarna payment method fields. The gender is automatically filled by the core Magento field.

You can disable both fields on the Klarna payment method and then the customer will fill in this information on the MultiSafepay payment pages.

This change is only for Magento developers. We strongly advise to test the change and place the change in the local folder.

Steps:

1. Open app\code\community\MultiSafepay\Msp\Model\Gateway\Klarna.php
2. Comment this line `protected $_formBlockType = 'msp/klarna';`
3. Save the file, clear the cache and test the change.
