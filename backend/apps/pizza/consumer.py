from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.observer import model_observer

from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.group = 'pizzas'
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            return await self.close()

        await self.accept()
        await self.channel_layer.group_add(self.group, self.channel_name)

    @model_observer(PizzaModel, serializer_class=PizzaSerializer)
    async def pizza_model_activity(self, message, action, subscribing_request_ids, **kwargs):
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    @action()
    async def subscribe_to_pizza_model_changes(self, request_id, **kwargs):
        await self.pizza_model_activity.subscribe(request_id=request_id)