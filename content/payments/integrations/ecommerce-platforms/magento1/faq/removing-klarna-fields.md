---
title : "Removing the Klarna Gender and Date of birth fields at checkout"
meta_title: "Magento 1 plugin - Removing Klarna fields - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: 
    - /integrations/magento1/faq/can-i-remove-the-gender-and-date-of-birth-field-for-the-klarna-payment-method-in-the-checkout/
---

Klarna requires the customer's gender and date of birth. By default, the customer fills in this information in the Magento checkout in the Klarna payment method fields. The gender is automatically filled by the core Magento field.

You can disable both fields on the Klarna payment method. The customer then enters this information on the MultiSafepay payment page.

This change is only for Magento developers. We recommend testing the change and placing it in your local folder.

To disable Klarna gender and date of birth fields, follow these steps:

1. Open `app\code\community\MultiSafepay\Msp\Model\Gateway\Klarna.php`.
2. Comment this line `protected $_formBlockType = 'msp/klarna';`
3. Save the file.
4. Clear your cache.
5. Test the change.
