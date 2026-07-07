from app.workers.tasks_sync import sync_orders

async def trigger_orders_sync(integration: str, account_id: int):
    task = sync_orders.delay(integration, account_id)
    return {"task_id": task.id}
