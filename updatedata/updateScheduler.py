from .dataUpdater import check_for_updated_data

from app import scheduler

# @scheduler.task("cron", id="check_for_updated_data", minute="*/30") # for testing
# run every 12 hours on the last Monday of each month
@scheduler.task("cron", id="check_for_updated_data", day='last mon', hour='*/12')
def scheduled_job():
    print("Running scheduled job...")
    # Schedule the cron job to run every 12 hour on the last occurrence of Monday within the month
    with scheduler.app.app_context():
        check_for_updated_data()

