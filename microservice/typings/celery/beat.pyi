"""
This type stub file was generated by pyright.
"""

from collections import namedtuple
from functools import total_ordering
from threading import Thread
from kombu.utils.objects import cached_property
from .utils.log import get_logger

"""The periodic task scheduler."""
event_t = namedtuple('event_t', ('time', 'priority', 'entry'))
logger = get_logger(__name__)
DEFAULT_MAX_INTERVAL = 300
class SchedulingError(Exception):
    """An error occurred while scheduling a task."""
    ...


class BeatLazyFunc:
    """An lazy function declared in 'beat_schedule' and called before sending to worker.

    Example:

        beat_schedule = {
            'test-every-5-minutes': {
                'task': 'test',
                'schedule': 300,
                'kwargs': {
                    "current": BeatCallBack(datetime.datetime.now)
                }
            }
        }

    """
    def __init__(self, func, *args, **kwargs) -> None:
        ...
    
    def __call__(self):
        ...
    
    def delay(self):
        ...
    


@total_ordering
class ScheduleEntry:
    """An entry in the scheduler.

    Arguments:
        name (str): see :attr:`name`.
        schedule (~celery.schedules.schedule): see :attr:`schedule`.
        args (Tuple): see :attr:`args`.
        kwargs (Dict): see :attr:`kwargs`.
        options (Dict): see :attr:`options`.
        last_run_at (~datetime.datetime): see :attr:`last_run_at`.
        total_run_count (int): see :attr:`total_run_count`.
        relative (bool): Is the time relative to when the server starts?
    """
    name = ...
    schedule = ...
    args = ...
    kwargs = ...
    options = ...
    last_run_at = ...
    total_run_count = ...
    def __init__(self, name=..., task=..., last_run_at=..., total_run_count=..., schedule=..., args=..., kwargs=..., options=..., relative=..., app=...) -> None:
        ...
    
    def default_now(self):
        ...
    
    _default_now = ...
    __next__ = ...
    def __reduce__(self):
        ...
    
    def update(self, other):
        """Update values from another entry.

        Will only update "editable" fields:
            ``task``, ``schedule``, ``args``, ``kwargs``, ``options``.
        """
        ...
    
    def is_due(self):
        """See :meth:`~celery.schedule.schedule.is_due`."""
        ...
    
    def __iter__(self):
        ...
    
    def __repr__(self):
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def editable_fields_equal(self, other):
        ...
    
    def __eq__(self, other) -> bool:
        """Test schedule entries equality.

        Will only compare "editable" fields:
        ``task``, ``schedule``, ``args``, ``kwargs``, ``options``.
        """
        ...
    
    def __ne__(self, other) -> bool:
        """Test schedule entries inequality.

        Will only compare "editable" fields:
        ``task``, ``schedule``, ``args``, ``kwargs``, ``options``.
        """
        ...
    


class Scheduler:
    """Scheduler for periodic tasks.

    The :program:`celery beat` program may instantiate this class
    multiple times for introspection purposes, but then with the
    ``lazy`` argument set.  It's important for subclasses to
    be idempotent when this argument is set.

    Arguments:
        schedule (~celery.schedules.schedule): see :attr:`schedule`.
        max_interval (int): see :attr:`max_interval`.
        lazy (bool): Don't set up the schedule.
    """
    Entry = ...
    schedule = ...
    max_interval = ...
    sync_every = ...
    sync_every_tasks = ...
    _last_sync = ...
    _tasks_since_sync = ...
    logger = ...
    def __init__(self, app, schedule=..., max_interval=..., Producer=..., lazy=..., sync_every_tasks=..., **kwargs) -> None:
        ...
    
    def install_default_entries(self, data):
        ...
    
    def apply_entry(self, entry, producer=...):
        ...
    
    def adjust(self, n, drift=...):
        ...
    
    def is_due(self, entry):
        ...
    
    def populate_heap(self, event_t=..., heapify=...):
        """Populate the heap with the data contained in the schedule."""
        ...
    
    def tick(self, event_t=..., min=..., heappop=..., heappush=...):
        """Run a tick - one iteration of the scheduler.

        Executes one due task per call.

        Returns:
            float: preferred delay in seconds for next call.
        """
        ...
    
    def schedules_equal(self, old_schedules, new_schedules):
        ...
    
    def should_sync(self):
        ...
    
    def reserve(self, entry):
        ...
    
    def apply_async(self, entry, producer=..., advance=..., **kwargs):
        ...
    
    def send_task(self, *args, **kwargs):
        ...
    
    def setup_schedule(self):
        ...
    
    def sync(self):
        ...
    
    def close(self):
        ...
    
    def add(self, **kwargs):
        ...
    
    def update_from_dict(self, dict_):
        ...
    
    def merge_inplace(self, b):
        ...
    
    def get_schedule(self):
        ...
    
    def set_schedule(self, schedule):
        ...
    
    schedule = ...
    @cached_property
    def connection(self):
        ...
    
    @cached_property
    def producer(self):
        ...
    
    @property
    def info(self):
        ...
    


class PersistentScheduler(Scheduler):
    """Scheduler backed by :mod:`shelve` database."""
    persistence = ...
    known_suffixes = ...
    _store = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def setup_schedule(self):
        ...
    
    def get_schedule(self):
        ...
    
    def set_schedule(self, schedule):
        ...
    
    schedule = ...
    def sync(self):
        ...
    
    def close(self):
        ...
    
    @property
    def info(self):
        ...
    


class Service:
    """Celery periodic task service."""
    scheduler_cls = ...
    def __init__(self, app, max_interval=..., schedule_filename=..., scheduler_cls=...) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def start(self, embedded_process=...):
        ...
    
    def sync(self):
        ...
    
    def stop(self, wait=...):
        ...
    
    def get_scheduler(self, lazy=..., extension_namespace=...):
        ...
    
    @cached_property
    def scheduler(self):
        ...
    


class _Threaded(Thread):
    """Embedded task scheduler using threading."""
    def __init__(self, app, **kwargs) -> None:
        ...
    
    def run(self):
        ...
    
    def stop(self):
        ...
    


def EmbeddedService(app, max_interval=..., **kwargs):
    """Return embedded clock service.

    Arguments:
        thread (bool): Run threaded instead of as a separate process.
            Uses :mod:`multiprocessing` by default, if available.
    """
    ...

