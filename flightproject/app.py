from logging.handlers import RotatingFileHandler
import main, logging
from datetime import datetime


logging_date = datetime.today().strftime('%Y-%m-%d')


logging.basicConfig(
    handlers=[RotatingFileHandler('logs/flight_spider.log', maxBytes=100000, backupCount=10), logging.StreamHandler()],
    format='%(asctime)s | %(levelname)-8s | %(message)s', datefmt='%m/%d/%Y | %I:%M:%S %p',
    level=logging.DEBUG
)
app = main.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=False, host='0.0.0.0', port=8000)
