"""Server executable"""

import slides
import logging
logger = slides.app.logger
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    slides.app.run("0.0.0.0", 5000)
    # For production:
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
