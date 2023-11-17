from apscheduler.schedulers.background import BackgroundScheduler
from .dataUpdater import check_for_updated_data

scheduler = BackgroundScheduler()

def scheduled_job():
    print("Running scheduled job...")
    # Schedule the cron job to run every 12 hour on the last occurrence of Monday within the month
    scheduler.add_job(
        check_for_updated_data,
        'cron', day='last mon', hour='*/12'
    )

def start_scheduler():
    print("Starting background scheduler...")
    scheduler.start()
    scheduled_job()
