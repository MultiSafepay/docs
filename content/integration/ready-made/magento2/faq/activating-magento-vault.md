---
title : "Using Magento Vault for Instant Purchase"
meta_title: "Magento 2 plugin - Activating Magento Vault - MultiSafepay Docs"
layout: "faqdetail"
read_more: "."
url: '/magento-2/magento-vault/'
aliases:
    - /integrations/ecommerce-integrations/magento2/faq/does-the-magento-2-plugin-support-magento-vault/
    - /payments/integrations/ecommerce-platforms/magento2/faq/activating-magento-vault/
---
Magento Vault enables you to use Instant Purchase, a feature that helps make repeat payments faster and easier, increasing conversion. 

## How it works

1. After filling out their credit card number, CVC, and expiry date at checkout, customers can give permission to store these details for future payments. 
2. MultiSafepay encrypts the sensitive payment details and stores the encrypted version on our secure, GDPR compliant servers. 
3. We return a non-sensitive identifier for the payment details, known as a token, which can only be used in your Magento webshop. 
4. The token is automatically stored in your Magento Vault. 
5. For subsequent payments, the customer can simply click **Instant purchase** at checkout. They don't need to re-provide any details. 

To see Instant Purchase in action, see Magento – [Instant purchase](https://magento.com/innovations-lab/instant-purchase).

## Requirements set by Mastercard and Visa

You must:  

- Include a checkbox at checkout for customers to give permission to tokenize their payment details (Already included in Magento Vault).
- Explain in your terms and conditions how you use and store their details.
- Inform customers how they can delete stored payment details.

## Activating Magento Vault

To activate Magento Vault, email a request to enable [recurring payments](/features/recurring-payments/) to <sales@multisafepay.com>

## Vault security

If you host Magento yourself, the security of the vault depends on the security of your server. 

However, the vault only contains tokens valid in your webshop. If your server is compromised, no actual payment details are at risk, only stored customer data.   