---
title : "Can I remove the Klarna fields \"Gender\" and \"Date of birth\" in my checkout?"
meta_title: "Magento 1 plugin remove Klarna fields - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

Klarna needs the gender and date of birth of the customer. By default, the customer fills in this information in the Magento checkout in the Klarna payment method fields. The gender is automatically filled by the core Magento field.

You can disable both fields on the Klarna payment method and then the customer will fill in this information on the MultiSafepay payment pages.

This change is only for Magento developers. We strongly advise to test the change and place the change in the local folder.

Steps:

1. Open app\code\community\MultiSafepay\Msp\Model\Gateway\Klarna.php
2. Comment this line `protected $_formBlockType = 'msp/klarna';`
3. Save the file, clear the cache and test the change.
