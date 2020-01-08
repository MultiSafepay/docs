---
title : "What is the IP range from MultiSafepay?"
meta_title: "FAQ General - IP range - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
In order to prevent a failed offline action for a status update (for instance by a HTTP 403 response), it is sometimes necessary to authorize our servers' ip address on your notification URL. 

To do so, please add the following IP ranges to your whitelist:

### Production
+ `213.189.0.0/23`
+ `185.99.128.0/22`    

### Test
+ `213.189.0.0/23`
+ `185.99.128.0/22`

### Qwindo
+ `185.99.130.125`
