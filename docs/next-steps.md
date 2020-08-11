# Chatbot: next steps

**Assuming this project continue evolving.**

## Send massive emails

To be able to send a massive emails, thousands of welcome emails, the structure has to be a rethink. I mean, a good improvement could be added to Celery, so the notification_processor will enqueue the message and we could have a lot of consumers. Another point of view could be to do an integration with an external email service.

## Clean architecture

This project has been developed following the DRF structure. Ideally, a nice improvement will be to adapt the structure to use a hexagonal structure.

I'm not an expert of hexagonal architecture (or any other), but an example could be:

- Adapters: Repositories for models (Provider, Currency, CurrencyExchangeRate). They implement `interfaces` and use Django (or others) models. They return `entity` objects.
- Entities: Objects representation of Django models
- Interfaces: Model interfaces to be implemented by different `repositories` types
- Services: Classes to interact with `adapters`

## Repository pattern

Another design pattern that could be used is `Repository`. 

Instead of access to Django models, I could declare a contract (interface) of what methods will be exposed. So, the different implementations, like Django, will extend this interface and implement those methods. In the future, if the project needs to swap Django for other ORM that change will be easily.