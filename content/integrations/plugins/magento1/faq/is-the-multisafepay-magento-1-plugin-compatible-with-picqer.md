---
title : "Is the MultiSafepay Magento 1 plugin compatible with Picqer?"
meta_title: "Magento 1 plugin Picqer compatibility - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

Yes, but you will have to follow two additional steps, because orders should not go to the Cancel state.

1. Go the the MultiSafepay Connect settings in you Magento 1 backend and link the status expired to Waiting
2. Open "app\code\community\MultiSafepay\Msp\Model\Base.php", copy the file to the local folder in the Magento structure
3. Find the line $order->cancel(); at the expired signal and remove it.

Now all the expired orders will keep the waiting status until you cancel them. You can do this by hand, schedule it with a custom cronjob or by using a plugin.
