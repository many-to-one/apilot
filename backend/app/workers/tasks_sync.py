from app.workers.celery_app import celery_app

@celery_app.task
def sync_orders(integration: str, account_id: int):
    # tu ciężka logika
    return {"integration": integration, "account_id": account_id}
