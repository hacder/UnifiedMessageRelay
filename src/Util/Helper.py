from typing import List, Union, Dict, Callable
import logging
from janus import Queue


# test attributes in config.yaml
def check_attribute(config: Dict, attributes: List[str], logger: logging.Logger) -> Union[str, None]:
    """
    Test if attributes exist in config
    :param config: config file
    :param attributes: list of attribute strings
    :param logger: log to this logger
    :return: str for first missing attribute, or None for Okay
    """
    for attr in attributes:
        if attr not in config:
            logger.error(f'{attr} not found in config.yaml')
            exit(-1)
    return None


# async put new task to janus queue
async def janus_queue_put_async(_janus_queue: Queue, func: Callable, *args, **kwargs):
    await _janus_queue.async_q.put((func, args, kwargs))


# sync put new task to janus queue
def janus_queue_put_sync(_janus_queue: Queue, func: Callable, *args, **kwargs):
    _janus_queue.sync_q.put((func, args, kwargs))
