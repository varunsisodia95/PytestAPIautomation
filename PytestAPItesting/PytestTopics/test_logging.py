import logging
LOGGER = logging.getLogger(__name__) # Good practice


def test_mylogging():
    LOGGER.info("Info logs")
    LOGGER.warning("Warning logs")
    LOGGER.error("Error logs")
    LOGGER.critical("Critical logs")
    assert True
