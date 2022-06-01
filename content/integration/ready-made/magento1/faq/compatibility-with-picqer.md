---
title : "Compatibility with Picqer"
meta_title: "Magento 1 plugin - Compatibility with Picqer - MultiSafepay Docs"

read_more: "."
url: "/magento-1/picqer/"
aliases: 
    - /integrations/magento1/faq/how-can-i-update-the-plugin-for-magento1/
    - /integrations/magento1/faq/is-the-multisafepay-magento-1-plugin-compatible-with-picqer/
    - /payments/integrations/ecommerce-platforms/magento1/faq/compatibility-with-picqer/
---

To make the MultiSafepay Magento 1 plugin compatible with Picqer, follow two additional steps, because orders must not receive **Cancelled** status.

1. In your Magento 1 [backend](/glossaries/multisafepay-glossary/#backend), go to the MultiSafepay Connect settings.
2. Link **Expired** status to **Waiting** status.
2. Open `app\code\community\MultiSafepay\Msp\Model\Base.php`, and then copy the file to the local folder in the Magento structure.
3. Find the line `$order > cancel();` at the expired signal and remove it.

All expired orders retain **Waiting** status until you cancel them:

- Manually
- With a custom cronjob 
- Using a plugin
